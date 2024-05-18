public class BankTest {
    public static void main(String[] args){
        // Create 3 bank accounts
        BankAccount acount1= new BankAccount(350,100);
        BankAccount acount2= new BankAccount(500,0);
        BankAccount acount3= new BankAccount(0,200);
        // Deposit Test
        // - deposit some money into each bank account's checking or savings account and display the balance each time
        acount1.depositMoney(150, "savings");
        System.out.println("balance: "+acount1.getcheckingBalance());
        acount1.depositMoney(0, "checking");
        System.out.println("balance: "+acount1.getcheckingBalance());
        // - each deposit should increase the amount of totalMoney

        // Withdrawal Test
        acount2.withdraw(100);
        System.out.println( "balance: "+acount2.getcheckingBalance());

        acount3.withdraw(50);
        System.out.println(acount3.getcheckingBalance());
        // - withdraw some money from each bank account's checking or savings account and display the remaining balance
        // - each withdrawal should decrease the amount of totalMoney
        System.out.println(acount1.getBalance());
        System.out.println(BankAccount.gettotalMoney());
        // Static Test (print the number of bank accounts and the totalMoney)

    }
}
