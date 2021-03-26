from datetime import date, timedelta, datetime

from utils import (
    query_done, query_date, check_date,
    print_tasks
)


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
        return print_tasks(query_date(date.today()).split("\n")[:-1])
    else:
        atributes = {
            "-d": list_with_date,
            "-w":list_last_week,
            "-lw":list_last_week,
        }
        return atributes.get(args[2], "wrong attribute. check help for help...")(args)
