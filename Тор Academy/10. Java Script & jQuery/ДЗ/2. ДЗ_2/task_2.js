// Получаем элемент div для вывода данных
let main_div = document.getElementById("task_1");


// Класс описывающий маркер
class Marker
{
    color = "blue";
    amount = 100; // Кол.во чернил в %

    print(str)
    {
        str = this.get_str_and_calc_amount(str);
        let new_div = document.createElement("div");
        new_div.textContent = str;
        new_div.style.color = this.color;
        main_div.appendChild(new_div);   
    }

    // Считает сколько осталось чернил и готовит стоку для вывода
    // (если чернил мало - строка выведется не полностью)
    get_str_and_calc_amount(str)
    {
        let result = "";
        for(char of str)
        {
            if(this.amount < 0.5) return result;
            result += char;
            if(char != " ") this.amount -= 0.5;
        }
        return result;
    }
}


let marker_obj = new Marker;
marker.print("Человек паук рулит!");
console.log(marker.amount);
marker.color = "black";
marker.print("История Кенни Уэллса — современного золотоискателя, хваткого дельца и мечтателя,"
            + " который отчаянно ждёт шанса переломить судьбу. Оставшись без особых вариантов,"
            + "Уэллс находит себе такого же неудачливого напарника — геолога, чтобы реализовать"
            + "грандиозный план: найти золото в неизведанных индонезийских джунглях.");
console.log(marker.amount);
