# Spicy Foods Functions

This Python module provides functions for working with a list of spicy foods.

## Functions

### `get_names(spicy_foods)`

Returns a list of names of each spicy food in the given list of dictionaries.

### `get_spiciest_foods(spicy_foods)`

Returns a list of dictionaries representing the spiciest foods (those with a heat level greater than 5) from the given list.

### `print_spicy_foods(spicy_foods)`

Prints the name, cuisine, and heat level of each spicy food in the given list.

### `get_spicy_food_by_cuisine(spicy_foods, cuisine)`

Returns the first spicy food from the list that matches the given cuisine.

### `print_spiciest_foods(spicy_foods)`

Prints the spiciest foods (those with a heat level greater than 5) from the given list.

### `get_average_heat_level(spicy_foods)`

Calculates and returns the average heat level of all spicy foods in the given list.

### `create_spicy_food(spicy_foods, new_spicy_food)`

Appends a new spicy food to the given list of spicy foods.

## Example Usage

```python
# Define a list of spicy foods
spicy_foods = [
    {"name": "Spicy Chicken Curry", "cuisine": "Indian", "heat_level": 8},
    {"name": "Sichuan Hot Pot", "cuisine": "Chinese", "heat_level": 9},
    {"name": "Kimchi Jjigae", "cuisine": "Korean", "heat_level": 7}
]

# Test get_names function
print(get_names(spicy_foods))
# Output: ['Spicy Chicken Curry', 'Sichuan Hot Pot', 'Kimchi Jjigae']

# Test get_spiciest_foods function
print(get_spiciest_foods(spicy_foods))
# Output: [{'name': 'Spicy Chicken Curry', 'cuisine': 'Indian', 'heat_level': 8},
#           {'name': 'Sichuan Hot Pot', 'cuisine': 'Chinese', 'heat_level': 9}]

# Test get_spicy_food_by_cuisine function
print(get_spicy_food_by_cuisine(spicy_foods, "Chinese"))
# Output: {'name': 'Sichuan Hot Pot', 'cuisine': 'Chinese', 'heat_level': 9}

# Test get_average_heat_level function
print(get_average_heat_level(spicy_foods))
# Output: 8

# Test create_spicy_food function
new_food = {"name": "Vindaloo", "cuisine": "Indian", "heat_level": 10}
create_spicy_food(spicy_foods, new_food)
print(get_names(spicy_foods))
# Output: ['Spicy Chicken Curry', 'Sichuan Hot Pot', 'Kimchi Jjigae', 'Vindaloo']
