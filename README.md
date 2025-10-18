# Руководство по запуску Jupyter Lab и Anaconda

## Содержание
1. [Установка Anaconda](#установка-anaconda)
2. [Запуск Anaconda Navigator](#запуск-anaconda-navigator)
3. [Создание виртуального окружения](#создание-виртуального-окружения)
4. [Запуск Jupyter Lab](#запуск-jupyter-lab)
5. [Полезные команды](#полезные-команды)
6. [Устранение неполадок](#устранение-неполадок)

## Установка Anaconda

### Для macOS:
1. Скачайте Anaconda с официального сайта: https://www.anaconda.com/download
2. Запустите установщик `.pkg` файл
3. Следуйте инструкциям установщика
4. После установки перезапустите терминал

### Проверка установки:
```bash
conda --version
python --version
```

## Запуск Anaconda Navigator

Anaconda Navigator - это графический интерфейс для управления пакетами, окружениями и приложениями Anaconda.

### Способы запуска:

#### 1. Через терминал:
```bash
# Запуск Anaconda Navigator
anaconda-navigator

# Запуск в фоновом режиме
anaconda-navigator &
```

#### 2. Через Spotlight (macOS):
- Нажмите `Cmd + Space`
- Введите "Anaconda Navigator"
- Нажмите Enter

#### 3. Через Launchpad (macOS):
- Откройте Launchpad
- Найдите папку "Anaconda3"
- Запустите "Anaconda Navigator"

#### 4. Через Applications (macOS):
- Откройте Finder
- Перейдите в папку "Applications"
- Найдите "Anaconda Navigator" и запустите

### Возможности Anaconda Navigator:

- **Home** - обзор установленных приложений
- **Environments** - управление виртуальными окружениями
- **Learning** - обучающие ресурсы
- **Community** - сообщество и поддержка

### Запуск приложений через Navigator:

1. Откройте Anaconda Navigator
2. Выберите нужное окружение (например, "base (root)")
3. Найдите приложение в списке (JupyterLab, Spyder, VS Code и др.)
4. Нажмите "Launch" для запуска

### Устранение проблем с Navigator:

```bash
# Если Navigator не запускается, попробуйте:
conda update anaconda-navigator

# Переустановка Navigator
conda remove anaconda-navigator
conda install anaconda-navigator

# Очистка кэша
anaconda-navigator --reset
```

## Создание виртуального окружения

### Создание нового окружения:
```bash
# Создание окружения с Python 3.9
conda create -n ds-env python=3.9

# Активация окружения
conda activate ds-env
```

### Установка необходимых пакетов:
```bash
# Установка Jupyter Lab
conda install jupyterlab

# Установка популярных библиотек для Data Science
conda install numpy pandas matplotlib seaborn scikit-learn

# Или установка через pip
pip install jupyterlab numpy pandas matplotlib seaborn scikit-learn
```

### Деактивация окружения:
```bash
conda deactivate
```

## Запуск Jupyter Lab

### 1. Активация окружения:
```bash
conda activate ds-env
```

### 2. Запуск Jupyter Lab:
```bash
# Запуск в текущей директории
jupyter lab

# Запуск в конкретной директории
jupyter lab --notebook-dir=/path/to/your/project

# Запуск на определенном порту
jupyter lab --port=8888
```

### 3. Доступ к Jupyter Lab:
- Откройте браузер и перейдите по адресу: `http://localhost:8888`
- Если появится запрос токена, скопируйте его из терминала

### 4. Остановка Jupyter Lab:
- В терминале нажмите `Ctrl + C` дважды
- Или закройте вкладку браузера и остановите процесс

## Полезные команды

### Управление окружениями Conda:
```bash
# Список всех окружений
conda env list

# Удаление окружения
conda env remove -n ds-env

# Экспорт окружения в файл
conda env export > environment.yml

# Создание окружения из файла
conda env create -f environment.yml
```

### Команды Jupyter:
```bash
# Список запущенных серверов
jupyter server list

# Остановка сервера по токену
jupyter server stop <token>

# Генерация конфигурационного файла
jupyter lab --generate-config
```

### Установка расширений Jupyter Lab:
```bash
# Установка популярных расширений
pip install jupyterlab-git
pip install jupyterlab-lsp
pip install jupyterlab-code-formatter
```

## Устранение неполадок

### Проблема: Jupyter Lab не запускается
**Решение:**
```bash
# Переустановка Jupyter Lab
conda uninstall jupyterlab
conda install jupyterlab

# Или через pip
pip uninstall jupyterlab
pip install jupyterlab
```

### Проблема: Порт уже используется
**Решение:**
```bash
# Запуск на другом порту
jupyter lab --port=8889

# Или найдите и остановите процесс
lsof -ti:8888 | xargs kill -9
```

### Проблема: Не удается импортировать библиотеки
**Решение:**
```bash
# Убедитесь, что окружение активировано
conda activate ds-env

# Установите библиотеку в активное окружение
conda install numpy
# или
pip install numpy
```

### Проблема: Jupyter Lab не видит виртуальное окружение
**Решение:**
```bash
# Установка ipykernel в окружение
conda activate ds-env
conda install ipykernel

# Регистрация ядра
python -m ipykernel install --user --name ds-env --display-name "Python (ds-env)"
```

## Структура проекта

```
ds/
├── lesson-1/
│   └── env/          # Виртуальное окружение
├── notebooks/        # Jupyter notebooks
├── data/            # Данные для анализа
├── src/             # Исходный код
└── README.md        # Этот файл
```

## Дополнительные ресурсы

- [Официальная документация Anaconda](https://docs.anaconda.com/)
- [Документация Jupyter Lab](https://jupyterlab.readthedocs.io/)
- [Руководство по Conda](https://conda.io/projects/conda/en/latest/user-guide/index.html)

---

**Примечание:** Этот README создан для проекта Data Science. Адаптируйте команды и настройки под ваши конкретные потребности.
