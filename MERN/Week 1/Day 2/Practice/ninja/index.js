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
const ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
ninja1.showStats();
ninja1.drinkshake();
