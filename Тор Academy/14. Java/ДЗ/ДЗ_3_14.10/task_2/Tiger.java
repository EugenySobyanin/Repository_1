public class Tiger extends Animal {
    private static final String TYPE_TITLE = "Tiger";

    // Конструкторы

    // Основной со всеми параметрами
    public Tiger(String name, Integer age, Integer weight){
        super(TYPE_TITLE, name, age, weight);
    }

    // Конструктор (имя, возраст)
    public Tiger(String name, Integer age){
        this(name,age, null);
    }

    // Конструктор (имя)
    public Tiger(String name){
        this(name, null);
    }

    // Конструктор без параметров
    public Tiger(){
        this(null);
    }

    @Override
    public String getType(){
        return TYPE_TITLE;
    }

    @Override
    public void setType(String type){
        throw new UnsupportedOperationException(
                "Нельзя изменить тип животного. Тип: Тигр"
        );
    }
}
