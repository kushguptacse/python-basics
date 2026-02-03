import datetime

t = datetime.time(4, 20, 1)

print(t)  # 04:20:01
print(
    f"hour: {t.hour}, minute: {t.minute}, second: {t.second}, microsecond: {t.microsecond}, tzinfo: {t.tzinfo}"
) # hour: 4, minute: 20, second: 1, microsecond: 0, tzinfo: None

print(f"earliest {datetime.time.min}")  # 00:00:00
print(f"latest {datetime.time.max}")  # 23:59:59.999999
print(f"resolution {datetime.time.resolution}")  # 0:00:00.000001

d = datetime.date(2023, 10, 5)
print(d)  # 2023-10-05
print(f"Year: {d.year}, Month: {d.month}, Day: {d.day}") #Year: 2023, Month: 10, Day: 5
print("Earliest  :", datetime.date.min)
print("Latest    :", datetime.date.max)
print("Resolution:", datetime.date.resolution)
today = datetime.date.today()
print("Today's date:", today)  # e.g., 2024-06-15

print("Difference:", today - d)

dt = datetime.datetime(2023, 10, 5, 4, 20, 1)  # combines date and time
print(dt)  # 2023-10-05 04:20:01
print(
    f"Year: {dt.year}, Month: {dt.month}, Day: {dt.day}, Hour: {dt.hour}, Minute: {dt.minute}, Second: {dt.second}"
) #Year: 2023, Month: 10, Day: 5, Hour: 4, Minute: 20, Second: 1
print("Datetime min:", datetime.datetime.min)
print("Datetime max:", datetime.datetime.max)
print("Datetime resolution:", datetime.datetime.resolution) 