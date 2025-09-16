// Переменные и константы, типы данных


var username = "sobyanin";
let age = 45;
const country = "Russia";

console.log(username, age, country)

// Определение переменных в одну строку
var name_1 = "Bob", name_2 = "Tailer", name_3 = "Connor";
console.log(name_1, name_2, '\n', name_3);


// Интерполяция (встраивание данных в строку)
str = `Меня зовут ${username}, мне ${age - 19}, я живу в ${country}.`;
console.log(str);

// Многострочный текст при помощи косых кавычек
str = `Алькарас
Синнер
Джокович
Зверев
Дрейпер
Фриц
Медведев`;
console.log(str);

// undefined - тип данных, который указывает, что значение не определено или не установлено
var a;
console.log(a);

// null - означает, что у переменной отсутствует значение
var a = null;
console.log(a);

// тип object - простейшее определение
var obj_1 = {first_name: "Orlando", profession: "Копатель"};
console.log(`${obj_1} - ${obj_1.first_name} - вот так вот.`);

// typeof - оператор для получения типа объекта
console.log(typeof str);
console.log(typeof a);
console.log(typeof age);
