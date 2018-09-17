
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

            // 确认通道已建立
            while (!channel.finishConnect())
                ;

            Selector selector = Selector.open();
            // 非阻塞模式,默认阻塞
            channel.configureBlocking(false);
            // 注册OP_READ消息
            channel.register(selector, SelectionKey.OP_READ);

            // 心跳线程
            new Thread(new Heartbeats(channel)).start();

            while (true) {
                // selectNow()会立即返回结果
                // if (selector.selectNow() > 0) {
                // 无论是否有读写事件发生，selector每隔1s被唤醒一次
                // if (selector.select(1000) > 0) {
                // 阻塞,只有当至少一个注册的事件发生的时候才会继续
                if (selector.select() > 0) {

                    // 获取所有已经Ready的keys,通过keys可以找到对应的channel
                    Set<SelectionKey> selectionKeys = selector.selectedKeys();
                    System.out.println("start iterator keys, size:{}" + selectionKeys.size());
                    Iterator<SelectionKey> keyIterator = selectionKeys.iterator();
                    while (keyIterator.hasNext()) {
                        SelectionKey key = keyIterator.next();
                        // a channel is ready for reading
                        if (key.isReadable()) {
                            System.out.println("key.isReadable(), startRead");
                            ByteBuffer input = ByteBuffer.allocate(4096);
                            // 通过key.channel()可以找到channel
                            SocketChannel keyChannel = (SocketChannel) key.channel();
                            int readByte = keyChannel.read(input);
                            System.out.println("readByte " + readByte);
                            // 写完数据需要做flip操作
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
                        // 遍历结束之后删除key,否则会一直存在于selector.selectedKeys()
                        keyIterator.remove();
                    }
                }
            }
        } catch (ConnectException e) {
            // 断链重连
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