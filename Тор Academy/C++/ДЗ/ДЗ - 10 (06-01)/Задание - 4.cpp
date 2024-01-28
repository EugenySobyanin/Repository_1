#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    int a;
    long long result = 1;
    while (true) {
        cout << "Введите число от 1 до 20: ";
        cin >> a;
        if (a >= 1 && a <= 20) {
            for (int i = a; i <= 20; i++) {
                result *= i;
            }
            cout << "Произведение = " << result << endl;
            break;
        }
        else {
            cout << "Введите корректное число." << endl;
        }
    }


    return 0;
}

