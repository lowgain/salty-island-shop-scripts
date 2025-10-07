import sys
import csv
import datetime
import logging


def main():
    if not sys.argv[1].endswith(".csv"):
        raise TypeError("File MUST be a CSV")
    input_file = csv.DictReader(open(sys.argv[1], "r", newline=""), delimiter=",")
    print("Press Enter to move to a newline")
    print(f"| {'Date':<17}|{'Gross sales':>12} |")
    for item in input_file:
        input(f"| {item['Date']:<17}|{'$' + item['Gross sales']:>12} |")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger = logging.getLogger(__name__)
        logging.basicConfig(
            filename=f"{datetime.datetime.now()}.log",
            encoding="utf-8",
            level=logging.DEBUG,
        )
        print(e)
        logger.exception(e)
