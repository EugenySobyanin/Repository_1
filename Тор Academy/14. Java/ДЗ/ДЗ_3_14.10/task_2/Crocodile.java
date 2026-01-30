public class Crocodile extends  Animal{
    private static final String TYPE_TITLE = "Crocodile";

    // Конструкторы

    // Основной со всеми параметрами
    public Crocodile(String name, Integer age, Integer weight){
        super(TYPE_TITLE, name, age, weight);
    }

    // Конструктор (имя, возраст)
    public Crocodile(String name, Integer age){
        this(name,age, null);
    }

    // Конструктор (имя)
    public Crocodile(String name){
        this(name, null);
    }

    // Конструктор без параметров
    public Crocodile(){
        this(null);
    }

    @Override
    public String getType(){
        return TYPE_TITLE;
    }

    @Override
    public void setType(String type){
        throw new UnsupportedOperationException(
                "Нельзя изменить тип животного. Тип: Крокодил"
        );
    }
}
