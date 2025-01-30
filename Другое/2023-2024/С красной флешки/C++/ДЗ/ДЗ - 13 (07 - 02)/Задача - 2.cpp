#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    int len_cell;
    cout << "Введите длину клеточки: ";
    cin >> len_cell;
    bool a = true;
    for (int i = 1; i <= 8 * len_cell; i++) {
        if (a) {
            for (int j = 1; j <= 8; j++) {
                if (j % 2 == 0) {
                    cout << "***";
                }
                else {
                    cout << "___";
                }
            }
            cout << endl;
        }
        else {
            for (int k = 1; k <= 8; k++) {
                if (k % 2 == 0) {
                    cout << "___";
                }
                else {
                    cout << "***";
                }
            }
            cout << endl;
        
        }
        if (i % len_cell == 0 && len_cell != 1) {
            a = !a;
        }
        if (len_cell == 1) {
            a = !a;
        }
    }

    return 0;
}