var e = [1, 2, 3, 4, 5];
console.log(e);
var ColorRed = 0;
var ColorGreen = 1;
var ColorBlue = 2;
var Point = /** @class */ (function () {
    function Point() {
    }
    Point.prototype.draw = function () {
        console.log('X: ' + this.x + ', Y: ' + this.y);
    };
    Point.prototype.getDistance = function (another) {
    };
    return Point;
}());
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
;
var backgroundColor = Color.Red;
var message;
message = 'abc';
var endswith = message.endsWith('c');
var log = function (mes) {
    console.log(mes);
};
var dolog = function (mes) { return console.log(mes); };
var point = new Point();
point.x = 1;
point.y = 2;
point.draw();
