package org.example;

public class Microwave extends Device {
    private static final String TITLE = "Микроволновка";
    private static final String SOUND = "ууууууууууу.. дзынь!";

    // Конструкторы

    public Microwave(Integer price, Integer weight) {
        super(TITLE, price, weight, SOUND);
    }

    public Microwave() {
        this(null, null);
    }

    @Override
    public void setTitle(String title) {
        throw new UnsupportedOperationException(
                "Невозможно изменить название. Название фиксировано: \"" + TITLE + "\""
        );
    }

    @Override
    public void setSound(String sound) {
        throw new UnsupportedOperationException(
                "Невозможно изменить звук микроволновки. Звук фиксирован: \"" + SOUND + "\""
        );
    }
}