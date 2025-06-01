# Prompt user for description of task

description = input("Task description? ")
task_priority = input("Task priority? (high/medium/low): ").lower()
time_bound = input("Is the task time bound (yes/no)? ").lower()

# Prepare the base reminder message based on priority
base_reminder = ""
match task_priority:
    case "high":
        base_reminder = f"Your task: **{description}** is a high priority task"
    case "medium":
        base_reminder = f"Your task: **{description}** is a medium priority task"
    case "low":
        base_reminder = f"Your task: **{description}** is a low priority task"
    case _:
        # Default for unrecognized priority
        base_reminder = f"Your task: **{description}** has an unrecognized priority"

# Modify the reminder based on time sensitivity
final_reminder = ""
if time_bound == "yes":
    final_reminder = f"{base_reminder} requires immediate attention today!"
elif time_bound == "no": # Changed 'No' to 'no' for consistency with .lower()
    final_reminder = f"{base_reminder} does not require immediate attention today." # Closes the sentence if not time-bound
else:
    # Handles cases where time_bound is not 'yes' or 'no'
    final_reminder = f"{base_reminder}. (Time-bound status was not recognized)."

# Print the final combined reminder
print(final_reminder)