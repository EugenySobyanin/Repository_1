#include <iostream>
#include <iomanip>
#include <time.h>
#include <string>

void show_card(int number, int suit);


int main()
{
    using namespace std;
    setlocale(LC_ALL, "RU");
    int number, suit;
    cout << "Номер карты: " << endl
        << "A - 1" << endl
        << "6 - 2" << endl
        << "7 - 3" << endl
        << "8 - 4" << endl
        << "9 - 5" << endl
        << "10 - 6" << endl
        << "J - 7" << endl
        << "Q - 8" << endl
        << "K - 9" << endl;
    cin >> number;
    cout << "Масть: " << endl
        << "Крести - 1" << endl
        << "Черви - 2" << endl
        << "Буби - 3" << endl
        << "Пики - 4" << endl;
    cin >> suit;
    
    show_card(number, suit);

    return 0;
}

void show_card(int number, int suit) {
    using namespace std;

    char card[9] = { 'A', '6', '7', '8', '9', '0', 'J', 'Q', 'K' };

    cout << " __________" << endl
        << "|          |" << endl;
    if (number == 6) cout << "|" << setw(7) << "1" << card[number - 1] << "  |" << endl;
    else cout << "|" << setw(8) << card[number - 1] << "  |" << endl;
        cout << "|          |" << endl;
    switch (suit) {
        case(1): cout << "|  КРЕСТИ  |" << endl; break;
        case(2): cout << "|   ЧЕРВИ  |" << endl; break;
        case(3): cout << "|   БУБИ   |" << endl; break;
        case(4): cout << "|   ПИКИ   |" << endl; break;
    }
    cout << "|          |" << endl;
    if (number == 6) cout << "| 1" << card[number - 1] << setw(8) << "|" << endl;
    else cout << "|" << setw(2) << card[number - 1] << setw(9) << "|" << endl;
         cout << "|__________|" << endl;
}