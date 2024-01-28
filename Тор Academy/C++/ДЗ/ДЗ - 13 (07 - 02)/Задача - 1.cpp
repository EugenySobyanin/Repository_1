#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    long num, num2;
    int sum = 0, i = 0, zero_count = 0;
    cout << "Введите число: ";
    cin >> num;
    num2 = num;
    while (num2 > 0) {
        int a = num2 % 10;
        num2 /= 10;
        sum += a;
        ++i;
        if (a == 0) {
            ++zero_count;
        }
    }
    cout << "Цифр в числе: " << i << endl;
    cout << "Сумма цифр: " << sum << endl;
    cout << "Среднее арифметическое: " << float(sum) / float(i) << endl;
    cout << "Количество нулей: " << zero_count << endl;


    return 0;
}