import os

def merge_files(file_names, output_file):
    # Список для хранения данных файлов
    file_data = []
    
    # Чтение файлов и сбор информации
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_data.append((file_name, len(lines), lines))  # (имя файла, количество строк, содержимое)
    
    # Сортировка файлов по количеству строк
    file_data.sort(key=lambda x: x[1])  # Сортируем по количеству строк
    
    # Запись в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name, line_count, lines in file_data:
            output.write(f"{file_name}\n")  # Имя файла
            output.write(f"{line_count}\n")  # Количество строк
            output.writelines(lines)  # Содержимое файла

# Пример использования
file_names = ['MERGE/1.txt', 'MERGE/2.txt']  # Список имен файлов
output_file = 'merged.txt'  # Имя итогового файла

merge_files(file_names, output_file)
