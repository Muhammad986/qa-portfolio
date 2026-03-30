# Подготовка проекта

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

Установить все зависимости из `requirements.txt`:

```bash
pip install -r requirements.txt
```

Сохранить текущие установленные библиотеки в `requirements.txt`

```bash
pip freeze > requirements.txt
```