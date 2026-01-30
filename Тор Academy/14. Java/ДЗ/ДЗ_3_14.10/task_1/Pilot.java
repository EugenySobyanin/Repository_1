import java.util.List;

public class Pilot extends Human {
    private static final String PROFESSION_TITLE = "Пилот";
    private Integer standartFlightHours; // Норма летных часов в месяц
    private Integer currentFlightHours; // Текущее количество часов

    // Конструкторы

    // Основной конструктор со всеми параметрами
    public Pilot(
            String fullName,
            Integer age,
            Integer workExperience,
            Integer standartFlightHours,
            Integer currentFlightHours
    ){
        super(fullName, age, PROFESSION_TITLE, workExperience);
        standartFlightHours = standartFlightHours != null ? standartFlightHours : 100;
        currentFlightHours = currentFlightHours != null ? currentFlightHours: 0;
    }

    // Конструктор по умолчанию
    public Pilot (){
        this(null, null, null, null, null);
    }

    // Конструктор (имя, норма часов, текущие часы)
    public Pilot(String fullname, Integer standartFlightHours, Integer currentFlightHours){
        this(fullname, null, null, standartFlightHours, currentFlightHours);
    }

    // Геттеры

    @Override
    public String getProfession(){
        return PROFESSION_TITLE;
    }

    public Integer getStandartFlightHours() {
        return standartFlightHours;
    }

    public Integer getCurrentFlightHours() {
        return currentFlightHours;
    }

    // Сеттеры

    @Override
    public void setProfession(String profession) {
        throw new UnsupportedOperationException(
                "Нельзя изменить профессию. Профессия фиксирована: Пилот"
        );
    }

    public void setStandartFlightHours(Integer standartFlightHours) {
        this.standartFlightHours = standartFlightHours;
    }

    public void setCurrentFlightHours(Integer currentFlightHours) {
        this.currentFlightHours = currentFlightHours;
    }

    // Методы

    // Сколько часов осталось налетать в текущем месяце?
    public Integer getHoursRemains(){
        return standartFlightHours - currentFlightHours;
    }

    // Обнулить количество летных часов
    public void resetFlightHours(){
        currentFlightHours = 0;
    }
}
