print("ФАЙЛ run_parsing_part.py ЗАПУЩЕН")

from parsing.web_parser import AutoRuParser
import pandas as pd
import os

def main():
    print("Запуск парсинга Auto.ru")

    parser = AutoRuParser()

    url = 'https://auto.ru/moskva/cars/bmw/all/'
    data = parser.parse_cars(url)

    print(f"Найдено объявлений: {len(data)}")

    os.makedirs('parsing/data', exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(
        'parsing/data/bmw_auto_ru.csv',
        index=False,
        encoding='utf-8-sig'
    )

    parser.close()
    print("Парсинг завершён")

if __name__ == '__main__':
    main()
