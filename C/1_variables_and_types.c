#include <stdio.h>
#include <locale.h>
#include <limits.h>
 
int main(void)
{
    char *locale = setlocale(LC_ALL, "");

    // Инициализация нескольких переменных
    int num1 = 10, num2 = 20, num3 = 30;
    printf("num1 = %d\nnum2 = %d\nnum3 = %d\n", num1, num2, num3);

    // Типы данных
    char sym1 = 'i'; // 1байт
    unsigned char sym2 = 50; // 1байт от 0 до 255
    signed char sym3 = -50; // 1байт от -128 до 127
    putchar(sym3); // Выводит только один символ
    printf("\n");
    printf("%c%c%c\n", sym1, sym2, sym3);

    short short_num = 15155; // 2байта от -32 768 до 32 767
    printf("short = %hd\n", short_num);
    long long_num = 2099123124; // 4байта от −2 147 483 648 до 2 147 483 647
    long long long_long_num = 9223372036854775807; // 8байт от -9 223 372 036 854 775 807 до +9 223 372 036 854 775 807
    printf("Size of long: %zu bytes\n", sizeof(int));
    printf("LONG_MAX = %ld\n", LONG_MAX);
    printf("long = %ld\n", long_num);
    printf("long_long = %lld\n", long_long_num);

    // Получатся, что int не отличается от long
    int num5 = 2147483647; // 4байта от −2 147 483 648 до 2 147 483 647
    unsigned int num6 = 3000000000; // 4байта
    printf("int = %d\n", num5);

    float num6 = 355.16; // 4байта
    double num7 = 144555.26 // 8байт
    long double num8 = 455555.78 // 10байт
    
    return 0;
}