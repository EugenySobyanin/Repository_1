// Получаем элемент кнопки
let date_button = document.getElementById("get-date");

date_button.onclick = function(event){
    event.preventDefault();

    // Получаем главный div
    let div = document.getElementById("next-date-generator");

    // Получаем дату в формате строки
    let current_date = document.getElementById("date-input").value;

    // Преобразуем в объект даты
    let date = new Date(current_date);

    // Увеличиваем дату на 1 день
    date.setDate(date.getDate() + 1);

    let new_div = document.createElement("div");
    new_div.textContent = formatDate(date);
    div.appendChild(new_div);

}

// Функция для форматирования даты
function formatDate(date) {
    let year = date.getFullYear();
    
    // padStart - добавляет символы в начало строки если ее длина меньше указанной
    let month = String(date.getMonth() + 1).padStart(2, '0'); // Месяцы начинаются с 0
    let day = String(date.getDate()).padStart(2, '0');

    return `${day}-${month}-${year}`;
}
