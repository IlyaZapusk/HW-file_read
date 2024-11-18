# Создаем пустой словарь для всех рецептов
cook_book = {}

# Открываем файл
with open('recipes.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Переменная для хранения текущего блюда
current_recipe = None

# Идем по всем строкам файла
i = 0
while i < len(lines):
    line = lines[i].strip()
    
    # Если строка содержит название рецепта
    if line.isalpha():
        current_recipe = line
        cook_book[current_recipe] = []  # Для каждого рецепта создаем пустой список для ингредиентов
        i += 1
        continue

    # Если строка содержит количество ингредиентов
    if line.isdigit():
        num_ingredients = int(line)
        for j in range(num_ingredients):
            i += 1
            ingredient_line = lines[i].strip()
            ingredient, quantity, unit = ingredient_line.split(' | ')
            # Добавляем ингредиент в список для текущего рецепта
            cook_book[current_recipe].append({
                'ingredient_name': ingredient,
                'quantity': float(quantity),
                'measure': unit
            })
    
    i += 1

# Выводим результат
for recipe, ingredients in cook_book.items():
    print(f"Рецепт: {recipe}")
    for ingredient in ingredients:
        print(f"  {ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}")
    print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}  # Словарь для хранения итогового списка покупок
    
    # Проходим по каждому блюду в списке dishes
    for dish in dishes:
        if dish in cook_book:  # Проверяем, есть ли такое блюдо в cook_book
            ingredients = cook_book[dish]  # Получаем список ингредиентов для текущего блюда
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count  # Умножаем на количество персон
                measure = ingredient['measure']
                
                # Если ингредиент уже есть в итоговом списке, добавляем к его количеству
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    # Добавляем новый ингредиент в список покупок
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
    
    return shop_list

# # Пример использования
# dishes = ['Омлет', 'Утка по-пекински']  # Список выбранных блюд
# person_count = 2  # Количество персон

shopping_list = get_shop_list_by_dishes(dishes, person_count)

# Выводим итоговый список покупок
for ingredient, details in shopping_list.items():
    print(f"{ingredient}: {details['quantity']} {details['measure']}")
