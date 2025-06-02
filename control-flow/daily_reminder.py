task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high"| "medium" | "low":
        if time == "yes":
          print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
             print(f"Reminder: '{task}' is a {priority} priority task. Please make sure to complete it.")
    
    case _:
        print("Invalid input for priority! Please enter high, medium, or low. ")

