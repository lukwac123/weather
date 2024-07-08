from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Pobranie dat i temperatur maksymalnych z pliku.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# Dane wykresu.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Formatowanie wykresu.
ax.set_title("Najwyższa temperatura dnia, lipiec 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatura (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

