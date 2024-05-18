public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        
        // Menu variables (add yours below)
        double mochaPrice = 3.5;
        double dripCoffee = 5.0;
        double latte = 4.0;
        double cappuccino = 4.5;
    
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Sam";
        String customer3 = "jimmy";
        String customer4 = "Noah";

    
        // Order completions (add yours below)
        boolean isReadyOrder1 = true;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = false;
        boolean isReadyOrder4 = true;    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
    	// ** Your customer interaction print statements will go here ** //
        //! Cindhuri Order
        System.out.println(generalGreeting + customer1 ); // Displays "Welcome to Cafe Java, Cindhuri"
        System.out.println(isReadyOrder1 ? readyMessage + displayTotalMessage + mochaPrice : pendingMessage);

        System.out.println("*************************************");

        //! Sam Order
        System.out.println(generalGreeting + customer4);
        if(isReadyOrder4){
            System.out.println(readyMessage + displayTotalMessage + cappuccino);
        }
        else{
            System.out.println(pendingMessage);
        }

        System.out.println("*************************************");

        //! Sam Order
        if (isReadyOrder2){
            System.out.println(generalGreeting + customer2 + readyMessage + displayTotalMessage + 2 * latte);
        }
        else{
            System.out.println(generalGreeting + customer2 + pendingMessage);
        }


        System.out.println("*************************************");


        //! Jimmy Order
        System.out.println(generalGreeting + customer3);
        if (isReadyOrder3) {
            System.out.println(displayTotalMessage + latte);
        } else {
            double newTotal = latte - dripCoffee;
            System.out.println(displayTotalMessage + newTotal);
        }

    }
}
