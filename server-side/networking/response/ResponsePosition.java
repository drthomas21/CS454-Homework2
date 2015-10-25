package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePosition extends GameResponse {

    private String position;

    public ResponsePosition() {
        responseCode = Constants.SMSG_POSITION;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(position);
        return packet.getBytes();
    }
    
	public String getPosition() {
		return position;
	}

	public void setPosition(int x, int y, int z) {
		this.position = x + "," + y + "," + z;
	}
}
