import argparse
import json
import os
from utils.csv_parser import parse_csv
from reports.payout_report import generate_payout_report


def main():
    # -h --help
    parser = argparse.ArgumentParser(description="Salary report generator") 
    # передаем тип, говорим что можно несколько файлов, и справка
    parser.add_argument("files", nargs="+", help="CSV files with employee data")
    # создаем обязательную команду, ограничиваем ее по payout, и справка
    parser.add_argument("--report", required=True, choices=["payout"], help="Type of report to generate")

    args = parser.parse_args()

    all_rows = []
    # перебираем все переданные файлы
    for file_path in args.files:
        # проверка на наличе файла
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        # получаем данные и пишем их в переменную
        rows = parse_csv(file_path)
        all_rows.extend(rows)

	# проверка на запрос
    if args.report == "payout":
        # создаем payout
        result = generate_payout_report(all_rows)
    else:
        print(f"Unsupported report type: {args.report}")
        return

	# Конвертируем в json
    print(json.dumps(result, indent=4))

# Проверка запуска файла
if __name__ == "__main__":
    main()
