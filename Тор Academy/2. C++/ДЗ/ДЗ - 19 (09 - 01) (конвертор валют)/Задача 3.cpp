#include <iostream>
#include <string>

int main()
{
    using namespace std;
    setlocale(LC_ALL, "RU");

    string days_of_the_week[7]{ "понедльник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье" };
    float spend_days[7]{ 0 };
    float total_sum = 0;
    int days_over_100 = 0;
    string name_days_over_100[7];


    for (int i = 0; i < 7; i++) {
        float current_value;
        switch (i) {
        case 0:
            cout << "Расходы за " << days_of_the_week[i] << " :";
            cin >> spend_days[i];
            break;

        case 1:
            cout << "Расходы за " << days_of_the_week[i] << " :";
            cin >> spend_days[i];
            break;

        case 2:
            cout << "Расходы за " << days_of_the_week[i] << " :";
            cin >> spend_days[i];
            break;

        case 3:
            cout << "Расходы за " << days_of_the_week[i] << " :";
            cin >> spend_days[i];
            break;

        case 4:
            cout << "Расходы за " << days_of_the_week[i] << " :";
            cin >> spend_days[i];
            break;

        case 5:
            cout << "Расходы за " << days_of_the_week[i] << " :";
            break;

        case 6:
            cout << "Расходы за " << days_of_the_week[i] << " :";
            cin >> spend_days[i];
            break;

        }
    }



    for (int i = 0; i < 7; ++i) {
        total_sum += spend_days[i];
        if (spend_days[i] > 100) {
            ++days_over_100;
            name_days_over_100[i] = spend_days[i];
        }
    }


    cout << "Расходы за неделю: " << total_sum << " $" << endl;
    cout << "Расходы в среднем за неделю: " << total_sum / 7 << " $" << endl;
    cout << "Количество дней, когда расходы больше 100$: " << days_over_100 << endl;
    cout << "Дни недели, когда траты были больше 100$: " << endl;
    for (int i = 0; i < days_over_100; ++i) {
        cout << "\t\t" << name_days_over_100[i] << endl;
    }



    return 0;
}

