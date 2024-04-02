class Unit {
    constructor(name, cost, power,) {
        this.name = name;
        this.cost = cost;
        this.power = power;
        this.resilience = 4;

}
    attack(target){
        target.resilience-=this.power
    }
}
Red_belt=new Unit("Red belt ninja",3,3)
Black=new Unit("Black belt ninja",4,5)
class Effect {
    constructor(name, cost, stat,magnitud) {
        this.name = name;
        this.cost = cost;
        this.stat = stat;
        this.magnitud = magnitud;

}
    play(target){
        if (this.stat=="resiience") {
            target.resilience+=this.magnitud
        }
        if (this.stat=="power") {
            target.power+=this.magnitud
        }
    }
    
}
Hard_algo=new Effect("Hard Algorithm",2,"resiience",3)
rejection=new Effect("Unhandled Promise Rejection",1,"resiience",-2)
pair=new Effect("pair programming",3,"power",2)
Hard_algo.play(Red_belt)
rejection.play(Red_belt)
pair.play(Red_belt)
Red_belt.attack(Black)