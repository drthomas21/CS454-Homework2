package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePosition extends GameResponse {

    private String position;
    private String username; 

    public ResponsePosition() {
        responseCode = Constants.SMSG_POSITION;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
        packet.addString(position);
        return packet.getBytes();
    }
    
	public String getPosition() {
		return position;
	}

	public void setPosition(double x, double y, double z) {
		this.position = x + "," + y + "," + z;
	}

	public void setUsername(String username)
	{
		this.username = username; 
	}
	public String getUsername()
	{
		return username; 
	}
}
