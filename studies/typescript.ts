let e: number[] = [1,2,3,4,5]
console.log(e)

const ColorRed = 0;
const ColorGreen = 1;
const ColorBlue =2;

//can only have a signature noimplementation in interface
interface Point{ //should be upper case P 
    x:number,
    y:number,
    // draw:() => void //cannot implement anything so we use class
}

class Point {
    x:number;
    y:number;

    draw(){
        console.log('X: ' + this.x + ', Y: ' + this.y);
    }

    getDistance(another: Point){

    }
}

enum Color { Red =0, Green =1, Blue=2};
let backgroundColor = Color.Red;

let message;
message = 'abc';

let endswith=(<string>message).endsWith('c')

let log = function(mes){
    console.log(mes)
}

let dolog =(mes) => console.log(mes);

let point = new Point();
point.x = 1;
point.y =2;
point.draw();


