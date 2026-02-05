#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    int operator1, operator2;
    float time, minMTS = 3.5, minBeline = 3.7, minMegafone = 3.3, minTele2 = 2.8;
    cout << "Введите код вашего оператора: " << endl
         << "МТС     - 1\n"
            "Билайн  - 2\n"
            "Мегафон - 3\n"
            "Теле2   - 4\n"
            "\t- ";
    cin >> operator1;
    cout << "Введите код оператора на который будет сделан звонок: " << endl
        << "МТС     - 1\n"
        "Билайн  - 2\n"
        "Мегафон - 3\n"
        "Теле2   - 4\n"
        "\t- ";
    cin >> operator2;
    cout << "Введите длительность разговора (в минутах): ";
    cin >> time;
    if (operator1 == operator2) {
        cout << "Звонки внутри сети бесплатные.";
    }
    else if (operator1 == 1 && operator2 == 2 || operator2 == 3 || operator2 == 4) {
        cout << "Стоимость разговора: " << time * minMTS << endl;
    }
    else if (operator1 == 2 && operator2 == 1 || operator2 == 3 || operator2 == 4) {
        cout << "Стоимость разговора: " << time * minBeline << endl;
    }
    else if (operator1 == 3 && operator2 == 1 || operator2 == 2 || operator2 == 4) {
        cout << "Стоимость разговора: " << time * minMegafone << endl;
    }
    else if (operator1 == 4 && operator2 == 1 || operator2 == 2 || operator2 == 3) {
        cout << "Стоимость разговора: " << time * minTele2 << endl;
    }
    else {
        cout << "Некорректные данные. " << endl;
    }
}
