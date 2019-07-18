var firstFraction = 7 / 9;
var secondFraction = 13 / 25; // <-- must be set first before called

var theBiggest = (function (a, b) {
    var result;
    a > b ? result = ["a", a] : result = ["b", b];
    return result;
})(firstFraction, secondFraction) // <-- the parenthesis invokes the function

console.log(theBiggest);
// console.log(theBiggest); <-- returns the function itself if no parenthesis added above

