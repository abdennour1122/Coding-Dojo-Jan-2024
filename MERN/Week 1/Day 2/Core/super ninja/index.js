class Ninja{
    constructor(name) {
        this.name = name;
        this.health = 90;
        this.speed = 3;
        this.strength = 3;
    }
    sayName(){
        console.log(`your health is ${this.health}`)
    }
    showStats(){
        console.log(` your name is ${this.name}, your health is ${this.health},your speed is ${this.speed} and your strength is ${this.strength}`)
    }
    drinkshake(){
        this.health+=10
        console.log(this.health)
    }
}


class Sensei extends Ninja{
    constructor(name){
        super(name)
        this.wisdom=10
    }
    speakwisdom(){
        super.drinkshake();
        console.log("zadezds");

    }

    
}
const sensei1=new Sensei("abdennour")
sensei1.speakwisdom()

