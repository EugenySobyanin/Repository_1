// Получаем нужный div
let div_3 = document.getElementById("task_3");


// Класс описывающий работника
class Employee
{
    constructor(
        name="Неизвестен", 
        age=0, 
        post="Без должности", 
        salary=0, 
        experience=0
    )
    {
        this.name = name;
        this.age = age;
        this.post = post;
        this.salary = salary;
        this.experience = experience;   
    }
}

// Создаем массив с работниками и добавляем туда 4 работника
let workers = [];
workers.push(new Employee("Александр Овечкин", 41, "Лучший снайпер НХЛ", 838470000, 20));
workers.push(new Employee("Мэттью Макконахи", 55, "Актер", experience=32));
workers.push(new Employee("Иван Иванов", 35, "Работник", 50000, 10));
workers.push(new Employee());


// Класс который получает массив работников, а возращает html код таблицы
class EmpTable
{
    constructor(workers = [])
    {
        this.workers = workers;
    }

    getHtml()
    {
        // Создаем таблицу
        let table = document.createElement("table");
        table.border = "1";

        // Создаем заголовок таблицы
        let headerRow = table.insertRow();
        for(let key in this.workers[0])
        {
            let headerCell = document.createElement("th");
            headerCell.textContent = key;
            headerRow.appendChild(headerCell);
        }

        // Добавляем строки с данными 
        for(let worker of this.workers)
        {
            let row = table.insertRow();
            for(let key in worker)
            {
                let cell = row.insertCell();
                cell.textContent = worker[key];
            }
        }
        return table;
    }
}


// Выводы
let table_obj = new EmpTable(workers);
div_3.appendChild(table_obj.getHtml());
