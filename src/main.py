import habits
import os
import time
from rich.console import Console
import datetime
import calendar

year = datetime.datetime.now().year
month = datetime.datetime.now().month
days = calendar.monthrange(year, month)[1]
console = Console()
action = ""
commands = {
    "add habit": habits.addhabit,
    "log habit": habits.loghabit
}

def draw_dash():
    console.print(datetime.datetime.now().strftime("%B"), style="bold cyan")
    for x in habits.habits:
        line = f"{x}: |"
        for y in range(days):
            if y in habits.habits[x]:
                line += "x"
            else:
                line += "-"
        line += f"| {len(habits.habits[x])} / {days}"
        console.print(line, style="bold green")

while(action != "exit"):
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_dash()
    action = input("Enter action (help for list of commands): ")
    try:
        commands[action.lower()]()
    except:
        if action != "exit":
            print("Invalid")
        else:
            print("Goodbye!")
    time.sleep(0.5)
