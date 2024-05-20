//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Mamal mamal = new Mamal();
        Gorilla gorilla = new Gorilla();
        Bat bat = new Bat();


        mamal.displayEnergy();

        gorilla.displayEnergy();
        gorilla.throwSomething();
        gorilla.eatBananas();
        gorilla.climb();
        gorilla.displayEnergy();


        System.out.println("-----------------");
        bat.displayEnergy();
        bat.fly();
        bat.displayEnergy();
        bat.attackTown();
        bat.displayEnergy();




    }
}