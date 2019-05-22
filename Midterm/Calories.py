# Item Calories
# Calculate Calories from Fat and Carbohydrates

# Define integer variables
fat_gm = 0
carb_gm = 0
fat_cal = 0
carb_cal = 0
total_cal = 0


# Get fat and carbohydrate grams consumed
fat_gm = int(input("\nEnter Fat Grams: "))
carb_gm = int(input("Enter Carbohydrate Grams: "))

# Calculate calories consumed
fat_cal = fat_gm * 9
carb_cal = carb_gm * 4
total_cal = fat_cal + carb_cal

# Display calories from fat and carbohydrates
print("\nFat Calories:", format(fat_cal, ','))
print("Carbohydrate Calories:", format(carb_cal, ','))
print("Total Calories Consumed:", format(total_cal, ','))
