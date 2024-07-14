#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    setlocale(LC_ALL, "RU");
    int x, y, result;
    cout << "Введите первое число: ";
    cin >> x;
    cout << "Введите второе число: ";
    cin >> y;
    result = x;
    for (int i = 1; i < abs(y); i++) {
        result *= x;
    }
    if (y == 0) {
        cout << "Результат: " << 1 << endl;
    }
    else if (y < 0) {
        cout << "Результат: " << 1 / float(result) << endl;
    }
    else {
        cout << "Результат: " << result << endl;
    }
    cout << "Проверка через функцию: " << pow(x, y) << endl;
}
