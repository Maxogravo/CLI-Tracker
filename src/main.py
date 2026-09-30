import habits
import os
import time
import dashboard

action = ""
commands = {
    "add habit": habits.addhabit,
    "log habit": habits.loghabit,
    "log previous habit": habits.logprevhabit
}

while(action != "exit"):
    os.system('cls' if os.name == 'nt' else 'clear')
    dashboard.draw_dash()
    action = input("Enter action (help for list of commands): ")
    try:
        commands[action.lower()]()
    except Exception as e:
        if action != "exit":
            print(f"Error: {e}")
        else:
            print("Goodbye!")
    time.sleep(0.5)
