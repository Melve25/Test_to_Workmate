from typing import List, Dict

RATE_COLUMNS = {"hourly_rate", "rate", "salary"}

def normalize_row(row: Dict[str, str]) -> Dict[str, str]:
    # копируем строку
    new_row = row.copy()
	# перебираем из константы и заменяем на одинаковые
    for key in RATE_COLUMNS:
        if key in row:
            new_row['rate'] = row[key]
            break
    return new_row


def generate_payout_report(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    report = []
	
	# получаем все прочитанные файлы
    for row in rows:
        # нормализуем в одно название
        norm_row = normalize_row(row)
        try:
            # делаем расчёты
            payout = int(norm_row['hours_worked']) * int(norm_row['rate'])
        except (ValueError, KeyError):
            payout = None
		# создаем словарик
        report.append({
            "id": norm_row.get("id"),
            "name": norm_row.get("name"),
            "email": norm_row.get("email"),
            "department": norm_row.get("department"),
            "payout": payout
        })
    return report