// GIVEN
console.log(example);
var example = "I'm the example!";
//var example
// console.log(example); // logs undefined
// example = "I'm the example!";

// two
console.log(example);
let example = "I'm the example!";    
//console.log(example);//error
// let example="i'm the example!";

//three
console.log(hello);                                   
var hello = 'world'; 
//var hello                                
// console.log(hello);//undefined;
// hello = "world"

// four
var needle = 'haystack';
test();
function test(){
    var needle = 'magnet';
    console.log(needle);
}
// var needle= "haystack";
//function test()=magnet;

// five
var brendan = 'super cool';
function print(){
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);
//var brendan="super cool"
// function print()="only okay"

//six
var food = 'chicken';
console.log(food);
eat();
function eat(){
    food = 'half-chicken';
    console.log(food);
    var food = 'gone';
}
// var food="chicken"
//console.log(food)//"chiken";
//function eat():half-chicken;

//seven
mean();
console.log(food);
var mean = function() {
    food = "chicken";
    console.log(food);
    var food = "fish";
    console.log(food);
}
console.log(food);
//var mean
// console.log(food)/undefined
// mean=fish

// eight
console.log(genre);
var genre = "disco";
rewind();
function rewind() {
    genre = "rock";
    console.log(genre);
    var genre = "r&b";
    console.log(genre);
}
console.log(genre);
// var genre;
// rewind();
//function rewind()="r&b";
//genre=disco

//nine
dojo = "san jose";
console.log(dojo);
learn();
function learn() {
    dojo = "seattle";
    console.log(dojo);
    var dojo = "burbank";
    console.log(dojo);
}
console.log(dojo);
// dojo="san jose";
//undefined
//"seattle"
//"burbank" 
//"san jose"

