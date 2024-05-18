import java.util.HashMap;




public class Hashmatique {

    // create a private HashMap  variable
    private HashMap<String, String> trackList = new HashMap<String, String>();


    // create a public method that adds a song to the trackList
    public void addSong(String title, String lyrics) {
        trackList.put(title, lyrics);
    }

    // create a public method that retrieves a song from the trackList
    public String getSong(String title) {
        return trackList.get(title);
    }
    
    
    // create a public method that retrieves all the songs from the trackList
    public void getTrackList() {
        for (String key : trackList.keySet()) {
            System.out.println("Title : " + key + " / lyrics : " + trackList.get(key));
        }
    }
}