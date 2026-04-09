
from data.data import Color, Date, Person
from faker import Faker
from pathlib import Path
from datetime import datetime, timedelta
import random

faker_ru = Faker('ru_RU')
faker_en = Faker('en_US')
Faker.seed()

def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=faker_ru.random_int(min=18, max=80),
        salary=faker_ru.random_int(min=120000, max=450000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
        date_of_birth=faker_ru.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=80).strftime("%d %b %Y")
    )

def generated_file():
    path = f'/home/muhammad/Dev/qa-portfolio/file_for_tests/test_file{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello, this is a test file. Random number: {random.randint(0, 999)}')
    file.close()
    return Path(path).name, path

def generated_subject():
    subjects = [
        "Hindi", "English", "Maths", "Physics", "Chemistry",
        "Biology", "Computer Science", "Commerce", "Accounting",
        "Economics", "Arts", "Social Studies", "History", "Civics"
    ]
    return random.choice(subjects)

def generate_random_date(start_year=1980, end_year=2005):
    """
    Генерирует случайную дату между 1 января start_year и 31 декабря end_year
    и возвращает её в формате 'DD Mon YYYY'
    """
    # Генерируем случайный год, месяц и день
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.strftime("%d %b %Y")

def generated_color():
    yield Color(
        color_name=[
            "Red", "Blue", "Green", "Yellow", "Purple", "Black", "White","Voilet", "Indigo", "Magenta", "Aqua"
        ]
    )
def generated_date():
    yield Date(
        date=faker_en.day_of_month(),
        month=faker_en.month_name(),
        year=faker_en.year(),
        time='12:00'
    )
