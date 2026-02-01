package org.example;

// Тестовый класс
public class TestIMath {
    public static void main(String[] args) {
        int[] data = {5, 2, 8, 1, 9, 3};
        Array array = new Array(data);

        array.printArray();
        System.out.println("Максимальный элемент: " + array.Max());
        System.out.println("Минимальный элемент: " + array.Min());
        System.out.println("Среднее арифметическое: " + array.Avg());
    }
}
