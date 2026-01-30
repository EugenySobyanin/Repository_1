public class Kangaroo extends Animal{
    private static final String TYPE_TITLE = "Kangaroo";

    // Конструкторы

    // Основной со всеми параметрами
    public Kangaroo(String name, Integer age, Integer weight){
        super(TYPE_TITLE, name, age, weight);
    }

    // Конструктор (имя, возраст)
    public Kangaroo(String name, Integer age){
        this(name,age, null);
    }

    // Конструктор (имя)
    public Kangaroo(String name){
        this(name, null);
    }

    // Конструктор без параметров
    public Kangaroo(){
        this(null);
    }

    @Override
    public String getType(){
        return TYPE_TITLE;
    }

    @Override
    public void setType(String type){
        throw new UnsupportedOperationException(
                "Нельзя изменить тип животного. Тип: Кенгуру"
        );
    }
}
