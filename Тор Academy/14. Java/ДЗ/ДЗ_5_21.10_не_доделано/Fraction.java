public class Fraction {
    private int numerator;    // числитель
    private int denominator;  // знаменатель

    public Fraction() {
        this.numerator = 0;
        this.denominator = 1;
    }


    public Fraction(int numerator, int denominator) {
        if (denominator == 0) {
            throw new IllegalArgumentException("Знаменатель не может быть равен 0");
        }
        this.numerator = numerator;
        this.denominator = denominator;
        simplify();
    }

    /**
     * Конструктор для целого числа - создает дробь number/1
     * @param number целое число
     */
    public Fraction(int number) {
        this.numerator = number;
        this.denominator = 1;
    }

    /**
     * Конструктор копирования
     * @param other другая дробь для копирования
     */
    public Fraction(Fraction other) {
        this.numerator = other.numerator;
        this.denominator = other.denominator;
    }

    // Геттеры
    public int getNumerator() {
        return numerator;
    }

    public int getDenominator() {
        return denominator;
    }

    // Сеттеры с проверками
    public void setNumerator(int numerator) {
        this.numerator = numerator;
        simplify();
    }

    public void setDenominator(int denominator) {
        if (denominator == 0) {
            throw new IllegalArgumentException("Знаменатель не может быть равен 0");
        }
        this.denominator = denominator;
        simplify();
    }

    /**
     * Метод для нахождения наибольшего общего делителя (НОД)
     * @param a первое число
     * @param b второе число
     * @return НОД чисел a и b
     */
    private int gcd(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    /**
     * Метод для сокращения дроби
     */
    private void simplify() {
        if (denominator < 0) {
            numerator = -numerator;
            denominator = -denominator;
        }

        int gcd = gcd(numerator, denominator);
        if (gcd != 0) {
            numerator /= gcd;
            denominator /= gcd;
        }
    }

    /**
     * Сложение дробей
     * @param other другая дробь
     * @return новая дробь - результат сложения
     */
    public Fraction add(Fraction other) {
        int newNumerator = this.numerator * other.denominator +
                other.numerator * this.denominator;
        int newDenominator = this.denominator * other.denominator;
        return new Fraction(newNumerator, newDenominator);
    }

    /**
     * Вычитание дробей
     * @param other другая дробь
     * @return новая дробь - результат вычитания
     */
    public Fraction subtract(Fraction other) {
        int newNumerator = this.numerator * other.denominator -
                other.numerator * this.denominator;
        int newDenominator = this.denominator * other.denominator;
        return new Fraction(newNumerator, newDenominator);
    }

    /**
     * Умножение дробей
     * @param other другая дробь
     * @return новая дробь - результат умножения
     */
    public Fraction multiply(Fraction other) {
        int newNumerator = this.numerator * other.numerator;
        int newDenominator = this.denominator * other.denominator;
        return new Fraction(newNumerator, newDenominator);
    }

    /**
     * Деление дробей
     * @param other другая дробь
     * @return новая дробь - результат деления
     * @throws ArithmeticException если деление на ноль
     */
    public Fraction divide(Fraction other) {
        if (other.numerator == 0) {
            throw new ArithmeticException("Деление на ноль");
        }
        int newNumerator = this.numerator * other.denominator;
        int newDenominator = this.denominator * other.numerator;
        return new Fraction(newNumerator, newDenominator);
    }

    /**
     * Проверка равенства дробей
     * @param other другая дробь
     * @return true если дроби равны
     */
    public boolean equals(Fraction other) {
        if (this == other) return true;
        Fraction f1 = new Fraction(this.numerator, this.denominator);
        Fraction f2 = new Fraction(other.numerator, other.denominator);
        f1.simplify();
        f2.simplify();
        return f1.numerator == f2.numerator && f1.denominator == f2.denominator;
    }

    /**
     * Сравнение дробей
     * @param other другая дробь
     * @return -1 если this < other, 0 если this == other, 1 если this > other
     */
    public int compareTo(Fraction other) {
        int left = this.numerator * other.denominator;
        int right = other.numerator * this.denominator;
        return Integer.compare(left, right);
    }

    /**
     * Проверка, является ли дробь положительной
     * @return true если дробь > 0
     */
    public boolean isPositive() {
        return (numerator > 0 && denominator > 0) || (numerator < 0 && denominator < 0);
    }

    /**
     * Проверка, является ли дробь отрицательной
     * @return true если дробь < 0
     */
    public boolean isNegative() {
        return (numerator > 0 && denominator < 0) || (numerator < 0 && denominator > 0);
    }

    /**
     * Проверка, является ли дробь целым числом
     * @return true если знаменатель делит числитель без остатка
     */
    public boolean isInteger() {
        return numerator % denominator == 0;
    }

    /**
     * Преобразование дроби в десятичное число
     * @return десятичное представление дроби
     */
    public double toDouble() {
        return (double) numerator / denominator;
    }

    /**
     * Преобразование дроби в смешанное число
     * @return строка в формате "целая_часть числитель/знаменатель"
     */
    public String toMixedNumber() {
        if (denominator == 0) return "Undefined";

        int wholePart = numerator / denominator;
        int remainder = Math.abs(numerator % denominator);

        if (remainder == 0) {
            return String.valueOf(wholePart);
        } else if (wholePart == 0) {
            return toString();
        } else {
            return wholePart + " " + remainder + "/" + denominator;
        }
    }

    /**
     * Строковое представление дроби
     * @return строка в формате "числитель/знаменатель"
     */
    @Override
    public String toString() {
        if (denominator == 1) {
            return String.valueOf(numerator);
        }
        return numerator + "/" + denominator;
    }
}
