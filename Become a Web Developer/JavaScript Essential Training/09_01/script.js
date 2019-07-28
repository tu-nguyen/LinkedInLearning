var i = 1;
var reps = 0;

while (i < 567) {
    ++reps;
    console.log(reps + " reps gives us " + i);
    i *= 2.1;
}

// do while loop same as above but will run at least once
// do {
//     ++reps;
//     console.log(reps + " reps gives us " + i);
//     i *= 2.1;
// } while (i < 567);