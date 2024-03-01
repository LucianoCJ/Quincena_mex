import pandas as pd

def BS(ds):
    # Obtener el día del mes
    date = pd.to_datetime(ds, format='%Y-%m-%d')
    day_of_month = date.day
    month = date.month
    year = date.year
    day_of_week = date.weekday()
    
    # Verificar si es sábado o domingo
    if day_of_week in [5, 6]:  # 5 es sábado, 6 es domingo
        # Ajustar al viernes más cercano
        if day_of_week == 5:  # sábado
            date -= pd.Timedelta(days=1)
        else:  # domingo
            date -= pd.Timedelta(days=2)

    # Si ya se ajustó el día, no volver a ajustarlo
    if day_of_week in [5, 6]:
        return 0
    
    # Verificar si es febrero y si es un año bisiesto
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_feb = 29  # Año bisiesto
        else:
            days_in_feb = 28
        # Verificar si el día del mes es el último día válido de febrero
        # Verificar si el día del mes es mayor que el último día válido de febrero
        if day_of_month > days_in_feb :
            day_of_month = days_in_feb
    
    # Verificar si es día de quincena (suponiendo quincenas los días 15 y 30)
    if (day_of_month == 15 or day_of_month == 30) or (month == 2 and day_of_month in [28, 29]):
        return 1
    elif day_of_week == 4:  # Viernes
        next_day_1 = date + pd.Timedelta(days=1)
        next_day_2 = date + pd.Timedelta(days=2)
        if (next_day_1.day == 15 or next_day_1.day == 30 or 
            next_day_2.day == 15 or next_day_2.day == 30):
            return 1
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days_in_feb = 29  # Año bisiesto
            else:
                days_in_feb = 28
            if (next_day_1.day == days_in_feb or next_day_2.day == days_in_feb):
                return 1
    return 0


# Ejemplo de uso
print("15 de febrero",BS("2024-02-15"))    
print("28 de febrero",BS("2023-02-28"))
print("29 de marzo",BS("2024-03-29"))
print("29 de ferero",BS("2024-02-29"))  # Salida: 1 (primer quincena de febrero)
print("15 de marzo",BS("2024-03-15"))  # Salida: 1 (segunda quincena de febrero)
print("30 de marzo",BS("2024-03-30"))  # Salida: 0 (fuera de quincenas)
print("15 de junio",BS("2024-06-15"))  # Salida: 1 (primer quincena de junio)
print("30 de junio",BS("2024-06-30"))  # Salida: 1 (segunda quincena de junio)
print("28 de junio",BS("2024-06-28"))
print("11 de julio",BS("2024-07-11"))
print("28 de febrero",BS("2021-02-28"))
print("27 de febrero",BS("2021-02-27"))
print("26 de febrero",BS("2021-02-26"))
