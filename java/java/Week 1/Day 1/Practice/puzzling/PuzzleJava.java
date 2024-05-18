import java.util.Random;
import java.util.ArrayList;


public class PuzzleJava {

    
    public static ArrayList<Integer> getTenRolls() {
        // create an ArrayList
        ArrayList<Integer> rolls = new ArrayList<>();
        // create a Random object
        Random random = new Random();
        // generate random numbers
        for (int i = 0; i < 10; i++) {
            // add random numbers to the ArrayList
            rolls.add(random.nextInt(20)+1);
        }
        return rolls;
    }

    public static char getRandomLetter() {
        // create an array with all 26 letters of the alphabet
        char[] alphabet = new char[26];
        for (int i = 0; i < 26; i++) {
            alphabet[i] = (char) ('a' + i);
        }
        // create a Random object
        Random random = new Random();
        
        // generate a random int
        int randomIndex = random.nextInt(26);
        
        // return the random letter
        return alphabet[randomIndex];
    }
    
    public static String generatePassword() {
        // generate a random password
        String password = "";
        for (int i = 0; i < 8; i++) {
            password += getRandomLetter();
        }
        // return the password
        return password; 
    }

    public static String[] getNewPasswordSet(int length){
        // create array
        String[] passwords = new String[length];
        // generate random numbers
        for (int i = 0; i < length; i++) {
            passwords[i] = generatePassword();
        }       
        return passwords;
    }
}
