# Dostęp do danych w formacie CSV oraz ich wizualizacja.

Analiza danych, które przechowywane są w pliku w formacie CSV. Wykorzystanie modułu **csv** ze standardowej biblioteki Pythona do zaimportowania danych,
a następnie użycie biblioteki **matplotlib** do przygotowania wizualizacji tych danych.

W pliku _sitka_highs_lows.py_ zaimportowane zostały dane dotyczące warunków pogodowych na przestrzeni 2021 roku dla miejscowości Sitka na Alasce.
Wykorzystano tutaj moduł **datetime** aby wyświetlić na wykresie datę jako format daty. Wykres zawiera dwie serie danych: temperaturę maksymalną i minimalną,
które były rejestrowane każdego dnia przez odpowiednią stację badawczą.

![Weather_Sitka_Alaska_2021](https://github.com/lukwac123/weather/assets/161370029/42fce1f0-90ee-411d-ad95-d3cc1544777d)

<sup>Wykres 1. Dwie serie danych wraz z pocieniowanym obszarem między nimi.</sup>


Plik _death_valley_highs_lows.py_ zawiera podobny zestaw danych z tym że w danych brakuje pomiarów z jednego dnia, aby obsłużyć ten wyjątek zmodyfikowano
kod programu tak aby wyświetlał informację o braku danych ale jednocześnie potrafił przedstawić wykres z pozostałymi danymi (użycie _try-except-else_).

![Weather_Dolina_Smierci_Kalifornia_2021](https://github.com/lukwac123/weather/assets/161370029/4f2a3097-6c04-4c62-b3d3-4b7d9e0c4001)

<sup>Wykres 2. Dwie serie danych wraz z pocieniowanym obszarem między nimi.</sup>
