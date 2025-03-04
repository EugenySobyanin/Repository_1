// Получаем нужный div
let div_2 = document.getElementById("task_2");


class ExtendedDate extends Date
{
    getFormatedDate()
    {
        const months = [
            "январь", "февраль", "март", "апрель",
            "май", "июнь", "июль", "август",
            "сентябрь", "октябрь", "ноябрь", "декабрь",
        ]

        const month = months[this.getMonth()];
        return `${this.getDate()} - ${month}`;
    
    }

    isFutureOrCurrentDate()
    {
        let current_date = new Date();
        // Обнуляем время у обеих дат для корректного сравнения
        this.setHours(0, 0, 0, 0);
        current_date.setHours(0, 0, 0, 0);
        return this >= current_date;
    }

    // Метод возвращает високосный год или нет
    isLeapYear()
    {
        let year = this.getFullYear();
        return year % 400 == 0 || year % 4 == 0 && year % 100 != 0;
    }

    // Возращает следующую дату
    getNextDate()
    {   
        // копируем дату
        let next_date = new ExtendedDate(this);
        next_date.setDate(this.getDate() + 1);
        return "Следующая дата: " + next_date.getFormatedDate() + "<br>";
    }
}


// Выводы
let date_obj = new ExtendedDate("2008-02-29");

// Метод вывода даты
div_2.innerHTML += date_obj.getFormatedDate() + "<br>";

// Метод проверки дата из прошлого или из будущего
if(date_obj.isFutureOrCurrentDate())
{
    div_2.innerHTML += "Дата текущая или из будущего.<br>";
}
else
{   
    div_2.innerHTML += "Дата из прошлого.<br>";
}

// Метод проверки високосный год или нет
if(date_obj.isLeapYear())
{
    div_2.innerHTML += "Год високосный!<br>";
}
else
{
    div_2.innerHTML += "Год не високосный.<br>";
}

// Метод получения следующей даты
div_2.innerHTML += date_obj.getNextDate();
