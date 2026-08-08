#include <iostream>
#include <iomanip>
#include <time.h>
#include <string>


template<typename T>
void create_massive(T arr, int size);

template<typename T>
float arithmetic_mean(T arr, int size);

template<typename T>
void print(T arr, int size);


int main()
{
    using namespace std;
    setlocale(LC_ALL, "RU");

    const int size = 10;
    int arr_1[size];

    create_massive(arr_1, size);
    print(arr_1, size);

    cout << "Среднеарифметическое = " << arithmetic_mean(arr_1, size);
}


template<typename T>
void create_massive(T arr, int size) {

    using namespace std;
    srand(time(0));

    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 20;
    }
}


template<typename T>
float arithmetic_mean(T arr, int size) {
    float sum = 0;

    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum / float(size);
}

template<typename T>
void print(T arr, int size) {

    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}
