// Question 1. Declare firstName, lastName, country, city, age, isMarried, year variable and assign value to it and use the typeof operator to check different data types.
let firstame = "Shriya";
let lastname = "Shukla";
let country = "India";
let city = "Kanpur";
let age = 22;
let isMarried = "No";
let year = 2022;
console.log(typeof(firstame));
console.log(typeof(lastname));
console.log(typeof(country));
console.log(typeof(city));
console.log(typeof(age));
console.log(typeof(isMarried));
console.log(typeof(year));

// Question 2. Boolean value is either true or false.
// a. Write three JavaScript statements which provide truthy value.
if (true)
if ("false")
if ({})

// b. Write three JavaScript statements which provide falsy value.
if (false)
if ("")
if (undefined)

// Question 3. Figure out the result of the following expressions first without using console.log().

// a. 4 > 3 && 10 < 12
console.log(4 > 3 && 10 < 12);

// b. 4 > 3 && 10 > 12
console.log(4 > 3 && 10 > 12);

// c. 4 > 3 || 10 < 12
console.log(4 > 3 || 10 < 12);

// d. 4 > 3 || 10 > 12
console.log(4 > 3 || 10 > 12);

// e. !(4 > 3)
console.log(!(4 > 3));

// f. !(4 < 3)
console.log(!(4 < 3));

// g. !(false)
console.log(!(false));

// h. !(4 > 3 && 10 < 12)
console.log(!(4 > 3 && 10 < 12));

// i. !(4 > 3 && 10 > 12)
console.log(!(4 > 3 && 10 > 12));

// j. !(4 === '4')
console.log(!(4 === '4'));

// Question 4. Even numbers are divisible by 2 and the remainder is zero. How do you check, if a number is even or not using JavaScript?

let n = 7;
if (n % 2 == 0){
    console.log("Even");
}
else{
    console.log("Odd");
}

// Question 5. Write a code which can give grades to students according to theirs scores:
// a. 80-100, A b. 70-79, B c. 60-69, C d. 50-59, D e. 0-49, F
let score = 70;
switch (true){
    case score >= 80 && score <= 100:
        console.log("Grade A");
        break;
    case score >= 70 && score <= 79:
        console.log("Grade B");
        break; 
    case score >= 60 && score <= 69:
        console.log("Grade C");
        break;  
    case score >= 50 && score <= 59:
        console.log("Grade D");
        break;  
    case score >= 0 && score <= 49:
        console.log("FAIL");
        break; 
}

// Question 6. Write a program which tells the number of days in a month.
let mon = 9;
switch(mon){
    case 1 : 
            console.log(31);
            break;
    case 2 : 
            console.log(28);
            break; 
    case 3 : 
            console.log(31);
            break;    
    case 4 : 
            console.log(30);
            break; 
    case 5 : 
            console.log(31);
            break;
    case 6 : 
            console.log(30);
            break; 
    case 7 : 
            console.log(31);
            break;    
    case 8 : 
            console.log(31);
            break;                               
    case 9 : 
            console.log(30);
            break;
    case 10 : 
            console.log(31);
            break; 
    case 11 : 
            console.log(30);
            break;    
    case 12 : 
            console.log(31);
            break; 
}

// Question 7. Create a human readable time format using the Date time object
// a. YYYY-MM-DD HH:mm
const now = new Date();
console.log(now.getFullYear() + "-" + now.getMonth() + "-" + now.getDate() + " " + now.getHours() + ":" + now.getMinutes());

// b. DD-MM-YYYY HH:mm
console.log(now.getDate() + '-' + now.getMonth() + '-' + now.getFullYear() + ' ' + now.getHours() + ':' + now.getMinutes());

// c. DD/MM/YYYY HH:mm
console.log(now.getDate() + '/' + now.getMonth() + '/' + now.getFullYear() + ' ' + now.getHours() + ':' + now.getMinutes());

// Question 8. Suppose 1 dollar is equal to 82.23 Indian rupee, create a program which converts dollars to rupees.
let dollar = 5;
let rupee = 82.23 * dollar;
console.log(rupee);

// Question 9. Write a program to print unit digit of a given number.
n = 6693;
console.log(n%10)

// Question 10. Write a program to find the area of the circle. Take radius of circle from user as input and print the result in below given format. 
let r = 5;
 PI = Math.PI;
 A = PI * r * r;
 console.log(`
 Area of circle is ${A} having the radius ${r}
 `)