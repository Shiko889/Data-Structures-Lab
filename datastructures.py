def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return 

# Test case for get_names
spicy_foods = [
    {"name": "Spicy Chicken Curry", "cuisine": "Indian", "heat_level": 8},
    {"name": "Sichuan Hot Pot", "cuisine": "Chinese", "heat_level": 9},
    {"name": "Kimchi Jjigae", "cuisine": "Korean", "heat_level": 7}
]
print(get_names(spicy_foods))
# Output: ['Spicy Chicken Curry', 'Sichuan Hot Pot', 'Kimchi Jjigae']

# Test case for get_spiciest_foods
print(get_spiciest_foods(spicy_foods))
# Output: [{'name': 'Spicy Chicken Curry', 'cuisine': 'Indian', 'heat_level': 8},
#           {'name': 'Sichuan Hot Pot', 'cuisine': 'Chinese', 'heat_level': 9}]

# Test case for print_spicy_foods (no output since it's a print function)

# Test case for get_spicy_food_by_cuisine
print(get_spicy_food_by_cuisine(spicy_foods, "Chinese"))
# Output: {'name': 'Sichuan Hot Pot', 'cuisine': 'Chinese', 'heat_level': 9}

# Test case for print_spiciest_foods (no output since it's a print function)

# Test case for get_average_heat_level
print(get_average_heat_level(spicy_foods))
# Output: 8

# Test case for create_spicy_food
new_food = {"name": "Vindaloo", "cuisine": "Indian", "heat_level": 10}
create_spicy_food(spicy_foods, new_food)
print(get_names(spicy_foods))
# Output: ['Spicy Chicken Curry', 'Sichuan Hot Pot', 'Kimchi Jjigae', 'Vindaloo']
 