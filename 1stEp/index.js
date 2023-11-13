// getName()
// console.log(x)
// console.log("Before",getName);

// var x = 7

// function getName(params) {
//     console.log("Namaste JavaScript")
// }

// console.log("After",getName)


// var a =7
// console.log(a);

// var x;

// if (x === undefined) {
//     console.log(`Value of X is ${x} `);
// }


// function a (){
//     function c (){
//         console.log(b);
//     }
//     c()
// }

// var b = 10;
// a();

// Lexial env  means local memory of a variable + lexical memory of the parent of that variable
// Scope Chain :- The whole chain of lexical env is called scope chain


// console.log(b);
// // console.log(a);  // this will trow error as we use let

// let a = 10
// var b = 100

// console.log(a);
// // let and const are allocated memory in different memory space than global memory space.
// // var is allocated memory in global memory space
// {
//    block means  compound statement 
// in js we use block to group multiple statement
// }

// we group multiple statements inside a block so that we can use that block in a place where js expect a single statement
// {
// var a = 10;
// let b = 20;
// const c = 30;
// console.table(a,b,c)
// }

// console.table(a,b,c)


// Shadowing
// {
//     let a = 20;
//     {
//         let a = 10;
//         console.log(a);  // o/p = 10
//     }
//     console.log(a);     // o/p = 20
// }


// Illegal shadowing
// {
//     let a = 100;
//     {
//         var a = 20;
//         console.log(a);
//     }
//     console.log(a);
// }


// // Clousre

// function x (){
//     let a = 7 ;
//     function y() {
//         console.log(a);
//     }
//     a = 100;
//     return y;
//     // y()
// }

// const z = x()
// console.log(z);
// z();


// function x() {
//     var i = 1;

//     setTimeout( function (){
//         console.log(i);
//     }, 1000);

//     for( var i = 1 ; i <= 5 ; i++ ){
//         setTimeout(() => {
//             console.log(i);
//         }, i * 1000);
//     }

//     for ( let i = 1 ; i <= 5 ; i++ ){
//         setTimeout( function (){
//             console.log(i);
//         }, i * 1000)
//     }
//     for ( var i = 1 ; i<= 5 ; i++){
//         function close(x){
//             setTimeout ( function (){
//                 console.log(x);
//             }, x * 1000)
//         }
//         close(i);
//     }

//     console.log("Namaste JavaScript");
    
// }


// x();