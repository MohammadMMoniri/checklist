from datetime import date, timedelta, datetime


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


def query_date(task_date):
    result = ""
    with open("checklist.txt", "r") as lines:
        for line in lines:
            if line.split(",")[1] == str(task_date):
                result += line
    return result


def query_done(bool):
    result = ""
    with open("checklist.txt", "r") as lines:
        for line in lines:
            if line.split(',')[3] == bool+"\n":
                result += line
    return result