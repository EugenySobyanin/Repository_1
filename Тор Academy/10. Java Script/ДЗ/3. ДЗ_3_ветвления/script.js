// Задание 1.
// let old = prompt("Введите ваш возраст");
// let result = ""
// if (old < 12) { 
//     result = "Вы ребенок.";
// }
// else if (old > 11 && old < 18){
//     result = "Вы подросток.";
// }
// else if (old > 17 && old < 61){
//     result = "Вы взрослый.";
// }
// else {
//     result = "Вы пенсия.";
// }
// alert(result);


// Задание 2.
// let symbol = prompt("Введите число от 0 до 9.");

// switch(symbol){
//     case("0"):
//         alert(")");
//         break;
//     case("1"):
//         alert("!");
//         break;
//     case("2"):
//         alert("@");
//         break;
//     case("3"):
//         alert("№");
//         break;
//     case("4"):
//         alert("$");
//         break;
//     case("5"):
//         alert("%");
//         break;
//     case("6"):
//         alert(":");
//         break;
//     case("7"):
//         alert("?");
//         break;
//     case("8"):
//         alert("*");
//         break;
//     case("9"):
//         alert("(");
//         break;
//     default:
//         alert("Некоректный ввод.");
// }


// Задание 3.
// let num = prompt("Введите трехзначное число: ");
// if (num[0] == num[1]) {
//     alert("Первое и второе число одинаковые.");
// }
// else if (num[1] == num[2]) {
//     alert("Второе и третье число одинакоые.");
// }
// else if (num[0] == num[2]) {
//     alert("Первое и третье число одинаковые.");
// }
// else {
//     alert("Одинаковых чисел нет.");
// }


// Задание 4.
// let year = prompt("Введите год");
// let result = "Год - ";
// result += (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0) ? "високосный": "не високосный");
// alert(result);


// Задание 5.
// let num = prompt("Введите пятиразрядное число");
// let result = "Число - ";
// result += (num[0] == num[4] && num[1] == num[3] ? "" : "не ");
// alert(result + "палиндром.");


// Задание 6.
let amount = document.getElementById("amount");
// let result = document.getElementById("result");
let button = document.getElementById("submit");

button.onclick = function(event){
    
}


// Задание 7.
// let sum = prompt("Введите сумму покупки");
// let sale = 0;
// if (sum >= 200 && sum < 300) {
//     sale = 3;
// }
// else if (sum >= 300 && sum < 500) {
//     sale = 5;
// }
// else if (sum >= 500) {
//     sale = 7;
// }
// alert(`Сумма к оплате: ${(sum * (1 - sale / 100 )).toFixed(2)}`);


// Задание 8.
// let l = prompt("Введите длину окружности");
// let p = prompt("Введите периметр квадрата");
// let result_2 = p / 4 > l / Math.PI ? "Помещается!": "Не помещается(";
// alert(result_2);


// Задание 9.


