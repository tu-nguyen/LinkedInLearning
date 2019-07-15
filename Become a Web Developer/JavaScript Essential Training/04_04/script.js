function findBiggestFraction(a, b) {
    var res;
    a > b ? res = ["firstFraction", a] : res = ["secondFraction", b];
    return res;
}

var firstFraction = 3 / 4;
var secondFraction = 5 / 7;

var fractionRes = findBiggestFraction(firstFraction, secondFraction);

console.log(fractionRes);
