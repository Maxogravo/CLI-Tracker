import datetime

current_time = datetime.datetime.now()
habits ={
    "Example":[2,5,9,12,14,15,16,21,28,31]
}

def addhabit():
    name = input("Enter habit name: ")
    habits[name] = []
    print(f"{name} added as a habit.")

def loghabit():
    name = input("Enter habit to log: ")
    habits[name] += [current_time.day]
    print("logged")

def logprevhabit():
    name = input("Enter habit to log: ")
    if name in habits:
        datelist = input("Enter Dates To Log: ")
        dates = datelist.split()
        for x in dates:
            habits[name].append(int(x))
        print("Logged")
    else:
        print("Invalid Habit")
