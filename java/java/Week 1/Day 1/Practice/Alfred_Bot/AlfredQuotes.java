import java.util.Date;

public class AlfredQuotes {
    
    // Returns a basic greeting message
    public String basicGreeting() {
        return "Hello, lovely to see you. How are you?";
    }
    
    // Returns a personalized greeting message for a guest
    public String guestGreeting(String name) {
        String greetingGuest =  String.format("Hello, %s. Lovely to see you.", name);
        return greetingGuest;
    }
    
    // Returns the current date announcement
    public String dateAnnouncement() {
        Date currentDate = new Date();
        return "It is currently " + currentDate.toString() + ".";
    }
    
    // Responds based on the conversation input before Alexis is mentioned
    public String respondBeforeAlexis(String conversation) {
        if (conversation.indexOf("Alexis") != -1) {
            return "Right away, sir. She certainly isn't sophisticated enough for that.";
        } else if (conversation.indexOf("Alfred") != -1) {
            return "At your service. As you wish, naturally.";
        } else {
            return "Right. And with that I shall retire.";
        }
    }
    //ninjas bonus
    // Returns a personalized greeting message for a guest with a specific day period
    public String guestGreeting(String name, String dayPeriod) {
        String greeting = String.format("Good %s, %s. Lovely to see you.", dayPeriod, name);
        return greeting;
    }
}


