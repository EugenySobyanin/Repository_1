package org.example;

public class Teapot extends Device {
    private static final String TITLE = "Чайник";
    private static final String SOUND = "Пшшшшшшшш";

    // Конструкторы

    public Teapot(Integer price, Integer weight) {
        super(TITLE, price, weight, SOUND);
    }

    public Teapot() {
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
                "Невозможно изменить звук чайника. Звук фиксирован: \"" + SOUND + "\""
        );
    }
}