// Получаем элемент кнопки
let date_button = document.getElementById("get-date");

date_button.onclick = function(event){
    event.preventDefault();
    let div = document.getElementById("next-date-generator");
    let current_date = getElementById("date-input").value;
    let new_div = document.createElement("div");
    new_div.textContent = current_date;
    div.appendChild(new_div);

}
