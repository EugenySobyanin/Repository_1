package org.example;


public class Product extends Money {
    private String title;  // Название товара

    // Конструкторы

    // Основной со всеми параметрами
    public Product(String title, Integer whole, Integer pennies){
        super(whole, pennies);
        this.title = title != null ? title : "Не установлено";
    }

    // Конструктор без копеек
    public Product(String title, Integer whole){
        this(title, whole, null);
    }

    // Методы

    public void setFullPrice(double price){
        Integer whole = (int) price;
        Integer pennies = (int) ((price - whole) * 100);
        setWholeAndPennies(whole, pennies);
    }

    // Уменьшение цены на заданное число
    public void downPrice(double value){
        double currentPrice = getWhole() + (double) getPennies() / 100;
        setFullPrice(currentPrice - value);
    }
}
