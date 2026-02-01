package org.example;

public class Ship extends Device {
    private static final String TITLE = "Кораблик";
    private static final String SOUND = "Туууууууу";

    // Конструкторы

    public Ship(Integer price, Integer weight) {
        super(TITLE, price, weight, SOUND);
    }

    public Ship() {
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
                "Невозможно изменить звук корабля. Звук фиксирован: \"" + SOUND + "\""
        );
    }
}
