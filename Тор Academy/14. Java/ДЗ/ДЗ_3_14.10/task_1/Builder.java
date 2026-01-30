public class Builder extends Human {
    private static final String PROFESSION_TITLE = "Строитель";
    private static final String NO_PROJECT_STATUS = "Не назначен";
    private static final String NO_SPECIALIZATION = "Не определена";

    private String constructionSpecialization;
    private String currentProject;

    // Основной конструктор со всеми параметрами
    public Builder(
            String fullName,
            Integer age,
            Integer workExperience,
            String constructionSpecialization,
            String currentProject
    ) {
        super(fullName, age, PROFESSION_TITLE, workExperience);
        this.constructionSpecialization = constructionSpecialization != null
                ? constructionSpecialization : NO_SPECIALIZATION;
        this.currentProject = currentProject != null
                ? currentProject : NO_PROJECT_STATUS;
    }

    // Конструктор с 4 параметрами (имя, возраст, опыт, специализация)
    public Builder(
            String fullname,
            Integer age,
            Integer workExperience,
            String constructionSpecialization
    ) {
        this(fullname, age, workExperience, constructionSpecialization, null);
    }

    // Конструктор с 3 параметрами (имя, возраст, опыт)
    public Builder(String fullname, Integer age, Integer workExperience) {
        this(fullname, age, workExperience, null);
    }

    // Конструктор с 2 параметрами (имя, специализация)
    public Builder(String fullname, String constructionSpecialization) {
        this(fullname, null, null, constructionSpecialization);
    }

    // Конструктор с 2 параметрами (имя, возраст)
    public Builder(String fullname, Integer age) {
        this(fullname, age, null);
    }

    // Конструктор без параметров
    public Builder() {
        this(null, null, null, null, null);
    }

    // Геттеры

    public String getConstructionSpecialization() {
        return constructionSpecialization;
    }

    public String getCurrentProject() {
        return currentProject;
    }

    // Сеттеры

    public void setConstructionSpecialization(String constructionSpecialization) {
        this.constructionSpecialization = constructionSpecialization;
    }

    public void setCurrentProject(String currentProject) {
        this.currentProject = currentProject;
    }

    @Override
    public void setProfession(String profession){
        throw new UnsupportedOperationException(
                "Нельзя изменить профессию для строителя. Профессия фиксирована: Строитель"
        );
    }

    // Методы

    @Override
    public String toString(){
        StringBuilder strBuilder = new StringBuilder(super.toString());
        if (this.onProject()){
            strBuilder.deleteCharAt(strBuilder.length() - 1);
            strBuilder.append(", currentProject=" + currentProject + "}");
        }
        return strBuilder.toString();
    }

    // Задействован ли строитель на проекте
    public Boolean onProject(){
        return !currentProject.equals(NO_PROJECT_STATUS);
    }

    // Закрытие проекта
    public String closeProject(){
        StringBuilder result = new StringBuilder();
        if (!this.onProject()){
            result.append("Рабочий не задействован на проекте.\n");
            return result.toString();
        }
        result.append("Рабочий " + getFullName() + " завершил проект " + currentProject + "\n");
        this.currentProject = NO_PROJECT_STATUS;
        return result.toString();
    }
}
