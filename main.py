import random

def generate_meal_plan():
    protein_index = random.randint(0, 6)
    protein_options = ["Chicken", "Ground Turkey", "Salmon", "Pork Chops", "Steak", "Shrimp", "Ground Beef"]

    seasoning_blend = random.randint(0, 8)
    seasoning_options = ["Taco Seasoning", "Italian Seasoning", "Garam Masala", "Jerk Seasoning",
                         "Fajita Seasoning", "Adobo Seasoning", "Dukkah", "Homemade Sazón Seasoning", "Za'atar"]

    form_factor = random.randint(0, 5)
    form_factor_options = ["Sandwich", "Casserole", "Pasta", "Salad", "Soup", "Rice"]

    side_vegetable = random.randint(0, 5)
    side_vegetable_options = ["Roasted Broccoli", "Sautéed Squash", "Fried Eggplant",
                              "Fried Green tomatoes", "Balsamic Brussels Sprouts", "Roasted Asparagus"]

    meal_plan = {
        "Protein": protein_options[protein_index],
        "Spice Blend": seasoning_options[seasoning_blend],
        "Served As": form_factor_options[form_factor],
        "Side Veggie": side_vegetable_options[side_vegetable]
    }

    return meal_plan

greeting = "Hello, would you like a Meal Prep Plan for the Week? "
response = "Great! Here's your meal prep plan:"
answer = input(greeting)
second_response = "Would you like another option? "
third_response = "Great! Here's another meal prep plan you might like!:"

if answer.lower() in ["yes", "sure"]:
    print(response)
    meal = generate_meal_plan()
    for key, value in meal.items():
        print(f"{key}: {value}")
second_answer = input("Would you like another option? ")
if second_answer.lower() in ["yes", "sure"]:
    print(third_response)
    meal = generate_meal_plan()
    for key, value in meal.items():
        print(f"{key}: {value}")
