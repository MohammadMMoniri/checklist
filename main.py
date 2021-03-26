import sys
from datetime import date, timedelta, datetime

from lis import lis
from add import add
from done import done


def main(args):
    if len(args) < 2:
        return print("error of no atribute")
    functions = {
        "add": add,
        "list": lis,
        "done": done,
    }
    return functions.get(args[1], "check help for help...")(args)
    

if __name__ == "__main__":
    main(sys.argv)
