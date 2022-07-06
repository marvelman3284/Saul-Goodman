import random
from rich.prompt import Confirm


def get_random_line(file: str) -> str:
    line_num = 0
    selected = ""
    with open(file) as f:
        while 1:
            line = f.readline()
            if not line:
                break
            line_num += 1
            if random.uniform(0, line_num) < 1:
                selected = line

    return selected


def main():

    quote = Confirm.ask("Do you want to hear a Saul Goodman quote?")

    while quote:
        line = get_random_line("data/quotes.txt")

        print(f"Saul Goodman Once Said: {line}")

        quote = Confirm.ask("Do you want to hear another Saul Goodman quote?")

        if not quote:
            break



if __name__ == "__main__":
    main()
