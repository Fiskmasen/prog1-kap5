import datetime, time

dt = datetime.datetime.now()
persnum = input("Mata in ditt personnummer(yyyymmdd): ")
persSplit = persnum.split("-")
dtpers = dt.strptime(persSplit[0], '%Y%m%d')

years = dt.year - dtpers.year
months = dt.month - dtpers.month
days = dt.day - dtpers.day

if dt.month == dtpers.month and dt.day == dtpers.day:
  print("Grattis det är din födelsedag! ", dtpers.date())
  

else:
  print("Det är inte din födelsedag ännu, kom tillbaka när du faktiskt fyller år, ditt fä!")

print(f"Du är {years} år, {months} månader och {days} dagar gammal.")