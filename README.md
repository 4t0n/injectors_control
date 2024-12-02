### Описание проекта:

Данное приложение позволяет управлять автомобильными высокоомными форсунками:

Основные возможности:

* Управление с помощью Arduino Nano
* Подключение через COM-порт
* Выбор частоты и времени импульса
  
### Stack
* Python 3.12
* PyQT5

### Как запустить проект на Windows:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/4t0n/injectors_control.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить main.py.

### Общий вид приложения

![injectors](https://github.com/user-attachments/assets/7a3f25a0-897c-4320-b379-52aebb4db562)
