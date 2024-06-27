#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    int people, code, count;
    const int count_drink_el = 5, count_cake_el = 4;
    string drinks[count_drink_el] = { "Кофе", "Чай", "Молочный коктейль",
                                      "Кола", "Смузи" },
        cakes[count_cake_el] = { "Наполеон", "Медовик", "Чизкейк", "Сникерс" };
    float drinks_prices[count_drink_el] = { 240, 150, 330, 180, 210 },
          cakes_prices[count_cake_el] = { 360, 290, 400, 330 };
    float total_order = 0;
    cout << "Введите количество человек: ";
    cin >> people;

    for (int i = 0; i < people; i++) {
        // Цикла проходит по всем людям которые делают заказ.
        cout << "Ознакомьтесь с меню." << endl;
        for (int j = 0; j < count_cake_el; j++) {
            // Цикл для вывода тортиков (2ая часть меню)
            if (j == 0) {
                for (int k = 0; k < count_drink_el; k++) {
                    // Цикл для вывода напитков (1ая часть меню)
                    cout << drinks[k] << " - " << drinks_prices[k]
                        << "руб. | Код - " << k + 1 << endl;
                }
            }
            cout << cakes[j] << " - " << cakes_prices[j] << "руб. | Код - "
                << j + count_drink_el + 1 << endl;
        }


        while (true) {
            cout << "Введите код продукта - ";
            cin >> code;
            if (code == 0) {
                break;
            }
            cout << "Введите количество - ";
            cin >> count;
            cout << "Что бы завершить заказ - нажмите 0" << endl;
            if (code <= count_drink_el && code > 0) {
                total_order += drinks_prices[code - 1] * count;
            }
            else if (code > count_drink_el
                && code <= count_drink_el + count_cake_el) {
                total_order += cakes_prices[code - (count_drink_el + 1)] * count;
            }
            else {
                cout << "Некорректный код продукта." << endl;
            }


        }
        cout << endl;
    }
    cout << "Сумма вашего заказа: " << total_order << endl;

    return 0;
}