public class Mamal {

    private int energy=100;

    public Mamal(){
        this.energy= 100;
    }

    public int getEnergy() {
        return energy;
    }

    public void setEnergy(int energy) {
        this.energy = energy;
    }

    public void displayEnergy(){
        System.out.println("Energy: "+energy);
    }


}
