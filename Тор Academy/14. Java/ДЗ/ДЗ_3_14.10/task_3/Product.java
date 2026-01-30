public class Product extends Money {
    private String title;

    // Конструкторы

    public Product(String title, Integer whole, Integer pennies){
        super(whole, pennies);
        this.title = title != null ? title : "Не установлено";
    }

    // Методы

    private setWholeAndPennie
}
