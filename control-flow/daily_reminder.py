# daily_reminder.py

# Prompt for a single task description
task = input("Enter a task description")

# Loop until a valid priority is given
while true:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Please enter a valid priority: high, medium, or low.")

    
# Loop until a valid time-bound answer is given
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Please answer with 'yes' or 'no'.")


# Construct the base message
message = f"Reminder: '{task}' is a {priority} priority task"



# Add time-sensitivity message
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += ". Consider completing it when you have free time."
else:
    message += "."



# Print final reminder
print("\n" + message)
