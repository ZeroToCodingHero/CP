// Declare a variable named message
/*
let message; 

// store the string 'Hello' in the variable named message
message = 'Hello'
*/

// Declare a variable named message and store the string 'Hello' in it
let message = 'Hello World';

const myBirthday = '16-09-2003';

myBirthday = '01-01-2001'; // error, can't reassign the constant!


// Initialize x to 10
let x = 10;

console.log("Initial x:", x);

// Most Common Arithmetic Operators
console.log("Addition:", x + 5);
console.log("Subtraction:", x - 3);
console.log("Multiplication:", x * 2);
console.log("Division:", x / 2);
console.log("Modulus (remainder):", x % 3);
console.log("Exponentiation:", x ** 2);

// Most Common Assignment Operators
x = 10;           // reset
console.log("\nAfter reset, x =", x);

x += 5;           // x = x + 5
console.log("x += 5 →", x);

x -= 3;           // x = x - 3
console.log("x -= 3 →", x);

x *= 2;           // x = x * 2
console.log("x *= 2 →", x);

x /= 2;           // x = x / 2
console.log("x /= 2 →", x);

// Most Common Comparison Operators
console.log("\nComparison Operators:");
console.log("x == 10:", x == 10);
console.log("x === 10:", x === 10);
console.log("x > 5:", x > 5);
console.log("x < 20:", x < 20);
console.log("x >= 10:", x >= 10);
console.log("x <= 10:", x <= 10);

// Most Common Logical Operators
let a = true;
let b = false;
console.log("\nLogical Operators:");
console.log("AND (true && false):", a && b);
console.log("OR (true || false):", a || b);
console.log("NOT (!true):", !a);