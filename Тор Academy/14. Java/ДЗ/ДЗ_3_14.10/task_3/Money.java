package org.example;

public class Money {
    private Integer whole;
    private Integer pennies;

    // Конструкторы

    public Money(Integer whole, Integer pennies){
        this.whole = whole != null ? whole : 0;
        this.pennies = pennies != null ? pennies : 0;
    }

    public Money(Integer whole){
        this(whole, null);
    }

    public Money(){
        this(null, null);
    }

    // Геттеры

    protected Integer getWhole(){return  this.whole; }

    protected Integer getPennies(){return  this.pennies; }

    // Сеттеры

    public void setWhole(Integer whole) {
        this.whole = whole;
    }

    public void setPennies(Integer pennies) {
        this.pennies = pennies;
    }

    public void setWholeAndPennies(Integer whole, Integer pennies){
        this.whole = whole;
        this.pennies = pennies;
    }

    // Другие методы

    public void getCoastInfo(){
        System.out.println(whole.toString() + "." + makePenniesInfo());
    }

    private String makePenniesInfo(){
        if (pennies < 10)
            return "0" + pennies;
        return pennies.toString();
    }
}
