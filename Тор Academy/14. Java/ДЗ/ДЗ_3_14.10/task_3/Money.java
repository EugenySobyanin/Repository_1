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

    public void setWhole(Integer whole) {
        this.whole = whole;
    }

    public void setPennies(Integer pennies) {
        this.pennies = pennies;
    }

    public void getCoastInfo(){
        System.out.println(whole.toString() + "." + makePenniesInfo());
    }

    private String makePenniesInfo(){
        if (pennies < 10)
            return "0" + pennies;
        return pennies.toString();
    }
}
