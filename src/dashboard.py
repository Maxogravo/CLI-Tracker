import habits
from rich.console import Console
import datetime
import calendar

year = datetime.datetime.now().year
month = datetime.datetime.now().month
days = calendar.monthrange(year, month)[1]
console = Console()

def draw_dash():
    # Month
    console.print(datetime.datetime.now().strftime("%B"), style="bold cyan")
    # heatmap
    for x in habits.habits:
        line = f"{x}: |"
        for y in range(days):
            if y+1 in habits.habits[x]:
                line += "x"
            else:
                line += "-"
        line += f"| {len(habits.habits[x])} / {days}"
        console.print(line, style="bold green")
