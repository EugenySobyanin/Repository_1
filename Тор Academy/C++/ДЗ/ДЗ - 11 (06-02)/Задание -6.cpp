#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    int num;
    cout << "Введите целое число: ";
    cin >> num;
    for (int i = 1; i <= num; i++) {
        if (num % i == 0) {
            cout << i << endl;
        }
    }
}

