#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    long num;
    cout << "Введите целое число: ";
    cin >> num;
    int result = 0;
    for (int i = 1; i < num; i++) {
        long a = pow(i, 2);
        long b = pow(i, 3);
        if (num % a == 0 && num % b != 0) {
            ++result;
            cout << i << endl;
        }
    }
    cout << "Всего чисел: " << result << endl;

}

