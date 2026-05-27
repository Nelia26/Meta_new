# AdGrid Generator (Meta Ads)

Невеликий прототип для формування рекламної сітки (Ad Grid) та експорту у Excel.

## Вимоги
- Python 3.10+

## Встановлення
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск
```bash
python main.py --config sample_config.json --out AdGrid_MetaAds.xlsx
```

## Формат конфігу
Див. `sample_config.json`.

> Примітка: інтеграція з Meta Marketing API не виконується (потрібні токени). Прототип готує структуру даних/файл для планування.
