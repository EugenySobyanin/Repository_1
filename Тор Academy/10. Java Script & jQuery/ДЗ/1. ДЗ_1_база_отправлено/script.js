// Задание 1.
var input_name = prompt("Введите ваше имя: ");
alert(`Привет, ${input_name}`);

// Задание 2.
const CURRENT_YEAR = 2025;
var input_old = prompt("Укажите ваш год рождения:");
alert(`Ваш возраст: ${CURRENT_YEAR - input_old}.`);

// Задание 3.
var input_side = prompt("Укажите сторону квадрата: ");
alert(`Периметр квадрата: ${input_side * 4}\n
Площадь квадрата: ${input_side ** 2}.`);

// Задание 7.
const FILE_SIZE_MB = 820;
var input_size = prompt("Укажите размер флешки в ГБ: ");
alert(`На флешку поместится: ${parseInt(input_size * 1000 / FILE_SIZE_MB)} файлов.`);

// Задание 8.
var input_money = Number(prompt("Сколько у Вас денег?"));
var input_coast = Number(prompt("Сколько стоит одна шоколадка?"));
alert(`Вы можете купить ${parseInt(input_money / input_coast)} шоколадок 
и у Вас останется ${input_money % input_coast} рублей.`);

// Задание 9.
var input_num = prompt("Введите трехзначное число: ");
var result_str = "";
for(var i = input_num.length - 1; i >= 0; i--){
    result_str += input_num[i];
}
alert(result_str);

// Задание 10.
var input_num = Number(prompt("Введите число: "));
if (input_num % 2 == 0){
    alert("Число четное.");
}
else{
    alert("Число нечетное.");
}
