// Получаем нужный div
let div_4 = document.getElementById("task_4");


// Класс унаследованный от EmpTable из 3 задания
class StyledEmpTable extends EmpTable
{
    getStyles()
    {
        return `
            <style>
                table {
                    width: 80%;
                    border-collapse: collapse;
                    font-family: Arial, sans-serif;
                }
                
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                
                th {
                    background-color: #f2f2f2;
                    color: #333;
                }

                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }

                tr:hover {
                    background-color: #ddd;
                }
            </style>
        `;
    }
    
    // Переопределяем метод родительского класса
    getHtml()
    {
        let table = super.getHtml(); // Получаем таблицу из родительского класса
        let styles = this.getStyles(); // Получаем стили

        // Создаем контейнер для таблицы и стилей
        let container = document.createElement("div");
        container.innerHTML = styles;
        container.appendChild(table);

        return container;
    }
}


// Выводы
// Используются данные из задания 3
let styled_table_obj = new StyledEmpTable(workers);
div_4.appendChild(styled_table_obj.getHtml());