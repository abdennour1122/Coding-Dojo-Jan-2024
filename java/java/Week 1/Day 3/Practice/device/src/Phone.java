public class Phone extends Devices{

    public void Call(){
        System.out.println("you make a call");
        battery -= 5;
        displayBattery();
    }
    public void Game(){
        System.out.println("you play a game");
        battery -= 20;
        displayBattery();
    }
    public void Charging(){
        System.out.println("you charge your phone ");
        battery +=50;
        displayBattery();
    }
}
