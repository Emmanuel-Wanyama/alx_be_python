# Prompt user for task of task

task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

# Prepare the base reminder message based on priority
base_reminder = ""
match priority:
    case "high":
        base_reminder = f"Your task: **{task}** is a high priority task"
    case "medium":
        base_reminder = f"Your task: **{task}** is a medium priority task"
    case "low":
        base_reminder = f"Your task: **{task}** is a low priority task"
    case _:
        # Default for unrecognized priority
        base_reminder = f"Your task: **{task}** has an unrecognized priority"

# Modify the reminder based on time sensitivity
reminder = ""
if time_bound == "yes":
    reminder = f"{base_reminder} requires immediate attention today!"
elif time_bound == "no":
    reminder = f"{base_reminder} does not require immediate attention today."
else:
    # Handles cases where time_bound is not 'yes' or 'no'
    reminder = f"{base_reminder}. (Time-bound status was not recognized)."

# Print the final combined reminder, starting with "Reminder: "
print(f"Reminder: {reminder}")

