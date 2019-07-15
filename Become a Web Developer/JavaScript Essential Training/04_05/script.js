var a = 5 / 7;
var b = 18 / 25;

var theBiggest = function (a, b) {
    var res;
    a > b ? res = ["a: ", a] : res = ["b: ", b];
    // console.log(res);
    return res;
}

console.log(theBiggest(a, b));