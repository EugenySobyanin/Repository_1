﻿#include <iostream>
#include <time.h>


int range_sum(int x, int y);

int main()
{
    using namespace std;
    srand(time(NULL));
    setlocale(LC_ALL, "RU");

    cout << range_sum(10, 1);

}

int range_sum(int x, int y)
{
    using namespace std;
    int result = 0;

    if (y < x)
    {
        swap(x, y);
    }
    
    for (int i = x + 1; i < y; i++)
    {
        result += i;
    }
    return result;
}