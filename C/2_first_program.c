#include <stdio.h>
#include <locale.h>

int main(void) {

    char *locale = setlocale(LC_ALL, "");

    printf("Привет, мир!\n");
    return 0;
}

/*
gcc
Команда для компиляции файла gcc 2_first_program.c
*/

/*
clang
Команда для компиляции файла clang 2_first_program.c -o first.exe
флаг -o для того чтобы задать имя файлу
запуск файла - ./first
*/

/*
Кириллица

    - создаем locale
    - меняем кодировку в редакторе
*/

