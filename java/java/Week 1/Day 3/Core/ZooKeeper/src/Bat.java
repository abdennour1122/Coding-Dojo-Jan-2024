public class Bat extends Mamal{


    public void fly(){
        this.setEnergy(getEnergy()-50);
        System.out.println("Bat is airborne");
    }
    public void eatHumans(){
        this.setEnergy(getEnergy()+25);
        System.out.println("Bat is eating humans");
    }
    public void attackTown(){
        this.setEnergy(getEnergy()-100);
        System.out.println("Bat is attacking town");
    }
}
