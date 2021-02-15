import datetime, time

dt = datetime.datetime.now()
persnum = input("Mata in ditt personnummer(yyyymmdd): ")
persSplit = persnum.split("-")
dtpers = dt.strptime(persSplit[0], '%Y%m%d')

if (dt.month == dtpers.month and dt.day == dtpers.day):
  print("Grattis det är din födelsedag! ", dtpers.date())

if int(persSplit[1][-2]) % 2 == 0:
  print("Du är en kvinna.")
else:
    print("Du är en man.")


years = dt.year - dtpers.year
months = dt.month - dtpers.month
days = dt.day - dtpers.day

print(f"Du är {years} år, {months} månader och {days} dagar gammal.")