import sys
from datetime import date, timedelta, datetime
print(datetime.now().strftime("%Y%m%d%H%M%S%f"))


def check_date(inp):
    splited = inp.split('-')
    if len(splited) == 1:
        task_date = date.today() + timedelta(days=int(splited[0]))
    elif len(splited) == 2:
        if "" in splited:
            task_date = date.today() + timedelta(days=-(int(splited[1])))
        else:
            task_date = date(year=date.today().year, month=splited[0], day=splited[1])
    elif len(splited) == 3:
        task_date = date(year=int(splited[0]), month=int(splited[1]), day=int(splited[2]))
    else:
        raise Exception("wrong type of date")
    return task_date


def add(args):
    if len(args) < 3:
        return print("at least one task")
    with open("checklist.txt", "a") as reader:
        task_date = check_date(args[3]) if len(args) > 3 else date.today()
        task_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        reader.write(f"{task_id},{args[2]},{task_date},n\n")
    return print("task added")


def query_date(task_date):
    result = ""
    with open("checklist.txt", "r") as lines:
        for line in lines:
            if line.split(",")[1] == str(task_date):
                result += line
    return result


def list_with_date(args):
    return print(query_date(check_date(args[3])), end="")


def list_last_week(args):
    base = date.today()
    total_tasks = ""
    for i in [base - timedelta(days=x) for x in range(7)]:
        total_tasks += query_date(i)
    return print(total_tasks, end="")


def lis(args):
    if len(args) == 2:
        return print(query_date(date.today()), end="")
    else:
        atributes = {
            "-d": list_with_date,
            "-w":list_last_week,
            "-lw":list_last_week,
        }
        return atributes.get(args[2], "wrong attribute. check help for help...")(args)
     

def query_done(bool):
    result = ""
    with open("checklist.txt", "r") as lines:
        for line in lines:
            if line.split(',')[3] == bool+"\n":
                result += line
    return result

def main(args):
    if len(args) < 2:
        return print("error of no atribute")
    functions = {
        "add": add,
        "list": lis,
    }
    return functions.get(args[1], "check help for help...")(args)
    

if __name__ == "__main__":
    print(query_done("n"))

    print(datetime.now())
    main(sys.argv)
