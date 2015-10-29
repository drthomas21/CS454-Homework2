package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseSelectchar extends GameResponse {

    private String message;
    private String position; 

    public ResponseSelectchar() {
        responseCode = Constants.SMSG_SELECTION;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(position);
        return packet.getBytes();
    }
    
	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
	
	public void setPosition(double x, double y, double z, double h) {
		this.position = x + "," + y + "," + z + "," + h;
	}
	public String getPosition()
	{
		return this.position; 
	}

	public void setPosition() {
		this.position = "";
		
	}
}
