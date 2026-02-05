#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    int num1, num2, c;
    cout << "Введите первое целое число: ";
    cin >> num1;
    cout << "Введите второе целое число: ";
    cin >> num2;
    cout << "Числа на которые делятся num1 и num2 одновременно: " << endl;
    if (num1 > num2) {
        c = num2;
        num2 = num1;
        num1 = c;
    }
    for (int i = 1; i <= num2; i++) {
        if (num1 % i == 0 && num2 % i == 0) {
            cout << i << endl;
        }
    }
}
