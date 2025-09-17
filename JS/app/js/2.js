// Условные выражения и условные операции ?: и ??


console.log(15 == "15");  // true
console.log(15 === "15");  // false

var obj_1 = "";
var ojb_2 = 0;

if(!(obj_1 && ojb_2)){
    console.log("Все работает как часы.")
}

// Тернарный оператор ?:
// [условие] ? [если true] : [если false]
var obj_3 = null;
var res = !obj_3 ? 'ТРУ' : 'НЕ ТРУ';
console.log(res);

// ?? позоволяет проверить значение на null и undefined
var res = obj_3 ?? "ГОЛОВА";
console.log(res);
console.log("" ?? "Голова");

// Модифицированный вариант оператора ??
obj_3 ??= 222;
console.log(obj_3);

