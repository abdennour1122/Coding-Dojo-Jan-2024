public class BankAccount {
    // MEMBER VARIABLES
    private double checkingBalance;
    private double savingsBalance;

    private static int accounts =0;
    private static double totalMoney=0; // refers to the sum of all bank account checking and savings balances

    // CONSTRUCTOR
    // Be sure to increment the number of accounts
    public BankAccount (double checkingBalance , double savingsBalance ){
        this.checkingBalance= checkingBalance;
        this.savingsBalance=savingsBalance;
        accounts++;
    }

    // GETTERS
    // for checking, savings, accounts, and totalMoney
    public double getcheckingBalance(){
        return checkingBalance;
    }
    public double getsavingsBalance(){
        return savingsBalance;
    }
    public static int getaccounts(){
        return accounts;
    }
    public static double gettotalMoney(){
        return totalMoney;
    }

    // METHODS

    public void depositMoney(double amount, String accountType){
        if(amount>0){
            if(accountType.equals("checking")){
                checkingBalance += amount;
            }else if(accountType.equals("savings")){
                checkingBalance+= amount ;
            }
            totalMoney+=amount;
        }
    }
    // deposit
    public double withdraw(double money){
        if(checkingBalance>money){
            checkingBalance-=money;
            totalMoney-= money;
        }else{
            System.out.println("insufficient founds");
        }
        return checkingBalance;
    }
    // - users should be able to deposit money into their checking or savings account
    // withdraw 
    // - users should be able to withdraw money from their checking or savings account
    // - do not allow them to withdraw money if there are insufficient funds
    // - all deposits and withdrawals should affect totalMoney
    // getBalance
    public  double getBalance(){
        return checkingBalance + savingsBalance;
    }
    // - display total balance for checking and savings of a particular bank account
}
