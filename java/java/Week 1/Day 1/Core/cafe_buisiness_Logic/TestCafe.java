import java.util.ArrayList;

public class TestCafe {
    public static void main(String[] args) {
        
        
        CafeUtil appTest = new CafeUtil();
        
        /* ============ App Test Cases ============= */
        // Get Streak Goal Test
        System.out.println("----- Streak Goal Test-----");
        System.out.printf("Purchases needed by week 10: %s \n\n", appTest.getStreakGoal());

        // Get Streak Goal Ninja Bonus Test
        System.out.println("----- Streak Goal Ninja Bonus Test-----");
        System.out.printf("Purchases needed by week : %s \n\n", appTest.getStreakGoal(5));

        // Order total test
        System.out.println("----- Order Total Test-----");
        double[] lineItems = {3.5, 1.5, 4.0, 4.5};
        System.out.printf("Order total: %s \n\n",appTest.getOrderTotal(lineItems));
        

        // Display Menu Test
        System.out.println("----- Display Menu Test-----");
        // Create a list of menu items
        ArrayList<String> menu = new ArrayList<String>();
        menu.add("drip coffee");
        menu.add("cappuccino");
        menu.add("latte");
        menu.add("mocha");
        appTest.displayMenu(menu);
    

        // Add Customer Test
        System.out.println("\n----- Add Customer Test-----");
        // Create a list of customers
        ArrayList<String> customers = new ArrayList<String>();
        // Add customers
        for (int i = 0; i < 6; i++) {
            appTest.addCustomer(customers);
            System.out.println("\n");
        }
    }
}

