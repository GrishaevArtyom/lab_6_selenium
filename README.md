# Автоматизированные тесты для поиска на Яндекс

## Описание проекта
Автоматизированные UI-тесты для проверки функциональности поиска на главной странице Яндекс (`https://ya.ru`) с использованием:
- Selenium WebDriver
- pytest
- Allure Framework
- Page Object Model

Тесты проверяют:
- Отображение подсказок при вводе текста
- Выполнение поиска по запросу
- Корректность результатов поиска
- Очистку поискового поля

## Технологический стек
- Python 3.8+
- Selenium == 4.15.0
- pytest == 7.4.3
- pytest-xdist == 3.5.0
- allure-pytest == 2.13.2
- webdriver-manager == 4.0.1

## Установка зависимостей
Установите зависимости из файла `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Запуск тестов 

Обычный запуск 
```bash
pytest tests/test_yandex_form.py -v
```

Параллельный запуск (2 потока) 
```bash
pytest tests/test_yandex_form.py -n 2 -v
```

С генерацией Allure-отчёта 
```bash
pytest tests/test_yandex_form.py --alluredir=allure-results -v
allure serve allure-results
```

Для работы команды allure необходимо предварительно установить Allure CLI: 
- Windows: choco install allure 
- macOS: brew install allure
- Linux: через SDKMAN (sdk install allure) или вручную с официального сайта 

## Структура проекта
```lab_6_selenium/
│
├── pages/                      # Page Object файлы
│   ├── __init__.py
│   └── yandex_form_page.py     # Страница поиска Яндекс
│
├── tests/                      # Тесты
│   ├── __init__.py
│   └── test_yandex_form.py     # Набор UI-тестов
│
├── conftest.py                 # PyTest фикстуры и конфиги браузера
├── pytest.ini                  # Настройки PyTest
├── requirements.txt            # Зависимости проекта
└── README.md                   # Документация проекта
```
