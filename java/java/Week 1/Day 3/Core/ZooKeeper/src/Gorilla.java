public class Gorilla extends Mamal {

    public Gorilla(){};
    public  void throwSomething(){
        this.setEnergy(getEnergy()-5);
        System.out.println("Gorilla throw something");
    }
    public void eatBananas(){
        this.setEnergy(getEnergy()+10);
        System.out.println("Gorilla satisfied");
    }
    public void climb(){
        this.setEnergy(getEnergy()-10);
        System.out.println("Gorilla climb a tree");
    }
}
