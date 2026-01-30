import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;

public class Sailor extends Human {
    private static final String PROFESSION_TITLE = "Моряк";
    private static final String DEFAULT_RANK = "Матрос";
    private static final String DEFAULT_SHIP = "Не установлено";
    private static final Map<String, Integer> RANK_VALUES = Map.ofEntries(
            Map.entry("Матрос", 0),
            Map.entry("Старший матрос", 1),
            Map.entry("Старшина", 2),
            Map.entry("Главный старшина", 3),
            Map.entry("Мичман", 4),
            Map.entry("Старший мичман", 5),
            Map.entry("Младший лейтенант", 6),
            Map.entry("Лейтенант", 7),
            Map.entry("Старший лейтенант", 8),
            Map.entry("Капитан-лейтенант", 9),
            Map.entry("Капитан 3-го ранга", 10),
            Map.entry("Капитан 2-го ранга", 11),
            Map.entry("Капитан 1-го ранга", 12),
            Map.entry("Контр-адмирал", 13),
            Map.entry("Адмирал", 14),
            Map.entry("Адмирал флота", 15)
    );
    private String rank;
    private String shipTitle;
    private List<Sailor> subordinates;
    private Integer salary;

    // Основной конструктор
    public Sailor(
            String fullName,
            String rank,
            Integer age,
            Integer salary,
            Integer workExperience,
            String shipTitle,
            List<Sailor> subordinates
    ){
        super(fullName, age, PROFESSION_TITLE, workExperience);
        setRank(rank);
        this.salary = salary;
        this.shipTitle = shipTitle != null ? shipTitle : "Не установлено";
        this.subordinates = subordinates != null ? subordinates : new ArrayList<>();
    }

    // Конструктор без подчиненных
    public Sailor(
            String fullName,
            String rank,
            Integer age,
            Integer salary,
            Integer workExperience,
            String shipTitle
    ){
        this(fullName, rank, age, salary, workExperience, shipTitle, null);
    }

    // Конструктор (имя, звание, возраст, опыт, название корабля)
    public Sailor(
            String fullName,
            String rank,
            Integer age,
            Integer workExperience,
            String shipTitle
    ){
        this(fullName, rank, age, null, workExperience, shipTitle);
    }

    // Конструктор (имя, звание, название корабля)
    public Sailor(
            String fullname,
            String rank,
            String shipTitle
    ){
        this(fullname, rank, null, null, shipTitle);
    }

    // Конструктор (имя, возраст, название корабля)
    public Sailor(
            String fullName,
            Integer age,
            String shipTitle
    ){
        this(fullName, DEFAULT_RANK, age, null, null, shipTitle);
    }

    // Конструктор (имя, возраст)
    public Sailor(String fullname, Integer age){
        this(fullname, age, DEFAULT_SHIP);
    }

    // Конструктор по умолчанию
    public Sailor() {
        this(null, DEFAULT_RANK, null, null,
                null, DEFAULT_SHIP, null);
    }

    // Геттеры

    @Override
    public String getProfession(){
        return PROFESSION_TITLE;
    }

    public String getRank() {
        return rank;
    }

    public String getShipTitle() {
        return shipTitle;
    }

    public List<Sailor> getSubordinates() {
        return new ArrayList<>(subordinates);
    }

    public Integer getSalary() {
        return salary;
    }

    // Сеттеры

    public void setRank(String rank) {
        if (rank == null || rank.trim().isEmpty()) {
            this.rank = DEFAULT_RANK;
        } else if (rankIsCorrect(rank)) {
            this.rank = rank;
        } else {
            System.out.println("Предупреждение: '" + rank + "' не является корректным званием.");
            System.out.println("Установлено звание по умолчанию: " + DEFAULT_RANK);
            System.out.println("Доступные звания:");
            printAvailableRanks();
            this.rank = DEFAULT_RANK;
        }
    }

    public void setShipTitle(String shipTitle) {
        this.shipTitle = shipTitle;
    }

    public void setSubordinates(List<Sailor> subordinates) {
        this.subordinates = subordinates;
    }

    public void setSalary(Integer salary) {
        this.salary = salary;
    }

    @Override
    public void setProfession(String profession) {
        throw new UnsupportedOperationException(
                "Нельзя изменить профессию. Профессия фиксирована: Моряк"
        );
    }

    // Методы

    // Метод проверяет допустимое ла передано звание
    private static Boolean rankIsCorrect(String rank){
        return rank != null && RANK_VALUES.containsKey(rank.trim());
    }

    // Вывод доступных званий
    private static void printAvailableRanks() {
        for (String rank : RANK_VALUES.keySet()) {
            System.out.println("  - " + rank);
        }
    }

    // Сравнение званий (текущий моряк ниже по званию?)
    public boolean isRankLowerThan(Sailor otherSailor) {
        if (this.rank == null || otherSailor.rank == null) {
            throw new IllegalStateException("У одного из моряков не установлено звание.");
        }

        Integer thisRankValue = RANK_VALUES.get(this.rank);
        Integer otherRankValue = RANK_VALUES.get(otherSailor.rank);

        if (thisRankValue == null || otherRankValue == null) {
            throw new IllegalStateException("Некорректное звание у одного из моряков");
        }

        return thisRankValue <= otherRankValue;
    }

    // Добавление нового подчиненного
    public boolean addSubordinate(Sailor newSailor) {
        if (newSailor == this) {
            System.out.println("Нельзя находиться у себя в подчинении.");
            return false;
        }

        if (this.isRankLowerThan(newSailor)) {
            System.out.println("Нельзя добавить в подчинение старшего или равного по званию.");
            return false;
        }

        if (subordinates.contains(newSailor)) {
            System.out.println("Моряк уже является подчиненным.");
            return false;
        }

        subordinates.add(newSailor);
        return true;
    }

    // Для добавления нескольких моряков
    public boolean addSubordinate(Sailor... sailors) {
        boolean allAdded = true;
        for (Sailor sailor : sailors) {
            if (!addSubordinate(sailor)) {
                allAdded = false;
            }
        }
        return allAdded;
    }

    // Для коллекции
    public boolean addSubordinate(Collection<Sailor> sailors) {
        boolean allAdded = true;
        for (Sailor sailor : sailors) {
            if (!addSubordinate(sailor)) {
                allAdded = false;
            }
        }
        return allAdded;
    }

    // Вывод информации о подчиненных
    public void printSubordinatesInfo(){
        if (subordinates.size() > 0){
            for(int i = 0; i < subordinates.size(); i++){
                System.out.println(i + 1 + ". " + subordinates.get(i));
            }
            return;
        }
        System.out.println("Нет подчиненных.");
    }

    @Override
    public String toString(){
        StringBuilder result = new StringBuilder();
        result.append(getFullName() != null ? "Имя: " + getFullName() : "");
        result.append(rank != null ? "; Звание: " + rank : "");
        result.append(getAge() != null ? "; Возраст: " + getAge() : "");
        result.append(shipTitle != null ? "; Корабль: " + shipTitle : "");
        result.append(getWorkExperience() != null ? "; Стаж: " + getWorkExperience() : "");

        return result.toString();
    }

    // Удалить подчиненного
    public Boolean deleteSubordinate(Sailor sailorForDelete){
        return subordinates.remove(sailorForDelete);
    }

    // Получить кол.во подчиненных
    public Integer getSubordinatesCount(){
        return subordinates.size();
    }
}
