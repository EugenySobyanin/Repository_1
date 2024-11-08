﻿#include <iostream>
#include <time.h>

void sum_massive_element(int arr_1[], int arr_2[], int arr_3[], int len);


int main()
{
    using namespace std;
    setlocale(LC_ALL, "RU");
    srand(time(0));

    const int len = 10;
    int numbers[len]{}, nums_1[len]{}, nums_2[len]{};

    for (int i = 0; i < len; i++)
    {
        nums_1[i] = 5 + rand() % 10;
        cout << nums_1[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < len; i++)
    {
        nums_2[i] = 10 + rand() % 10;
        cout << nums_2[i] << " ";
    }
    cout << endl;

    sum_massive_element(nums_1, nums_2, numbers, len);
    

    return 0;
}

void sum_massive_element(int arr_1[], int arr_2[], int arr_3[], int len)
{
    using namespace std;
    for (int i = 0; i < len; i++)
    {
        arr_3[i] = arr_1[i] + arr_2[i];
        cout << arr_3[i] << " ";
    }
}