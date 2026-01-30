print("ФАЙЛ run_api_part.py ЗАПУЩЕН")

from collecting_from_api.api_collector import NasaApodCollector

def main():
    print("Запуск сбора данных NASA API...")

    collector = NasaApodCollector()
    data = collector.get_apod(count=5)

    print(f"Получено записей: {len(data)}")

    collector.save_to_csv(
        data,
        'collecting_from_api/data/nasa_apod.csv'
    )

    print("API часть завершена")

if __name__ == '__main__':
    main()
