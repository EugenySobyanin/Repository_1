
#include <iostream>
#include <locale.h>
#include <cmath>
#include <stdlib.h>
#include <ctime>
using namespace std;


int main()

{
    setlocale(LC_ALL, "RU");
    /*int a = 0;
    int b = 15;
    system("color 00");*/

    //задача 1
    /*int hours, minute;
    cout << "Введите час:";
    cin >> hours;
    cout << "Введите минуты:";
    cin >> minute;
    int generalPastTime = hours * 3600 + minute * 60;
    int remainder = 24 * 3600 - generalPastTime;

    cout << hours << "h: " << minute << "m\n";

    cout << remainder / 3600 << "h:" <<
        ((remainder / 60)) % 60 << "m:" <<
        remainder % 60 << "s: ";*/




        //Задача 2
        //пользователь вводит диаметр, надо посчитать площадь в квадрате
    /*float d;
    cout << "Введите диаметр:";
    cin >> d;
    float p = 3.14;
    float area = p * pow((d / 2), 2);
    float perimeter = 2 * p * (d / 2);

    cout << "Площадь: " << area << "\n";
    cout << "Периметр: " << perimeter;*/


    //Задача 3
    /*int year;
    cin >> year;
    int remaind = year % 4;

    cout << "В году " << 365 + !bool(remaind) << "дней";*/

    //Задача 4
    /*int rub, penny;
    cout << "Введите рубли: ";
    cin >> rub;
    cout << "Введите копейки: ";
    cin >> penny;
    int remind = penny % 100;
    cout << "Рублей: " << rub + ((penny - remind) / 100)<< " " << "Копеек: " << remind;*/


    //Задача 5
    /*double a, b, c;
    cout << "Введите длину, ширину, высоту\n";
    cin >> a >> b >> c;
    cout << "Объем фигуры: " << a * b * c;*/

    //Задача 6
    /*cout << "Введите диаметр: \n";
    double d;
    cin >> d;
    double r = d / 2;
    double p = 3.14;
    cout << "Объем шара: " << (4./3. ) * p * pow(r, 3) << "см\n";*/


    //Задача 7 
    //Дано: стоимость одного ноутбука, количество ноутбуков, процент скидки
    // Найти: общую сумму заказа
    /*int quantity;
    double coast, sale;
    cout << "Введите стоимость ноутбука: \n";
    cin >> coast;
    cout << "Введите количество ноутбуков: \n";
    cin >> quantity;
    cout << "Введите величину скидки: \n";
    cin >> sale;
    cout << "Общая сумма заказа: " << quantity * coast * (sale / 100);*/



    //Задача 8
    /*int num1, num2;
    cin >> num1, num2;
    char operation;
    cin >> operation;

    switch (operation) {
        case '+':
            cout << "num1 + num2 = " << num1 + num2;
            break;
        case '-':
            cout << "num1 - num2 = " << num1 - num2;
            break;
        case '%':
            cout << "num1 % num2 = " 
                 << int(num1) - int(num2);//остаток от деления можно применять только к целым числам
            break;
        default:
            cout << "Что-то введено некоректно";
    }*/
    

    //Задача 9
    /*float num;
    cin >> num;
    cout << "Итоговая зарпалата за месяц: " << num * 0.05 + 100;*/

    //Задача 10
    /*long long size, speed;
    cout << "Введите размер файла в гигабайтах: ";
    cin >> size;
    cout << "Введите скорость интернет соединения в битах в секунду: ";
    cin >> speed;
    size *= 8589934592; //Переводим гигобайты
    cout << speed;
    double result = size / speed;
    cout << result << "\n";*/



    /*cout << "Часы: " << int(result / 3600) << "\n";
    cout << "Минуты: " << int(result / 60) % 60 << "\n";
    cout << "Секунды: " << int(result) % 60;*/

    // Задача 11
    /*int num;
    cout << "Введите число: ";
    cin >> num;
    if (num % 2 == 0) {
        cout << "Число четное";
    }
    else {
        cout << "Число нечетное";

    }*/

    //Задача 11
    /*int a, b;
    cout << "Введите два числа: ";
    cin >> a >> b;
    (a > b) ? cout << b : cout << a; //Тернарный оператор*/

    //Задача 12
    /*int a;
    cout << "Введите число: ";
    cin >> a;
    if (a == 0) {
        cout << "Число равно нулю";
    }
    else if (a > 0) {
        cout << "Число больше нуля";
    }
    
    else {
        cout << "Число меньше нуля";
    }*/

    //Задача 13
    /*int a, b;
    cout << "Введите два числа: ";
    cin >> a >> b;
    (a != b) ? cout << min(a, b) <<" " << max(a, b) : cout 
                    << "Числа ровны";*/ //Тернарный оператор

    //Задача 14
    /*int a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;
    cout << sum(a, b, c, d, e);*/

    //Задача 15
    /*double a, b;
    char c;
    cin >> a >> b >> c;
    switch (c){
        case '+':
            cout << a + b;
            break;
        case '-':
            cout << a - b;
            break;
        case '*':
            cout << a * b;
            break;
        case '/':
            cout << a / b;
            break;
        default:
            cout << "Такая операция не поддерживается";
            break;
    }*/


    /*int num;
    cout << "Введите число: ";
    cin >> num;
    int i;
    for (i = 0; i < 7; i++) {
        cout << pow(num, i) << endl;
    }*/


    ////////       Цикл while     ////////

    /*int a = 1;
    while (a <= 10) {
        cout << a << " ";
        ++a;

    }
    cout << endl;

    int b = 11;
    do {
        cout << b++ << " ";
    } while (b <= 10);

    int c = 1;
    for (; c <= 10; c++) {
        cout << "Opa" << endl;
    }*/
        
    /// задача 1 ///
    /*int a, b;
    cin >> a >> b;
    if (a < b) {
        for (a; a <= b; a++) {
            if (a % 2 == 0){
                cout << a << endl;
            }
            
        }
    }
    else {
        for (b; b <= a; b++) {
            if (a % 2 == 0) {
                cout << b << endl;
            }
        }
    }*/

    /// Задача 2 ///
    /*int a, b, c = 0;
    cin >> a >> b;
    while (a < b) {
        c += a;
        
        a++;
    }
    cout << c << endl;*/

    /// Задача 3 ///
    

    /*int a, b = 0;
    cin >> a;
    while (a != 0) {
        b += a;
        cin >> a;
        
    }
    cout << b;*/
    /*srand(time(0));                                                            //рандомное число!!!!!
    int a = rand() % 2+1;
    int b = 0;
    bool d = true;
    cout << "Добро пожаловать в игру! 
             Угадай число от 0 до 500 " << endl;
    long long t1 = time(0);
    while (d) {
        cout << "Введите число:  ";
        int c;
        cin >> c;
        b += 1;
        if (c < a) {
            cout << "Ваше число меньше" << endl;
        }
        else if (c > a) {
            cout << "Ваше число больше" << endl;
        }
        else if (c == a) {
            cout << "Вы победили!" << "Вам понадобилось" 
                 << " "<<  b <<" " << "попыток" << endl;
            

            d = false;
        }
        else if (c == 0) {
            d = false;
        }
        
        
    }
    
    long long t2 = time(0);
    long long t = t2 - t1;
    cout << "Вам потребовалось: " << t << " секунд";
    */

//for (int i = 0; i < 10; i++) {
//    if (i == 5) {
//        continue;
//    }
//    cout << i + 1 << endl;
//}
    

    //srand(time(0));                                   //Генерация рандомного числа
    //int a = rand() % 5 + 1;
    //cout << a;

    

    //Задача 1 27.11.2023
    //int a;
    //cout << "Введите число больше нуля: ";
    //cin >> a;
    //while (a > 0) {
    //    cout << a % 10;
    //    a /= 10;
    //}
    
    //Задача 1 Через цикл for
    //for (int i = 12345; i > 0; i /= 10) {
    //    cout << i % 10;
    //}

    
    ////Задача 2 27.11.2023
    //int a;
    //cout << "Введите число: ";
    //cin >> a;
    //int result = 0;
    //while (a > 0) {
    //    result += a % 10;
    //    a /= 10;
    //}
    //cout << result;



    //Задача 3 27.11.2023
    //int a, b = 15, c = 0;
    //cout << "Введите кол-во дней сколько ползла улитка: ";
    //cin >> a;
    //for (a; a > 0; a--) {
    //    c += b;
    //    b += 2;
    //     
    //}
    //cout << "Улитка проползла: " << c;
    



    //Задача 4 27.11.2023
    //int orel = 0, reshka = 0;
    //for (int i = 9; i > 0; i--) {
    //    int num;
    //    cout << "Введите число (1 или 0): ";
    //    cin >> num;
    //    if (num == 1) {
    //        orel += 1;
    //    }
    //    else if (num == 0) {
    //        reshka += 1;
    //    }
    //    else {
    //        cout << "Вводите 1 или 0" << endl;
    //        i++;
    //    }
    //    
    //}
    //cout << "Орел: " << orel << endl
    //     << "Решка: " << reshka;



    // Задача 4 - через рандомайзер
    //int orel = 0, reshka = 0;
    //srand(time(0));
    //for (int i = 0; i < 9; i++) {
    //    int num = rand() % 2;
    //    if (num == 1) {
    //        orel += 1;
    //    }
    //    else {
    //        reshka += 1;
    //    }
    //}
    //cout << "Орел: " << orel << endl
    //     << "Решка: " << reshka;
    

    //Задача 5 27.11.2023
    int month, day, days_count;
    cout << "Введите месяц: ";
    cin >> month;
    cout << "Введите день: ";
    cin >> day;
    if (month % 2 == 0 && month != 2) {
        days_count = 30;
    }
    else if (month == 2) {
        days_count = 28;
    }
    else {
        days_count = 31;
    }

    for (int i = 1; i <= days_count; i++) {
        if ( % 7 == 0) {

        }
    }
    
    

    



  /*  int a[5] = { 1, 2, 3, 4, 5 };

    for (int i = 0; i < 5; i++) {
        cout << i << " Число " << pow(a[i],2)  << endl;
    }*/

    













    





   
    return 0;
}
