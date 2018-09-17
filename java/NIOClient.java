
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.SocketChannel;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.net.ConnectException;

/**
 * Created by litao on 2018/8/31.
 */
public class NIOClient {

    public static void testSocketChannelConcurrent() throws Exception {
        try {
            final SocketChannel channel = SocketChannel.open(new InetSocketAddress("10.42.193.40", 5678));

            // ȷ��ͨ���ѽ���
            while (!channel.finishConnect())
                ;

            Selector selector = Selector.open();
            // ������ģʽ,Ĭ������
            channel.configureBlocking(false);
            // ע��OP_READ��Ϣ
            channel.register(selector, SelectionKey.OP_READ);

            // �����߳�
            new Thread(new Heartbeats(channel)).start();

            while (true) {
                // selectNow()���������ؽ��
                // if (selector.selectNow() > 0) {
                // �����Ƿ��ж�д�¼�������selectorÿ��1s������һ��
                // if (selector.select(1000) > 0) {
                // ����,ֻ�е�����һ��ע����¼�������ʱ��Ż����
                if (selector.select() > 0) {

                    // ��ȡ�����Ѿ�Ready��keys,ͨ��keys�����ҵ���Ӧ��channel
                    Set<SelectionKey> selectionKeys = selector.selectedKeys();
                    System.out.println("start iterator keys, size:{}" + selectionKeys.size());
                    Iterator<SelectionKey> keyIterator = selectionKeys.iterator();
                    while (keyIterator.hasNext()) {
                        SelectionKey key = keyIterator.next();
                        // a channel is ready for reading
                        if (key.isReadable()) {
                            System.out.println("key.isReadable(), startRead");
                            ByteBuffer input = ByteBuffer.allocate(4096);
                            // ͨ��key.channel()�����ҵ�channel
                            SocketChannel keyChannel = (SocketChannel) key.channel();
                            int readByte = keyChannel.read(input);
                            System.out.println("readByte " + readByte);
                            // д��������Ҫ��flip����
                            input.flip();
                            if (readByte == -1) {
                                System.out.println("readByte == -1, return!");
                                // return;
                                testSocketChannelConcurrent();
                            }
                            for (int i = 0; i < readByte; i++) {
                                System.out.println("read [" + i + "]:" + input.get());
                            }
                        }
                        // ��������֮��ɾ��key,�����һֱ������selector.selectedKeys()
                        keyIterator.remove();
                    }
                }
            }
        } catch (ConnectException e) {
            // ��������
            System.out.println("sleep(10000)");
            Thread.sleep(10000);
            System.out.println("try to reconnect......");
            testSocketChannelConcurrent();
        }

    }

    private static class Heartbeats implements Runnable {

        private SocketChannel socketChannel;

        public Heartbeats(SocketChannel socketChannel) {
            this.socketChannel = socketChannel;
        }

        public void run() {
            try {
                while (true) {
                    System.out.println("Heartbeats sleep(60000)");
                    Thread.sleep(60000);
                    ByteBuffer output = ByteBuffer.allocate(5);
                    output.put((byte) 1);
                    output.putInt(0);
                    output.flip();
                    socketChannel.write(output);
                    System.out.println("Heartbeats write complete");
                }
            } catch (Exception e) {
                // TODO: handle exception
            }

        }
    }

    // **************************
    // *** test socket client ***
    // **************************

    public static void main(String[] args) throws Exception {
        testSocketChannelConcurrent();
    }

}