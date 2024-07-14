#include <iostream>
#include <time.h>


void print_dice(int a);

int main()
{
    using namespace std;
    srand(time(NULL));
    setlocale(LC_ALL, "RU");

    int sum_1 = 0, sum_2 = 0, throw_num = 1, throw_sum = 0, total_sum1 = 0, total_sum2 = 0;

    for (int i = 1; i <= 6; i++) 
    {
        if (i % 2 != 0) 
        {
            cout << "Первый игрок выполняет бросок № " << throw_num << endl;
        }
        else 
        {
            cout << "Второй игрок выполняе бросок № " << throw_num << endl;
            ++throw_num;
        }
        throw_sum = 0;

        for (int j = 0; j < 2; j++) 
        {
            int a = rand() % 6 + 1;
            throw_sum += a;
            print_dice(a);
            cout << endl;
        }
        (i % 2 != 0) ? total_sum1 += throw_sum : total_sum2 += throw_sum;
        cout << "Cумма очков броска: " << throw_sum << endl;
        cout << endl;
    }
    cout << "Общее количество очков первого игрока: " << total_sum1 << endl
         << "Общее количество очков второго игрока: " << total_sum2 << endl;

    return 0;
}

void print_dice(int a) 
{
    using namespace std;
    int n = 7;
    switch (a) 
    {
    case 1:
        for (int i = 1; i <= n; i++) 
        {
            for (int j = 1; j <= n; j++) 
            {
                if (i == n / 2 + 1 and j == n / 2 + 1) 
                {
                    cout << "+ ";
                }
                else if (i == 1 or j == 1 or i == n or j == n) 
                {
                    cout << ". ";
                }
                else 
                {
                    cout << "  ";
                }
            }
            cout << endl;
        }
        break;
    case 2:
        for (int i = 1; i <= n; i++) 
        {
            for (int j = 1; j <= n; j++) 
            {
                if (i == 3 and j == 5 or i == 5 and j == 3) 
                {
                    cout << "+ ";
                }
                else if (i == 1 or j == 1 or i == n or j == n) 
                {
                    cout << ". ";
                }
                else 
                {
                    cout << "  ";
                }
            }
            cout << endl;
        }
        break;
    case 3:
        for (int i = 1; i <= n; i++) 
        {
            for (int j = 1; j <= n; j++) 
            {
                if (i == n / 2 + 1 and j == n / 2 + 1) 
                {
                    cout << "+ ";
                }
                else if (i == 2 and j == 6 or i == 6 and j == 2) 
                {
                    cout << "+ ";
                }
                else if (i == 1 or j == 1 or i == n or j == n) 
                {
                    cout << ". ";
                }
                else 
                {
                    cout << "  ";
                }
            }
            cout << endl;
        }
        break;
    case 4:
        for (int i = 1; i <= n; i++) 
        {
            for (int j = 1; j <= n; j++) 
            {
                if (i == 3 and j == 5 or i == 5 and j == 3
                    or i == 3 and j == 3 or i == 5 and j == 5) 
                {
                    cout << "+ ";
                }
                else if (i == 1 or j == 1 or i == n or j == n) 
                {
                    cout << ". ";
                }
                else 
                {
                    cout << "  ";
                }
            }
            cout << endl;
        }
        break;
    case 5:
        for (int i = 1; i <= n; i++) 
        {
            for (int j = 1; j <= n; j++) 
            {
                if (i == n / 2 + 1 and j == n / 2 + 1) 
                {
                    cout << "+ ";
                }
                else if (i == 2 and j == 6 or i == 6 and j == 2
                    or i == 2 and j == 2 or i == 6 and j == 6) 
                {
                    cout << "+ ";
                }
                else if (i == 1 or j == 1 or i == n or j == n) 
                {
                    cout << ". ";
                }
                else 
                {
                    cout << "  ";
                }
            }
            cout << endl;
        }
        break;
    case 6:
        for (int i = 1; i <= n; i++) 
        {
            for (int j = 1; j <= n; j++) 
            {
                if (i == 2 and j == 6 or i == 6 and j == 2
                    or i == 2 and j == 2 or i == 6 and j == 6) 
                {
                    cout << "+ ";
                }
                else if (i == n / 2 + 1 and j == 2 or i == n / 2 + 1 and j == 6) 
                {
                    cout << "+ ";
                }
                else if (i == 1 or j == 1 or i == n or j == n) 
                {
                    cout << ". ";
                }
                else 
                {
                    cout << "  ";
                }
            }
            cout << endl;
        }
        break;
    }

}