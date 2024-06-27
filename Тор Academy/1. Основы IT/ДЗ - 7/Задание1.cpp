#include <iostream>

long sum_even_fibonacci(long limit = 4000000) {

    long num1 = 0, num2 = 1, result_sum = 0;

    while (true) {

        long temp = num1;
        num1 = num2;
        num2 = temp + num2;

        if (num2 % 2 == 0) result_sum += num2;
        
        if (num2 + num1 > limit) break;
    
    }
    return result_sum;
}

int main()
{
    using namespace std;
    setlocale(LC_ALL, "RU");

    cout << "Ответ: " << sum_even_fibonacci() << endl;
    

}

