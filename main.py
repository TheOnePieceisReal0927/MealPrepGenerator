import random

greeting = "Hello, would you like a Meal Prep Plan for the Week? "
response = "Great! Here's your meal prep plan:"
Answer = input(greeting)

if Answer.lower() in ["yes", "sure"]:
    print(response and Meal_plan)

else:
    print("Okay, no problem.")

def generate_meal_plan():
    protein_index = random.randint(0, 6)

    if protein_index == 0:
        print("Protein: Chicken")
    if protein_index == 1:
        print("Protein: Ground Turkey")
    if protein_index == 2:
        print("Protein: Salmon")
    if protein_index == 3:
        print("Protein: Pork Chops")
    if protein_index == 4:
        print("Protein: Steak")
    if protein_index == 5:
        print("Protein: Shrimp")
    if protein_index == 6:
        print("Protein: Ground Beef")

    seasoning_blend = random.randint(0, 8)

    if seasoning_blend == 0:
        print("Spice Blend: Taco Seasoning")
    if seasoning_blend == 1:
        print("Spice Blend: Italian Seasoning")
    if seasoning_blend == 2:
        print("Spice Blend: Garam Masala")
    if seasoning_blend == 3:
        print("Spice Blend: Jerk Seasoning")
    if seasoning_blend == 4:
        print("Spice Blend: Fajita Seasoning")
    if seasoning_blend == 5:
        print("Spice Blend: Adobo Seasoning")
    if seasoning_blend == 6:
        print("Spice Blend: Dukkah")
    if seasoning_blend == 7:
        print("Spice Blend: Homemade Sazón Seasoning")
    if seasoning_blend == 8:
        print("Spice Blend: Za'atar")

    form_factor = random.randint(0, 5)

    if form_factor == 0:
        print("Served As: Sandwich")
    if form_factor == 1:
        print("Served As: Casserole")
    if form_factor == 2:
        print("Served As: Pasta")
    if form_factor == 3:
        print("Served As: Salad")
    if form_factor == 4:
        print("Served As: Soup")
    if form_factor == 5:
        print("Served with: Rice")

    side_vegetable = random.randint(0, 5)

    if side_vegetable == 0:
        print("Side Veggie: Roasted Broccoli")
    if side_vegetable == 1:
        print("Side Veggie: Sauted Squash")
    if side_vegetable == 2:
        print("Side Veggie: Fried Eggplant")
    if side_vegetable == 3:
        print("Side Veggie: Fried Green tomatoes")
    if side_vegetable == 4:
        print("Side Veggie: Balsamic Brussel Sprouts")
    if side_vegetable == 5:
        print("Side Veggie: Roasted Asparagus")

Meal_plan = generate_meal_plan()


second_response = "Would you like another option? "
second_answer = input(second_response)
third_response = "Great! Here's another meal prep plan you might like!:"

print(input(second_response))

if second_answer.lower ["yes", "sure", "why not"]:
    print(third_response)

else:
    print("Okay, no problem.")

    protein_index = random.randint(0, 6)

    if protein_index == 0:
        print("Protein: Chicken")
    if protein_index == 1:
        print("Protein: Ground Turkey")
    if protein_index == 2:
        print("Protein: Salmon")
    if protein_index == 3:
        print("Protein: Pork Chops")
    if protein_index == 4:
        print("Protein: Steak")
    if protein_index == 5:
        print("Protein: Shrimp")
    if protein_index == 6:
        print("Protein: Ground Beef")

    seasoning_blend = random.randint(0, 8)

    if seasoning_blend == 0:
        print("Spice Blend: Taco Seasoning")
    if seasoning_blend == 1:
        print("Spice Blend: Italian Seasoning")
    if seasoning_blend == 2:
        print("Spice Blend: Garam Masala")
    if seasoning_blend == 3:
        print("Spice Blend: Jerk Seasoning")
    if seasoning_blend == 4:
        print("Spice Blend: Fajita Seasoning")
    if seasoning_blend == 5:
        print("Spice Blend: Adobo Seasoning")
    if seasoning_blend == 6:
        print("Spice Blend: Dukkah")
    if seasoning_blend == 7:
        print("Spice Blend: Homemade Sazón Seasoning")
    if seasoning_blend == 8:
        print("Spice Blend: Za'atar")

    form_factor = random.randint(0, 5)

    if form_factor == 0:
        print("Served As: Sandwich")
    if form_factor == 1:
        print("Served As: Casserole")
    if form_factor == 2:
        print("Served As: Pasta")
    if form_factor == 3:
        print("Served As: Salad")
    if form_factor == 4:
        print("Served As: Soup")
    if form_factor == 5:
        print("Served with: Rice")

    side_vegetable = random.randint(0, 5)

    if side_vegetable == 0:
        print("Side Veggie: Roasted Broccoli")
    if side_vegetable == 1:
        print("Side Veggie: Sauted Squash")
    if side_vegetable == 2:
        print("Side Veggie: Fried Eggplant")
    if side_vegetable == 3:
        print("Side Veggie: Fried Green tomatoes")
    if side_vegetable == 4:
        print("Side Veggie: Balsamic Brussel Sprouts")
    if side_vegetable == 5:
        print("Side Veggie: Roasted Asparagus")