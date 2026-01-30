import java.io.PrintWriter;
import java.time.LocalDate;


public class Human {
    private String fullName;
    private Integer age;
    private String profession;
    private Integer workExperience;

    // Конструкторы

    // Основной конструктор со всеми параметрами
    public Human(String fullName,
                 Integer age,
                 String profession,
                 Integer workExperience) {
        this.fullName = fullName != null ? fullName : "Неизвестен";
        this.age = age != null ? age : null;
        this.profession = profession != null ? profession : "Неизвестно";
        this.workExperience = workExperience != null ? workExperience : null;
    }

    // Конструктор без параметров
    public Human() {
        this(null, null, null, null);
    }

    // Конструктор с 3 параметрами (имя, возраст, профессия)
    public Human(String fullName, int age, String profession) {
        this(fullName, age, profession, null);
    }

    // Конструктор с 3 параметрами (имя, профессия, опыт)
    public Human(String fullName, String profession, int workExperience) {
        this(fullName, null, profession, workExperience);
    }

    // Конструктор с 2 параметрами (имя, возраст)
    public Human(String fullName, int age) {

        this(fullName, age, null, null);
    }

    // Конструктор с 2 параметрами (имя, профессия)
    public Human(String fullName, String profession) {

        this(fullName, null, profession, null);
    }

    // Конструктор с 1 параметром (имя)
    public Human(String fullName) {

        this(fullName, null, null, null);
    }

    // Геттеры

    public String getFullName() {
        return fullName;
    }

    public Integer getAge() {
        return age;
    }

    public String getProfession() {
        return profession;
    }

    public Integer getWorkExperience() {
        return workExperience;
    }

    // Сеттеры

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setProfession(String profession) {
        this.profession = profession;
    }

    public void setWorkExperience(Integer workExperience) {
        this.workExperience = workExperience;
    }

    // Методы

    // Метод для проверки может ли человек работать
    public boolean canWork(){
        return age >= 18;
    }

    public boolean canWork(String specificProfession){
        return age >= 18 && specificProfession.equals(profession);
    }

    public boolean canWork(int minAge){
        return age >= minAge;
    }

    public boolean canWork(String specificProfession, int minAge){
        return age >= minAge && specificProfession.equals(profession);
    }

    // Получение информации
    public String getInfo(){
        return fullName + " - (" + age + ")";
    }

    public String getInfo(boolean includeProfession){
        if (includeProfession){
            return fullName + " - (" + age + ") - " + profession;
        }
        return getInfo();
    }

    @Override
    public String toString() {
        return "{" +
                "fullName='" + fullName + '\'' +
                ", age=" + age +
                ", profession='" + profession + '\'' +
                ", workExperience=" + workExperience +
                '}';
    }
}
