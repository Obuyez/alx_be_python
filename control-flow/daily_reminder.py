task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please make sure to complete it.")
    
    case "medium":
        if time == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Please make sure to complete it.")

    case "low":
        if time == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task. Please make sure to complete it.")

    case _:
        print("Invalid input for priority! Please enter high, medium, or low.")

