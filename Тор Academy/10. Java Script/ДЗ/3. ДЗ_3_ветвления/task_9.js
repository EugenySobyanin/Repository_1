// Вопросы
let questions = [
    "Кто исполнил главную мужскую роль в фильме Форест Гамп?",
    "Кто является лауреатом премии оскар в 2014 году?",
    "Кто является звездой сериала \"Настоящий детектив\"?",
]

// Варианты ответов
let answers = {
    0 : ["Кевин Спейси", "Рассел Кроу", "Том Хэнкс"],
    1 : ["Мэтью Макконахи", "Брэдли Купер", "Леонардо ДиКаприо"],
    2 : ["Бред Пит", "Зак Эфрон", "Мэтью Макконахи"],
}

let points = 0;
let quiz = document.getElementById("quiz");
let start_button = document.getElementById("start-button");
var result_button = document.createElement("button");
result_button.textContent = "Отправить";

start_button.onclick = function(event){
    event.preventDefault();
    
    for(let i = 0; i < questions.length; i++){
        let div = document.createElement("div")
        div.textContent = questions[i];

        let linebreak= document.createElement("br");
        div.appendChild(linebreak);

        for(let j = 0; j < answers[i].length; j++){
            let checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.id = `checkbox${i}_${j}`;
            checkbox.class = `checkbox${i}`;

            let label = document.createElement("label");
            label.class = `label${i}`;
            label.htmlFor = checkbox.id;
            label.textContent = answers[i][j];

            div.appendChild(checkbox);
            div.appendChild(label);

            let linebreak2= document.createElement("br");
            div.appendChild(linebreak2);
        }
        quiz.appendChild(div);
    }
    quiz.appendChild(result_button);
}

result_button.onclick = function(event){
    event.preventDefault();

    for(let i = 0; i < questions.length; i++){
        let check_answers = document.getElementsByClassName(`checkbox${i}`);
        let labels= document.getElementsByClassName(`label${i}`);
        for(let j = 0; j < answers[i].length; j++){
            if (check_answers[i].checked && (labels[i].textContent == "Том Хэнкс" || labels[i].textContent == "Мэтью Макконахи")){
                points += 2;
            }
        }
    }
    let h2 = document.createElement("h2");
    h2.textContent = `Вы набрали ${points} баллов`;
    quiz.appendChild(h2);
}
