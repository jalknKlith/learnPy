import datetime

# Get today's date
today = datetime.date.today()

# Generate a symbol pattern based on the relation of numbers in the date
pattern = ""
for num in str(today):
    if int(num) % 2 == 0:
        pattern += "*"
    else:
        pattern += "#"

# Create a workout routine based on the symbol pattern
workout = {
    "*": "Push-ups",
    "#": "Squats"
}

# Print the workout routine
print("Workout Routine:")
for symbol in pattern:
    print(workout[symbol] + ": 10 reps")
