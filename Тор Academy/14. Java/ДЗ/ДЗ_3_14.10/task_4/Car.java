package org.example;

public class Car extends Device {
    private static final String TITLE = "Автомобиль";
    private static final String SOUND = "бип-бип вррррр";

    // Конструкторы

    public Car(Integer price, Integer weight) {
        super(TITLE, price, weight, SOUND);
    }

    public Car() {
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
                "Невозможно изменить звук автомобиля. Звук фиксирован: \"" + SOUND + "\""
        );
    }
}
