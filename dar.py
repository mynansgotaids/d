camps = { 

    "Cultural immersion": {"days": 5, "difficulty": "easy", "cost": 800}, 

    "Kayaking and pancakes": {"days": 3, "difficulty": "moderate", "cost": 400}, 

    "Mountain biking": {"days": 4, "difficulty": "difficult", "cost": 900} 

} 

 

TRANSPORT_COST = 80 

 

def get_camp_details(): 

    """Gets camp details from the user, including age validation and transport option.""" 

    print("Welcome to the School Holiday Camp Registration!") 

 

     

    camper_age = 0 

    while not (5 <= camper_age <= 17): 

        try: 

            age_input = input("Please enter the camper's age (5-17): ") 

            camper_age = int(age_input) 

            if not (5 <= camper_age <= 17): 

                print("Invalid age. Campers must be between 5 and 17 years old.") 

        except ValueError: 

            print("Invalid input. Please enter a number for the age.") 

 

     

    camper_name = input("Please enter the camper's name: ") 

 

 

    num_days = input("Please enter the number of days attending: ") 

 

     

    print("\nAvailable Camps:") 

    for camp_name, details in camps.items(): 

        print(f"- {camp_name} ({details['days']} days, Difficulty: {details['difficulty']}, Cost: ${details['cost']})") 

 

     

    chosen_camp = "" 

    while chosen_camp not in camps: 

        chosen_camp = input("Please enter the name of the chosen camp: ") 

        if chosen_camp not in camps: 

            print("Invalid camp name. Please choose from the list.") 

 

     

    meal_choice = input("Please enter the meal choice (e.g., Standard, Vegetarian, Vegan): ") 

 

     

    transport_needed_input = input(f"Is transport needed? (yes/no, additional ${TRANSPORT_COST}): ").lower() 

    transport_needed = transport_needed_input == 'yes' 

 

     

    attending_input = input("Are they attending? (yes/no): ").lower() 

    is_attending = attending_input == 'yes' 

 

     

    total_cost = camps[chosen_camp]["cost"] 

    if transport_needed: 

        total_cost += TRANSPORT_COST 

 

     

    difficulty_level = camps[chosen_camp]["difficulty"] 

 