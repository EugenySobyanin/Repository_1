import pandas as pd

from constants import TABLE_DATA_PATH, TABLE_NEW_PATH


def update_table_a_with_b(table_a_path, table_b_path):
    """
    Обновляет таблицу A данными из таблицы B по совпадающим КБК
    Таблица A изменяется напрямую
    """
    # 1. Загрузка таблиц
    df_a = pd.read_excel(table_a_path)
    df_b = pd.read_excel(table_b_path)
    
    # 2. Определение колонок
    kbk_columns = ['цст', 'КВР', 'КОСГУ', 'Рег.класс', 'доп.код']
    
    # Предположим, финансовые колонки называются так:
    # В таблице A: ['Лимит_A', 'БО_A', 'Остаток_A']
    # В таблице B: ['Лимит_B', 'БО_B', 'Остаток_B']
    financial_columns_a = ['Лимиты бюджетных обязательств на 2025', 'Бюджетные обязательства на 2025', 'Предварительные заявки на 2025', 'Другое_A', 'Еще_A']
    financial_columns_b = ['Лимит_B', 'БО_B', 'Остаток_B', 'Другое_B', 'Еще_B']
    
    # 3. Создание словаря для сопоставления колонок
    column_mapping = dict(zip(financial_columns_b, financial_columns_a))
    
    # 4. Объединение таблиц по ключевым полям КБК
    merged = pd.merge(
        df_a, 
        df_b, 
        on=kbk_columns, 
        how='left', 
        suffixes=('_a', '_b')
    )
    
    # 5. Обновление данных в таблице A
    total_changes = 0
    for col_b, col_a in column_mapping.items():
        # Создаем маску для строк, где данные отличаются
        mask = (merged[col_a] != merged[col_b]) & (~merged[col_b].isna())
        
        # Обновляем значения в таблице A
        changes_count = mask.sum()
        if changes_count > 0:
            df_a.loc[mask, col_a] = merged.loc[mask, col_b]
            print(f"Обновлено {changes_count} значений в столбце {col_a}")
            total_changes += changes_count
    
    # 6. Перезаписываем исходную таблицу A
    df_a.to_excel(table_a_path, index=False)
    print(f"Таблица A обновлена. Всего изменений: {total_changes}")
    
    return df_a


# Пример использования
if __name__ == "__main__":
    updated_df = update_table_a_with_b(
        table_a_path=TABLE_DATA_PATH,
        table_b_path=TABLE_NEW_PATH
    )