﻿#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    int number, sum = 0;
    cout << "Введите целое число: ";
    cin >> number;
    for (int i  = number; i <= 500; i++) {
        sum += i;
    }
    cout << "Сумма: " << sum << endl;
}
