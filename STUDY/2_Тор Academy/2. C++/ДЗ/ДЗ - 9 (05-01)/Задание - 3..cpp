#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    float salary, tariff = 50.0 / 100.0;
    int lateness, liness_count;
    // 1. Входные данные: желаемая зарплата Васи, количество опзданий; 
    //    Выходные данные: количество строчек кода.

    cout << "Введите желаемый доход Васи: ";
    cin >> salary;
    cout << "Введите количество опозданий Васи: ";
    cin >> lateness;
    liness_count = (salary + lateness / 3 * 20) / tariff;
    cout << "Чтобы получить " << salary << " $ при " << lateness
         << " опозданиях, Васе надо написать - " << liness_count
         << " строчек кода." << endl;


    // 2. Входные данные: кол.во строк кода, желаемый доход;
    //    Выходные данные:  - кол.во возможных опозданий.

    cout << "Введите количеств строк: ";
    cin >> liness_count;
    cout << "Введите желаемую зп: ";
    cin >> salary;
    lateness = (liness_count * tariff - salary) * 3 / 20 + 2;
    cout << "Вася может опоздать: " << lateness << " раз." << endl;


    // 3. Входные данные: кол.во строк кода, кол-во опозданий;
    //    Выходные данные : Зарплата.

    cout << "Введите количество строк кода: ";
    cin >> liness_count;
    cout << "Введите количество опозданий: ";
    cin >> lateness;
    salary = liness_count * tariff - lateness / 3 * 20;
    if (salary > 0) {
        cout << "Вася заработал - " << salary << endl;
    }
    else {
        cout << "Вася задолжал - " << salary * -1 << " $" << endl;
    }

}