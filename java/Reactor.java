import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.SocketChannel;
import java.util.Set;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.sof.bas.Bytes2util;
import com.sof.bas.Util2Bytes;

public class Reactor implements Runnable {
	private static Logger logger = LoggerFactory.getLogger(Reactor.class);

	public Manager manager;
	final Selector selector;
	final SocketChannel socket;

	public SelectionKey sk;
	public InetSocketAddress serveraddress;

	static final int MESSAGE_LENGTH_HEAD = 4;
	private byte[] head = new byte[4];
	private int bodylen = -1;
	private int sequence = 0;

	public boolean done = true;

	public Reactor(String ip, int port, Manager manager) throws IOException {
		this.manager = manager;
		selector = Selector.open();
		socket = SocketChannel.open();
		socket.configureBlocking(true);
		serveraddress = new InetSocketAddress(ip, port);
	}

	public boolean connecttoserver() throws IOException {
		boolean result = false;
		socket.connect(serveraddress);
		result = true;
		new Thread(this).start();
		manager.setestablished();

		socket.configureBlocking(false);
		sk = socket.register(selector, 0);
		sk.interestOps(SelectionKey.OP_READ);
		selector.wakeup();

		return result;
	}

	public void run() {
		try {
			while (done) {
				logger.debug("selector is waitting  event....");
				selector.select();
				Set<SelectionKey> keys = selector.selectedKeys();
				if (keys.size() == 0) {
					logger.debug("nothing happened");
					continue;
				}

				for (SelectionKey key : keys) {
					if (key.isReadable()) {
						logger.debug("Readable event happened");
						readdata();
					} else if (key.isWritable()) {
						logger.debug("Writeable event happened");
					} else {
						logger.debug("others event happened");
					}
				}
				keys.clear();
			}
			logger.debug("thread exit");
		} catch (IOException ex) {
			logger.error(ex.getMessage());
		}
	}

	public void readdata() {
		try {
			read();
		} catch (IOException ex) {
			try {
				logger.debug("disconnection event happened");
				socket.close();
				synchronized (manager) {
					manager.setdisconnect();
					manager.notifyAll();
					done = false;
				}
			} catch (IOException e) {
				logger.error(e.getMessage());
			}
			sk.cancel();
		}

	}

	public void read() throws IOException {
		ByteBuffer input = ByteBuffer.allocate(1024 * 10000);
		socket.read(input);
		input.flip();
		sk.interestOps(SelectionKey.OP_READ);

		while (input.remaining() > 0) {
			if (bodylen < 0) {
				if (input.remaining() >= MESSAGE_LENGTH_HEAD) {
					input.get(head, 0, 4);
					bodylen = Util2Bytes.bytes2bigint(head);

				} else {
					break;
				}
			} else if (bodylen > 0) {
				if (input.remaining() >= bodylen) {

					byte[] body = new byte[bodylen];
					input.get(body, 0, bodylen);
					sequence++;
					byte[] headandbody = new byte[MESSAGE_LENGTH_HEAD + bodylen];
					System.arraycopy(head, 0, headandbody, 0, head.length);
					System.arraycopy(body, 0, headandbody, head.length,
							body.length);
					MsgBean message = new MsgBean(sequence, headandbody, socket);
					Process.getInstance().queue.put(message);
					bodylen = -1;

				} else {
					break;
				}
			} else if (bodylen == 0) {
				sequence++;
				byte[] headandbody = new byte[MESSAGE_LENGTH_HEAD + bodylen];
				System.arraycopy(head, 0, headandbody, 0, head.length);
				MsgBean message = new MsgBean(sequence, headandbody, socket);
				Process.getInstance().queue.put(message);
				bodylen = -1;
			}
		}
	}
}
