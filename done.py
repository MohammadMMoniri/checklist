from datetime import date, timedelta, datetime
from utils import query_date, query_done, print_tasks


def print_ndone_tasks():
    ndone_tasks = query_done("n").split("\n")[:-1]
    x={}
    x = print_tasks(tasks=ndone_tasks, task_id_dict=x)
    return x


def done_one_task(task_with_id, task_num):
    task_id = task_with_id.get(int(task_num), None)
    with open("checklist.txt", "r") as task_file:
        lines = task_file.readlines()
        for num, line in enumerate(lines):
            if line.split(",")[0] == task_id:
                lines[num] = lines[num][:-2] + "d\n"
    with open("checklist.txt", "w") as task_file:
        task_file.writelines(lines)


def done(args):
    if len(args) == 2:
        task_with_id = print_ndone_tasks()
        task_num = input("please enter target task id:")
        if len(task_num) == 1:
            done_one_task(task_with_id, task_num)
        else:
            pass
