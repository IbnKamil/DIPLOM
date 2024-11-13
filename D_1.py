import pandas as pd

file_path = r'C:\Users\Magom\PYTHON\python_Diplom\sample_dataset.xlsx'

df = pd.read_excel(file_path)

print("Первые 5 строк данных из Excel:")
print(df.head())

print("\nИнформация о данных (информация о столбцах, типах данных и количестве значений):")
print(df.info())

# Описание статистических данных (среднее, стандартное отклонение и т.д.)
print("\nСтатистическое описание данных:")
print(df.describe())

# Получение уникальных значений в столбце, т.е. всех данных для конкретного показателя )
if 'Уровень безработицы' in df.columns:
    print("\nУникальные значения в столбце 'Уровень безработицы':")
    print(df['Уровень безработицы'].unique())

# Фильтрация данных, где значение в столбце 'Уровень безработицы' равен 0)
if 'Уровень безработицы' in df.columns:
    filtered_data = df[df['Уровень безработицы'] == 0]
    print("\nОтфильтрованные данные (где значение в столбце 'Уровень безработицы' равен 0):")
    print(filtered_data)

# Создание нового столбца "общий показатель экономической производительности, учитывающий рост и инфляцию"
# Предположим, что мы хотим создать новый столбец, который будет в 2 раза больше значения из столбца 'Уровень безработицы'
if 'Уровень безработицы' in df.columns:
    df['общий показатель экономической производительности, учитывающий рост и инфляцию'] = df['Уровень безработицы'] * 2
    print("\nДанные с добавленным новым столбцом:")
    print(df.head())

# Сохранение измененного DataFrame в новый Excel-файл
output_file_path = r'C:\Users\Magom\PYTHON\python_Diplom\sample_dataset.xlsx'
df.to_excel(output_file_path, index=False)
print(f"\nИзмененные данные сохранены в файл: {output_file_path}")


import pandas as pd
import time
import dask.dataframe as dd

# Загрузка данных
data = pd.read_excel('sample_dataset.xlsx')

# Работа с Pandas
start_time = time.time()
pandas_result = data.groupby('Year').agg({
    'Экономический рост': 'mean',
    'Уровень безработицы': 'mean'
}).reset_index()
pandas_time = time.time() - start_time
print(f"Время выполнения для Pandas: {pandas_time:.4f} секунд")

# Работа с Dask
dask_data = dd.from_pandas(data, npartitions=4)
start_time = time.time()
dask_result = dask_data.groupby('Year').agg({
    'Экономический рост': 'mean',
    'Уровень безработицы': 'mean'
}).compute()
dask_time = time.time() - start_time
print(f"Время выполнения для Dask: {dask_time:.4f} секунд")

import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные из Excel
data = pd.read_excel('sample_dataset.xlsx')

# Получаем уникальные страны
countries = data['Country'].unique()

# Настройка для отображения графиков
fig, axs = plt.subplots(len(countries), 2, figsize=(14, 6 * len(countries)))

# Один график, делаем axs одномерным массивом
if len(countries) == 1:
    axs = [axs]

# Строим графики для каждой страны
for i, country in enumerate(countries):
    # Фильтруем данные по стране
    country_data = data[data['Country'] == country]

    # Агрегируем данные по году для каждой страны
    aggregated_country_data = country_data.groupby('Year').agg({
        'Экономический рост': 'mean',
        'Уровень безработицы': 'mean'
    }).reset_index()

    # График для 'Экономический рост'
    axs[i][0].plot(aggregated_country_data['Year'], aggregated_country_data['Экономический рост'])
    axs[i][0].set_title(f'Экономический рост по годам ({country})')
    axs[i][0].set_xlabel('Год')
    axs[i][0].set_ylabel('Экономический рост')

    # График для 'Уровень безработицы'
    axs[i][1].plot(aggregated_country_data['Year'], aggregated_country_data['Уровень безработицы'])
    axs[i][1].set_title(f'Уровень безработицы по годам ({country})')
    axs[i][1].set_xlabel('Год')
    axs[i][1].set_ylabel('Уровень безработицы')

# Настроим отступы и пространство между графиками
plt.subplots_adjust(left=0.086, bottom=0.063, right=0.96, top=0.956, wspace=0.198, hspace=0.8)

# Покажем графики
plt.show()
