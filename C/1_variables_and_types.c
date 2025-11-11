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

    // char
    char sym1 = 'i';  // 1байт
    unsigned char sym2 = 50;  // 1байт от 0 до 255
    signed char sym3 = -50;  // 1байт от -128 до 127
    putchar(sym3);  // Выводит только один символ
    printf("\n");
    printf("%c - %c - %c\n", sym1, sym2, sym3);
    printf("%d - %d - %d\n", sym1, sym2, sym3);

    // Целочисленные типы
    short short_num = 15155;  // 2байта от -32 768 до 32 767
    long long_num = 2099123124;  // 4байта от −2 147 483 648 до 2 147 483 647
    long long long_long_num = 9223372036854775807;  // 8байт от -9 223 372 036 854 775 807 до +9 223 372 036 854 775 807
    printf("short = %hd\n", short_num);
    printf("Size of long: %zu bytes\n", sizeof(int));  // Проверка сколько памяти занимает определенный тип данных
    printf("LONG_MAX = %ld\n", LONG_MAX);  // Максимальное значение, которое помещается в long
    printf("long = %ld\n", long_num);
    printf("long_long = %lld\n", long_long_num);

    // Получатся, что int не отличается от long
    int num5 = 2147483647;  // 4байта от −2 147 483 648 до 2 147 483 647
    printf("int = %d\n", num5);

    // unsigned типы и их спецификаторы при выводе %u
    unsigned int num6 = 3000000000;  // 4байта
    unsigned short unsigned_short = 60000;
    unsigned long long unsigned_long_long = 18333444555666777;
    printf("unsigned int = %u\n", num6);
    printf("unsigned_short = %hu\n", unsigned_short);
    printf("unsigned_long_long = %llu\n", unsigned_long_long);

    // Разные числовые системы
    int code1 = 0b1011;  // Двоичная система - число 11
    int code2 = 013;  // Восьмиричная система - число 11
    int code3 = 0XB;  // Шестнадцатиричная система - число 11
    printf("code1 = %d\tcode2 = %d\tcode3 = %d\n", code1, code2, code3);

    // Числа с плавающей точкой
    float float_num = 355.16f;  // 4байта
    double double_num = 144555.26;  // 8байт
    long double long_double_num = 455555.78l;  // 10байт
    printf("float_num = %f\n", float_num);
    printf("double_num = %f\n", double_num);
    printf("long_double_num = %Lf\n", long_double_num);

    // typedef - позволяет определить псевдоним для типа данных
    typedef unsigned long long MAX_NUM;
    MAX_NUM ull_num = 18333444555666777;
    printf("ull_num = %llu\n", ull_num);

    // sizeof - получение размера типа данных в байтах
    printf("sizeof(short) = %llu\n", sizeof(short));
    printf("sizeof(int) = %llu\n", sizeof(int));
    printf("sizeof(long) = %llu\n", sizeof(long));
    printf("sizeof(long long) = %llu\n", sizeof(long long));
    size_t result = sizeof(size_t);  // Пример с использованием size_t, size_t - псевдоним типа данных для результата функции sizeof
    printf("sizeof(size_t) = %llu\n", result);
    
    return 0;
}