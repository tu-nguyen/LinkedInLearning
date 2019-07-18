// const is constant and cannot be changed
// let is block scope variable, smaller scope than var

const MYCONSTANT = 5;
console.log(MYCONSTANT);
// MYCONSTANT = 6; script.js:6 Uncaught TypeError: Assignment to constant variable.

function logScope() {
    var localVar = 2;

    if (localVar) {
        //var localVar = "I'm different";
        //console.log("nested localVar: ", localVar); logScope localVar would change as well

        let localVar = "I'm different";
        console.log("nested localVar: ", localVar);
    }

    console.log("logScope localVar: ", localVar);
}

logScope();