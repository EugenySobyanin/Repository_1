// Преобразования типов


const_1 = "50";
const_2 = 5;
console.log(const_1 + const_2);

// parseInt - преобразование к целому числу
console.log(parseInt(const_1 + "Hello!") + const_2);

// c методом стоит быть аккуратным для дробных чисел, т.к. они преобразуются сначала в строку, а потом в int
// так же надо быть аккуратным с большими целыми числами
// вот пример:
var a = 0.000005;
console.log(parseInt(a));

var b = 0.0000005;  // В строковом виде представлен как 5e-7
console.log(String(b));
console.log(parseInt(b));

