import json
import logging
from pathlib import Path

logging.basicConfig(
    filename='json_chumak.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ф-я приймає шлях до теки з json-файлами та валідує їх. Інформацію про невалідні поміщає в json_chumak.log
def valid_json(folder_route):
    file_list = Path(folder_route)
    for file in file_list.glob("*.json"):
        try:
            with open(file, 'r', encoding='utf-8') as file:
                json.load(file)
            print(f'{file.name} is valid Json file.')
        except json.JSONDecodeError as e:
            logging.error(f'{file.name} is invalid Json file: {e}')
    print(f'Invalid files are logged in "json_chumak.log"')

json_directory = 'json_files'

valid_json(json_directory)

