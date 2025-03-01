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

// Вывод самой викторины
start_button.onclick = function(event){
    event.preventDefault();
    
    for(let i = 0; i < questions.length; i++){
        let div = document.createElement("div")
        div.textContent = questions[i];

        let linebreak= document.createElement("br");
        div.appendChild(linebreak);

        for(let j = 0; j < answers[i].length; j++){
            let radio = document.createElement("input");
            radio.type = "radio";
            radio.id = `radio${i}_${j}`;
            radio.name = `question${i}`;

            let label = document.createElement("label");
            label.className = `label${i}`;
            label.htmlFor = radio.id;
            label.textContent = answers[i][j];

            div.appendChild(radio);
            div.appendChild(label);

            let linebreak2= document.createElement("br");
            div.appendChild(linebreak2);
        }
        quiz.appendChild(div);
    }
    quiz.appendChild(result_button);
}

// Подсчет баллов
result_button.onclick = function(event){
    event.preventDefault();
    points = 0;

    for(let i = 0; i < questions.length; i++){
        let selected = document.querySelector(`input[name="question${i}"]:checked`);
        
        if (selected){
            let select_label = document.querySelector(`label[for="${selected.id}"]`)
            if (select_label && (select_label.textContent == "Том Хэнкс" || select_label.textContent == "Мэтью Макконахи")) {
                points += 2;
            }
        }
    }
    let h2 = document.createElement("h2");
    h2.textContent = `Вы набрали ${points} баллов`;
    quiz.appendChild(h2);
}
