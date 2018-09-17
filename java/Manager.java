import java.io.IOException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.sof.bas.Config;
import com.sof.exe.Client;

public class Manager implements Runnable {
	private static Logger logger = LoggerFactory.getLogger(Client.class);
	public boolean connstate = false;
	public String ip = Config.getInstance().getStringValue("ip");
	public int port = Config.getInstance().getIntValue("port");

	public void setestablished() {
		connstate = true;
	}

	public void setdisconnect() {
		connstate = false;
	}

	public boolean getconnstate() {
		return connstate;
	}

	public void run() {
		while (true) {
			Reactor reactor = null;
			try {
				reactor = new Reactor(ip, port, this);
				reactor.connecttoserver();
				logger.error("connect to server sucessful " + reactor.serveraddress.toString());
			} catch (IOException ex) {
				logger.error("connect to server unsucessful " + reactor.serveraddress.toString());
				continue;
			}

			while (getconnstate()) {
				try {
					synchronized (this) {
						this.wait();
						logger.debug("got a news about disconnection and reconnect to server" +  reactor.serveraddress.toString());
					}
				} catch (InterruptedException e) {
					logger.debug(e.getMessage());
				}
			}
		}
	}
}
