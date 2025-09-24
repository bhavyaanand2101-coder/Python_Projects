# Daily Calorie Tracker
# Author: [Bhavya Anand]
# Date: 24/09/2025

import datetime  # For timestamp in bonus task

def main():
    # Task 1: Welcome Message
    print("Welcome to the Daily Calorie Tracker!")
    print("This tool helps you log your meals for the day, calculate your total and average calorie intake,")
    print("and compare it against your daily calorie limit. Let's get started!\n")

    # Task 2: Input & Data Collection
    try:
        num_meals = int(input("How many meals do you want to enter? "))
        if num_meals <= 0:
            print("Please enter a positive number of meals.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    meals = []
    calories = []

    for i in range(num_meals):
        meal_name = input(f"Enter the name of meal {i+1}: ").strip()
        if not meal_name:
            meal_name = f"Meal {i+1}"  # Default if empty
        meals.append(meal_name)
        
        try:
            cal = int(input(f"Enter the calories for {meal_name}: "))
            if cal < 0:
                print("Calories cannot be negative. Setting to 0.")
                cal = 0
            calories.append(cal)
        except ValueError:
            print("Invalid calorie input. Skipping this meal.")
            continue  # Skip if invalid

    if not calories:  # If no valid meals entered
        print("No valid meals entered. Exiting.")
        return

    # Task 3: Calorie Calculations
    total_calories = sum(calories)
    average_calories = total_calories / len(calories)

    try:
        daily_limit = int(input("Enter your daily calorie limit: "))
        if daily_limit <= 0:
            print("Daily limit must be positive. Using 2000 as default.")
            daily_limit = 2000
    except ValueError:
        print("Invalid limit. Using 2000 as default.")
        daily_limit = 2000

    # Task 4: Exceed Limit Warning System
    if total_calories > daily_limit:
        status = "WARNING: You have exceeded your daily calorie limit!"
    else:
        status = "Success: You are within your daily calorie limit!"

    # Task 5: Neatly Formatted Output
    print("\n" + "="*40)
    print("DAILY CALORIE SUMMARY")
    print("="*40)
    print("Meal Name\tCalories")
    print("-" * 40)
    for meal, cal in zip(meals, calories):
        print(f"{meal}\t\t{cal}")
    print("-" * 40)
    print(f"Total:\t\t{total_calories}")
    print(f"Average:\t{average_calories:.2f}")
    print(f"Daily Limit:\t{daily_limit}")
    print(status)
    print("="*40)

    # Task 6 (Bonus): Save Session Log to File
    save_choice = input("\nDo you want to save this report to a file? (y/n): ").strip().lower()
    if save_choice == 'y' or save_choice == 'yes':
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = "calorie_log.txt"
        
        with open(filename, "w") as file:
            file.write(f"Daily Calorie Tracker Session Log\n")
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"Daily Limit: {daily_limit}\n\n")
            file.write("Meal Name\tCalories\n")
            file.write("-" * 40 + "\n")
            for meal, cal in zip(meals, calories):
                file.write(f"{meal}\t\t{cal}\n")
            file.write("-" * 40 + "\n")
            file.write(f"Total Calories: {total_calories}\n")
            file.write(f"Average Calories: {average_calories:.2f}\n")
            file.write(f"Status: {status}\n")
        
        print(f"Report saved to {filename}")

if __name__ == "__main__":
    main()
