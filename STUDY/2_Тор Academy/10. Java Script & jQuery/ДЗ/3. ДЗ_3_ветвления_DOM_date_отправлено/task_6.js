// Задание 6.
// Храним курс валют в объекте
let course = {
    "EUR": 0.96,
    "AZN": 1.7,
    "RUB": 98.01,
}
let convertor = document.getElementById("convertor");
let amount = document.getElementById("amount");
// Валюта
let currency = document.getElementById("currency");
let button = document.getElementById("submit");

button.onclick = function(event){
    // Предотвращаем стандартное поведение кнопки
    event.preventDefault();

    // Пробуем получить предыдущий результат
    let last_result = document.getElementById("result-div");
    if (last_result){
        convertor.removeChild(last_result);
    }

    // Создали новый элемент
    let result_div = document.createElement("div");
    // Задаем айдишник
    result_div.id = "result-div";

    // Вариант 1
    // Создали текстовый узел
    // let result_text = document.createTextNode(
    //     `${amount.value}$ - ${amount.value * course[`${currency.value}`]} ${currency.value}`
    // );
    // // Добавили текстовый узел к элементу
    // result_div.appendChild(result_text);

    // Вариант 2 (тектовый узел создается под капотом)
    result_div.textContent = (
        `${amount.value}$ - ${(amount.value * course[`${currency.value}`]).toFixed(2)} ${currency.value}`
    );
    // Добавили элемент в конец div c id="convertor"
    convertor.appendChild(result_div);

    // Сбрасываем форму
    amount.value = ""; // Сбрасываем поле ввода суммы
    currency.value = ""; // Сбрасываем выбор валюты (по умолчанию)
}