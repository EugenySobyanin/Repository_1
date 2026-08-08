#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    int product, // для ввода кода пиццы
        drink,   // для ввода кода напитка
        count_pizza, // кол-во пицц
        count_drink, // кол-во порций напитков
        button, // 
        for_check_pizza = 0, // для определения какие пиццы попали в заказ и вывод их в чек
        for_check_drink = 0; // для определения какие напитки попали в заказ и вывод их в чек
    int position_count_pizza[4],
        position_count_drink[3]; // для хранение кол-во пицц и порций напитка по каждой позиции, для вывода в чек
    double position_sum = 0, // сумма в заказе по каждой позиции
           total_order = 0;  // сумма всего заказа
    double pizza_prices[4] = { 7.55, 9.60, 8.90, 7.99 },
           drink_prices[3] = { 2.65, 2.25, 1.95 },
           position_sum_pizza[4] = {0, 0, 0, 0}, // сумма в заказе по каждой возможной позиции пиццы
           position_sum_drink[3] = {0, 0, 0}; // сумма в заказе по каждой возможной позиции напитка
    cout << "Домашнее задание 7.1\n" << endl;
    cout << "\tМеню" << endl
        << "Пицца: " << endl
        << "\tМаргарита - " << pizza_prices[0] << "$ - Код - 1" << endl
        << "\tПепперони - " << pizza_prices[1] << " $ - Код - 2" << endl
        << "\tГавайская - " << pizza_prices[2] << " $ - Код - 3" << endl
        << "\tБарбекю   - " << pizza_prices[3] << "$ - Код - 4" << endl
        << "Напитки: " << endl
        << "\tКофе\t  - " << drink_prices[0] << "$ - Код - 1" << endl
        << "\tЧай\t  - " << drink_prices[1] << "$ - Код - 2" << endl
        << "\tКока-кола - " << drink_prices[2] << "$ - Код - 3" << endl << endl;
    while (true)
    {
        cout << "Если хотите заказать пиццу - введите 1" << endl
            << "Если хотите заказать напиток - введите 2" << endl;
        cin >> button;
        if (button == 1) {
            cout << "Введите код пиццы: ";
            cin >> product;
            cout << "Введите количество пицц: ";
            cin >> count_pizza;
            switch (product)
            {
            case(1):
                for_check_pizza += 5;                           // В переменную 'for_check_pizza' в зависимости от выбранной пиццы
                position_sum_pizza[0] = 7.55 * count_pizza;     // добавляется число с разным количеством разрядов, с помощью этого мы 
                total_order += position_sum_pizza[0];           // в итоговом выводе чека можем опеделить - заказывали определенную пиццу или нет
                position_count_pizza[0] = count_pizza;
                break;
            case(2):
                for_check_pizza += 60;
                position_sum_pizza[1] = 9.60 * count_pizza;
                total_order += position_sum_pizza[1];
                position_count_pizza[1] = count_pizza;
                break;
            case(3):
                for_check_pizza += 700;
                position_sum_pizza[2] = 8.90 * count_pizza;
                total_order += position_sum_pizza[2];
                position_count_pizza[2] = count_pizza;
                break;
            case(4):
                for_check_pizza += 8000;
                position_sum_pizza[3] = 7.99 * count_pizza;
                total_order += position_sum_pizza[3];
                position_count_pizza[3] = count_pizza;
                break;
            default:
                cout << "Продукта с таким кодом в пиццерии нет(";
                break;
            }
        }
        else if (button == 2) {
            cout << "Введите код напитка: ";
            cin >> drink;
            cout << "Введите количество порций напитка: ";
            cin >> count_drink;
            switch (drink)
            {
            case(1):
                for_check_drink += 60;                      // Аналогично переменной 'for_check_pizza'
                position_sum_drink[0] = 2.65 * count_drink;
                total_order += position_sum_drink[0];
                position_count_drink[0] = count_pizza;
                break;
            case(2):
                for_check_drink += 700;
                position_sum_drink[1] = 2.25 * count_drink;
                total_order += position_sum_drink[1];
                position_count_drink[1] = count_pizza;
                break;
            case(3):
                for_check_drink += 8000;
                position_sum_drink[2] = 1.95 * count_drink;
                total_order += position_sum_drink[2];
                position_count_drink[2] = count_pizza;
                break;
            default:
                cout << "Продукта с таким кодом в пиццерии нет(";
                break;
            }
        }
        else {
            cout << "Ошибка! Вводите 1 или 2";
        }
        cout << endl << "Хотите продолжить заказ?" << endl
            << "Если да - введите 1   "
            << "Если нет - введите 0" << endl;
        cin >> button;
        if (button == 0) {
            cout << "\t\tЧек" << endl;
            if (for_check_pizza % 10 == 5) {
                cout << "Пицца Маргарита - " << position_count_pizza[0] << " шт. - " << position_sum_pizza[0] << "$" << endl;
            }
            if (for_check_pizza / 10 % 10 == 6) {
                cout << "Пицца Пепперони - " << position_count_pizza[1] << " шт. - " << position_sum_pizza[1] << "$" << endl;
            }
            if (for_check_pizza / 100 % 10 == 7) {
                cout << "Пицца Гавайская - " << position_count_pizza[2] << " шт. - " << position_sum_pizza[2] << "$" << endl;
            }
            if (for_check_pizza % 10000 / 1000 == 8) {
                cout << "Пицца Барбекю - " << position_count_pizza[3] << " шт. - " << position_sum_pizza[3] << "$" << endl;
            }
            if (for_check_drink / 10 % 10 == 6) {
                cout << "Кофе - " << position_count_drink[0] << " шт. - " << position_sum_drink[0] << "$" << endl;
            }
            if (for_check_drink / 100 % 10 == 7) {
                cout << "Чай - " << position_count_drink[1] << " шт. - " << position_sum_drink[1] << "$" << endl;
            }
            if (for_check_drink / 1000 == 8) {
                cout << "Кока-кола - " << position_count_drink[2] << " шт. - " << position_sum_drink[2] << "$" << endl;
            }
            cout << "Сумма вашего заказа: " << total_order << "$" << endl;
            break;
        }

    }


    return 0;
}