import java.time.LocalDate;
import java.util.function.BiFunction;

void main() {
    // Задание 1.

    // 1. Проверка является ли год високосным (2 варианта реализации)
    IntPredicate isLeapYear = year -> (year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0);
    Function<Integer, Boolean> isLeapYear2 =
            year -> (year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0);

    System.out.println(isLeapYear.test(2012));
    System.out.println(isLeapYear.test(2011));
    System.out.println(isLeapYear2.apply(2024));
    System.out.println(isLeapYear2.apply(1000));

    // 2. Подсчет количества дней между двумя датами
    BiFunction<LocalDate, LocalDate, Long> daysBetween =
            (date1, date2) -> ChronoUnit.DAYS.between(date1, date2);

    LocalDate date1 = LocalDate.of(2024, 1, 25);
    LocalDate date2 = LocalDate.of(2025, 1, 25);
    LocalDate date3 = LocalDate.of(2025, 1, 27);

    System.out.println(daysBetween.apply(date1, date2));
    System.out.println(daysBetween.apply(date2, date3));

    // 3. Подсчет количества полных недель между 2 датами
    BiFunction<LocalDate, LocalDate, Long> fullWeeksBetween =
            (dt1, dt2) -> dt1.until(dt2, ChronoUnit.WEEKS);

    System.out.println(fullWeeksBetween.apply(date1, date2));
    System.out.println(fullWeeksBetween.apply(date2, date3));

    // 4. Подсчет дня недели по полученной дате
    Function<LocalDate, DayOfWeek> dayOfWeek = LocalDate::getDayOfWeek;

    System.out.println(dayOfWeek.apply(date1));
    System.out.println(dayOfWeek.apply(date2));
    System.out.println(dayOfWeek.apply(date3));


    // Задание 2.

    Fraction fraction1 = new Fraction(3, 6);
    Fraction fraction2 = new Fraction(9, 99);

    // 1. Сумма двух дробей
    BiFunction<Fraction, Fraction, Fraction> sumFractions =
            (fr1, fr2) -> fr1.add(fr2);

    System.out.println(sumFractions.apply(fraction1, fraction2).toString());


    // 2. Разница двух дробей
    BiFunction<Fraction, Fraction, Fraction> differenceFractions =
            (fr1, fr2) -> fr1.subtract(fr2);

    System.out.println(sumFractions.apply(fraction2, fraction1).toString());

    // 3. Произведение двух дробей
    BiFunction<Fraction, Fraction, Fraction> multFractions =
            (fr1, fr2) -> fr1.multiply(fr2);

    System.out.println(multFractions.apply(fraction1, fraction2).toString());

    // 4. Деление двух дробей
    BiFunction<Fraction, Fraction, Fraction> devideFraction =
            (fr1, fr2) -> fr1.divide(fr2);

    System.out.println(multFractions.apply(fraction2, fraction1).toString());


    // Задание 3. (Обязательно использовать шаблоны)
    @FunctionalInterface
    interface IntQuadFunction {
        int apply(int a, int b, int c, int d);
    }

    // 1. Максимум из четырех
    IntQuadFunction maxOfFour = (a, b, c, d) ->
            Math.max(Math.max(a, b), Math.max(c, d));

    System.out.println(maxOfFour.apply(1, 2, 3, 5));

    // 2. Минимум из четырех
    IntQuadFunction minOfFour = (a, b, c, d) ->
            Math.min(Math.min(a, b), Math.min(c, d));

    System.out.println(minOfFour.apply(1, 2,  3, 4));

    // Задание 4. (использовать лямбду как параметр)
    // Ищем сумму элементов удовлетворяющих условию
    Number[] nums = {1, -5, 6, 0.4, 2, 11, 3, 3, 5, 6, 9, 10, 12};

    // Функциональный интерфейс
    @FunctionalInterface
    interface NumberCondition {
        boolean test(Number n);
    }

    public static double sumIf(Number[] numbers, NumberCondition condition) {
        double result = 0;
        for (Number n : numbers) {
            if (condition.test(n)) {
                result += n.doubleValue();
            }
        }
        return result;
    }

    // 1. Проверка на равенство конкретному числу

    // 2. Число не находится в диапазоне от А до В

    // 3. Проверка на положительность числа

    // 4. Проверка на отрицательность числа
}