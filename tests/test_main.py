import os

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.csv_parser import parse_csv
from reports.payout_report import generate_payout_report


# Тестируем csv_parser
def test_parse_csv():
    test_file = 'tests/test_data.csv'
    with open(test_file, 'w') as f:
        f.write("id,email,name,department,hours_worked,rate\n")
        f.write("1,alice@example.com,Alice Johnson,Marketing,160,50\n")
        f.write("2,bob@example.com,Bob Smith,Design,150,40\n")

    data = parse_csv(test_file)
    # Должно быть две строки данных
    assert len(data) == 2  
    # Проверка значений в первой строке
    assert data[0]["name"] == "Alice Johnson"  
    # Проверка значений во второй строке
    assert data[1]["department"] == "Design"  
    assert data[1]["hours_worked"] == "150" 
    


# Тестируем payout_report
def test_generate_payout_report():
    rows = [
        {"id": "1", "name": "Alice Johnson", "email": "alice@example.com", "department": "Marketing", "hours_worked": "160", "rate": "50"},
        {"id": "2", "name": "Bob Smith", "email": "bob@example.com", "department": "Design", "hours_worked": "150", "rate": "40"}
    ]
    
    result = generate_payout_report(rows)
    
	# Должно быть два отчета
    assert len(result) == 2 
    # 160 * 50 = 8000 
    assert result[0]["payout"] == 8000
    # 150 * 40 = 6000
    assert result[1]["payout"] == 6000