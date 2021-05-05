from datetime import date, timedelta, datetime

from utils import check_date


def add(args):
    if len(args) < 3:
        return print("at least one task")
    with open("checklist.txt", "a") as reader:
        task_date = check_date(args[3]) if len(args) > 3 else date.today()
        task_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        reader.write(f"{task_id},{args[2]},{task_date},n\n")
    return print("task added")