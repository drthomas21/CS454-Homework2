package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseSaveexit extends GameResponse {

    private short answer;

    public ResponseSaveexit() {
        responseCode = Constants.SMSG_SAVE_EXIT_GAME;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(answer);
        return packet.getBytes();
    }
    
	public short getAnswer() {
		return answer;
	}

	public void setAnswer(short answer) {
		this.answer = answer;
	}
}
