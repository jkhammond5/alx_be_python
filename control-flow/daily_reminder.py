# daily_reminder.py

# Prompt for a single task description
task = input("Enter your task: ")

# Loop until a valid priority is given
while True:
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

# Provide the reminder using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"

# Add time-sensitivity if applicable
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority == "low":
        message += ". Consider completing it when you have free time."
    else:
        message += " but it can be scheduled appropriately."

# Print the final message
print("\n" + message)
