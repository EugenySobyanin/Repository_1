import os
from PyPDF2 import PdfReader, PdfWriter

# Параметры
template_path = './141.pdf'  # Путь к шаблону
source_folder = './new/'  # Папка с PDF-файлами
output_folder = './output/'  # Папка для сохранения результатов

# Номера страниц для замены (пример: заменим страницы 1 и 2 в шаблоне)
pages_to_replace = [0, 1, 5]  # Индексы страниц (0 - первая страница)

# Чтение шаблона
with open(template_path, 'rb') as template_file:
    template_reader = PdfReader(template_file)
    writer = PdfWriter()
    
    # Проход по всем PDF-файлам в папке
    for filename in os.listdir(source_folder):
        if filename.endswith('.pdf'):
            source_path = os.path.join(source_folder, filename)
            with open(source_path, 'rb') as source_file:
                source_reader = PdfReader(source_file)
                
                # Заменяем страницы
                for i, page_index in enumerate(pages_to_replace):
                    # Убедитесь, что в источнике достаточно страниц
                    if i < len(source_reader.pages):
                        # Добавляем страницу из источника в writer на место заменяемой
                        writer.add_page(source_reader.pages[i])
                    else:
                        print(f"Недостаточно страниц в файле {filename} для замены.")

                # Добавляем оставшиеся страницы из шаблона
                for j in range(len(template_reader.pages)):
                    if j not in pages_to_replace:
                        writer.add_page(template_reader.pages[j])

            # Сохраняем новый файл
            output_file_path = os.path.join(output_folder, f'output_{filename}')
            with open(output_file_path, 'wb') as output_file:
                writer.write(output_file)

print("Готово! Файлы успешно созданы.")
