import datetime, time

dt = datetime.datetime.now()
persnum = input("Mata in ditt personnummer(yyyymmdd): ")
persSplit = persnum.split("-")
dtpers = dt.strptime(persSplit[0], '%Y%m%d')

years = dt.year - dtpers.year
months = dt.month - dtpers.month
days = dt.day - dtpers.day

if int(persSplit[1][-2]) % 2 == 0:
  print("Du är en kvinna.")

else:
    print("Du är en man.")