package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePrivateChat extends GameResponse {

    private String message;

    public ResponsePrivateChat() {
        responseCode = Constants.SMSG_PRIVATE_CHAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(message);
        return packet.getBytes();
    }
    
	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
}
