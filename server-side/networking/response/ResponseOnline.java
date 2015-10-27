package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseOnline extends GameResponse {

    private String user;

    public ResponseOnline() {
        responseCode = Constants.SMSG_ONLINE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(user);
        return packet.getBytes();
    }
    
	public String getUser() {
		return user;
	}

	public void setUser(String user) {
		this.user = user;
	}
}
