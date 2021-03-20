import sys
from datetime import date, timedelta


def check_date(inp):
    splited = inp.split('-')
    if len(splited) == 1:
        task_date = date.today() + timedelta(days=int(splited[0]))
    elif len(splited) == 2:
        task_date = date(year=date.today().year, month=splited[0], day=splited[1])
    elif len(splited) == 3:
        task_date = date(year=int(splited[0]), month=int(splited[1]), day=int(splited[2]))
    else:
        raise Exception("wrong type of date")
    return task_date


def add(args):
    if len(args) < 3:
        return print("at least one task")
    with open("chekclist.txt", "a") as reader:
        task_date = check_date(args[3]) if len(args) > 3 else date.today()
        reader.write(f"{args[2]},{task_date},n\n")
    return print("task added")


def main(args=None):
    if len(args) < 2:
        return print("error of no atribute")
    functions = {
        "-a": add(args),
    }
    return functions.get(args[1])


if __name__ == "__main__":
    main(sys.argv)
