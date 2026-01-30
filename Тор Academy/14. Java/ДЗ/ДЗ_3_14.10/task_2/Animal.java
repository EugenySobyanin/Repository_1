import javax.print.CancelablePrintJob;

public class Animal {
    private String type;
    private String name;
    private Integer age;
    private Integer weight;

    // Конструкторы

    // Основной конструктор со всеми параметрами
    public Animal(String type, String name, Integer age, Integer weight){
        this.type = type != null ? type : "Не установлено";
        this.name = name != null ? name : "Не установлено";
        this.age = age;
        this.weight = weight;
    }

    // Конструктор (Тип, имя, возраст)
    public Animal (String type, String name, Integer age){
        this(type, name, age, null);
    }

    // Конструктор (Тип, имя)
    public Animal(String type, String name){
        this(type, name, null);
    }

    // Конструктор (Тип, возраст)
    public Animal(String type, Integer age){
        this(type, null, age);
    }

    // Конструктор (Тип)
    public Animal(String type){
        this(type, null, null);
    }

    // Конструктор без параметров
    public Animal(){
        this(null, null, null, null);
    }

    // Геттеры

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getName() {
        return name;
    }

    // Сеттеры

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public Integer getWeight() {
        return weight;
    }

    public void setWeight(Integer weight) {
        this.weight = weight;
    }

    // Методы

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Животное: ");

        if (type != null && !"Не установлено".equals(type)) {
            sb.append("тип='").append(type).append('\'');
        }

        if (name != null && !"Не установлено".equals(name)) {
            if (sb.length() > 10) sb.append(", ");
            sb.append("кличка='").append(name).append('\'');
        }

        if (age != null) {
            if (sb.length() > 10) sb.append(", ");
            sb.append("возраст=").append(age);
            // Добавляем "лет/год/года" в зависимости от возраста
            if (age % 10 == 1 && age % 100 != 11) {
                sb.append(" год");
            } else if (age % 10 >= 2 && age % 10 <= 4 && (age % 100 < 10 || age % 100 >= 20)) {
                sb.append(" года");
            } else {
                sb.append(" лет");
            }
        }

        if (weight != null) {
            if (sb.length() > 10) sb.append(", ");
            sb.append("вес=").append(weight).append(" кг");
        }

        // Если все поля null или "Не установлено"
        if (sb.length() <= 10) {
            sb.append("данные не указаны");
        }

        return sb.toString();
    }
}
