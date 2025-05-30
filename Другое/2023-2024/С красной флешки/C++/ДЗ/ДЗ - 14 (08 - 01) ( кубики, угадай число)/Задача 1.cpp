﻿#include <iostream>
#include <chrono>
#include <thread>


int main()
{
    using namespace std;
    using namespace std::this_thread;
    using namespace std::chrono;
    setlocale(LC_ALL, "RU");
    char chr;
    int choice_1, choice_2;
    cout << "Введите символ для вывода линии: ";
    cin >> chr;
    cout << "Вертикальная линия - 1" << endl
         << "Горизонтальная линия - 2" << endl;
    cin >> choice_1;
    cout << "Выберите скорость вывода линии." << endl
        << "Быстро - 1" << endl
        << "Нормально - 2" << endl
        << "Медленно - 3" << endl;
    cin >> choice_2;
    
    for (int i = 0; i < 100; i++) {
        cout << chr;
        if (choice_1 == 1) {
            cout << endl;
        }
        if (choice_2 == 3) {
            sleep_for(nanoseconds(200000000));
        }
        else if (choice_2 == 2) {
            sleep_for(nanoseconds(8500));
        }
        else {
            sleep_for(nanoseconds(2000));
        }
    }

    return 0;
}