package org.example;

public class Array implements IMath {
    private int[] numbers;

    // Конструктор
    public Array(int[] numbers) {
        this.numbers = numbers;
    }

    // Максимальное значение
    @Override
    public int Max() {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalStateException("Массив пуст");
        }

        int max = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > max) {
                max = numbers[i];
            }
        }
        return max;

    }

    // Минимальное значение
    @Override
    public int Min() {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalStateException("Массив пуст");
        }

        int min = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] < min) {
                min = numbers[i];
            }
        }
        return min;

    }

    // Среднее значение
    @Override
    public float Avg() {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalStateException("Массив пуст");
        }

        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        return (float) sum / numbers.length;
    }

    // Вывод массива
    public void printArray() {
        System.out.print("Массив: [");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i]);
            if (i < numbers.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}
