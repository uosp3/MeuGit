"use strict";
//https://www.youtube.com/watch?v=ry3rVZRapTk
function fsoma(...n) {
    let s = 0;
    n.forEach((en) => {
        s += en;
    });
    return s;
}
console.log(fsoma(10, 20, 30));
