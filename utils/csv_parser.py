from typing import List, Dict

# парсим дату из файла
def parse_csv(path: str) -> List[Dict[str, str]]:
    with open(path, 'r') as f:
        lines = f.readlines()
        
	# фиксируем хедеры
    headers = [h.strip() for h in lines[0].strip().split(',')]
    data = []

    for line in lines[1:]:
        # получаем значения
        values = [v.strip() for v in line.strip().split(',')]
        # создаем строку словарь, ключ значение
        row = dict(zip(headers, values))
        # добавляем данные
        data.append(row)

    return data
