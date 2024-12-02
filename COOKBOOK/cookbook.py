from pprint import pprint
def load_cook_book(file_path):
    cook_book = {}  
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline().strip() 
            if not line:
                break  

            recipe_name = line 
            cook_book[recipe_name] = []  

            num_ingredients = int(file.readline().strip()) 
            for _ in range(num_ingredients):
                ingredient_line = file.readline().strip() 
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                
                cook_book[recipe_name].append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            file.readline()  
    
    return cook_book  
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}  
    
    for dish in dishes:  
        if dish in cook_book: 
            for ingredient in cook_book[dish]:  
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count  
                measure = ingredient['measure']
                
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'quantity': quantity, 'measure': measure}
        else:
            print(f"Блюдо '{dish}' отсутствует в книге рецептов.")
    
    return shop_list  




file_path = 'COOKBOOK/recipes.txt'  
cook_book = load_cook_book(file_path)
pprint(cook_book)

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shopping_list = get_shop_list_by_dishes(dishes, person_count, cook_book)

for ingredient, details in shopping_list.items():
    pprint(f"{ingredient}: {details['quantity']} {details['measure']}")