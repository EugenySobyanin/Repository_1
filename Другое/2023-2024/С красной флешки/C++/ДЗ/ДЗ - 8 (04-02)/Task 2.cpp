﻿#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    cout << "Домашнее задание 8.2\n" << endl;
    double sales, people1, people2, people3, salary, people = 0;
    cout << "Введите сумму продаж для 3-ех сотрудников." << endl;
    for (int i = 0; i < 3; ++i) {
        cout << "Сумма: ";
        cin >> sales;
        if (sales < 500 && sales > 0) {
            salary = 200 + sales * 1.03;
        }
        else if (sales <= 1000) {
            salary = 200 + sales * 1.05;
        }
        else if (sales > 1000) {
            salary = 200 + sales * 1.08;
        }
        else {
            cout << "Некорректный ввод";
        }
        for (int j = 0; j < 3; ++j) {
            switch (i)
            {
            case 0:
                people1 = salary;
                break;
            case 1:
                people2 = salary;
                break;
            case 2:
                people3 = salary;
                break;
            default:
                cout << "Ошибка!";
                break;
            }
        }
    }                                                                            
    if (people2 < people1) {
        people = people1;
        people1 = people2;
        people2 = people;
        if (people3 < people2 && people3 > people1) {
            people = people2;
            people2 = people3;
            people3 = people;
        }
        else if (people3 < people2 && people3 < people1) {
            people = people1;
            people1 = people3;
            people3 = people2;
            people2 = people;
        }
    }
    else if(people2 > people1) {
        if (people3 < people2 && people3 > people1) {
            people = people2;
            people2 = people3;
            people3 = people;
        }
        else if (people3 < people2 && people3 < people1) {
            people = people1;
            people1 = people3;
            people3 = people2;
            people2 = people;
        }
    }
    cout << endl
         << "3 место - " << people1 << " $" << endl
         << "2 место - " << people2 << " $" << endl
         << "1 место - " << people3 << " $" << ". Плюс премия за 1ое место. Итого:  "
         << people3 + 200 << " $" << endl;
}