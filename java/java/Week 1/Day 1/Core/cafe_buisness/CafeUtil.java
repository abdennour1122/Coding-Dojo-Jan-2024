import java.util.ArrayList;



public class CafeUtil {

    // Get Streak Goal
    public static int getStreakGoal() {
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            sum += i;
        }
        return sum;
    }
    // Get Streak Goal Ninja Bonus
    public static int getStreakGoal(int numWeeks) {
        int sum = 0;
        for (int i = 1; i <= numWeeks; i++) {
            sum += i;
        }
        return sum;
    }

    // Order Total
    public static double getOrderTotal(double[] lineItems) {
        double sum = 0;
        for (double item : lineItems) {
            sum += item;
        }
        return sum;
    }

    // Display Menu
    public static void displayMenu(ArrayList<String> menuitems) {
        System.out.println("Menu\n");
        for (int i = 0; i < menuitems.size(); i++) {
            System.out.println(i + " " + menuitems.get(i));
        }
    }


    // Add Customer
    public static void addCustomer(ArrayList<String> customers) {
        System.out.println("Please enter your name: ");
        //get user input from the terminal and store it in the variable
        String name = System.console().readLine();
        //add the name to the list
        customers.add(name);
        //print a greeting message
        System.out.println("Hello " + name + "!");
        //print the number of customers in the cafe
        System.out.println("We have " + customers.size() + " customers in the cafe.");
        //print the list of customers
        System.out.println("Customers in the cafe: " + customers);
    }

}