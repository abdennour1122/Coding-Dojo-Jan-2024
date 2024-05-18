import java.util.ArrayList;
import java.util.Random;
public class TestPuzzleJava {
    
	public static void main(String[] args) {
        //! getTenRolls
        // create an instance of the PuzzleJava class
		PuzzleJava puzzle = new PuzzleJava();
        // create an ArrayList and call the getTenRolls method
		ArrayList<Integer> randomRolls = puzzle.getTenRolls();
        // print the ArrayList
		System.out.println(randomRolls);

        System.out.println("====================================");

        //! getRandomLetter
        // call the getRandomLetter method
        char randomLetter = puzzle.getRandomLetter();
        // print the random letter
        System.out.println(randomLetter);

        System.out.println("====================================");
		
        //! generatePassword
        // call the generatePassword method
        String randomPassword = puzzle.generatePassword();
        // print the random password
        System.out.println(randomPassword);

        System.out.println("====================================");

        //! getNewPasswordSet
        // call the getNewPasswordSet method
        String[] randomPasswords = puzzle.getNewPasswordSet(5);
        // print the random passwords
        for (int i = 0; i < randomPasswords.length; i++) {
            System.out.println(randomPasswords[i]);
        }
	}
}
