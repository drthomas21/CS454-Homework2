package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseHeartbeat extends GameResponse {

    public ResponseHeartbeat() {
        responseCode = Constants.SMSG_HEARTBEAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        return packet.getBytes();
    }
}
