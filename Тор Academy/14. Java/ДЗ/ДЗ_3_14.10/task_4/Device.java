package org.example;

public class Device {
    private String title;
    private Integer price;
    private Integer weight;
    private String sound;

    // Конструкторы

    // Основной конструктор со всеми параметрами
    public Device(String title, Integer price, Integer weight, String sound){
        this.title = title != null ? title : "Не установлено";
        this.price = price;
        this.weight = weight;
        this.sound = sound != null ? sound : "Не установлено";
    }

    // Конструктор (название, цена)
    public Device(String title, Integer price){
        this(title, price, null, null);
    }

    // Конструктор (название, звук)
    public Device(String title, String sound){
        this(title, null, null, sound);
    }

    // Конструктор (название)
    public Device(String title){
        this(title, null, null, null);
    }

    // Конструктор без параметров
    public Device(){
        this(null);
    }

    // Геттеры

    public String getTitle() {
        return title;
    }

    public Integer getPrice() {
        return price;
    }

    public Integer getWeight() {
        return weight;
    }

    // Сеттеры

    public void setTitle(String title) {
        this.title = title;
    }

    public void setPrice(Integer price) {
        this.price = price;
    }

    public void setWeight(Integer weight) {
        this.weight = weight;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

    //  Методы

    public void sound() {
        System.out.println(sound);
    }

    public void show() {
        System.out.println(title);
    }

    public String desc() {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(!title.equals("Не установлено") ? "Название - " + title + "\n" : "");
        stringBuilder.append(price != null ? "Стоимость - " + price + "\n" : "");
        stringBuilder.append(weight != null ? "Вес - " + weight + "\n" : "");
        stringBuilder.append(!sound.equals("Не установлено") ? "Звук - " + sound + "\n" : "");
        if (stringBuilder.toString().equals("")){
            return "Информация отсутствует.";
        }
        return stringBuilder.toString();
    }
}
