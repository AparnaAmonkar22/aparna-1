import datetime

zodiacs = [(119, 'Cap'), (218, 'Aqu'), (320, 'Pis'), (419, 'Ari'), (520, 'Tau'),
        (620, 'Gem'), (722, 'Can'), (822, 'Leo'), (922, 'Vir'), (1022, 'Lib'),
        (1121, 'Sco'), (1221, 'Sag'), (1231, 'Cap')]

# Function to find Zodiac Sign
def findZodiac(birthday):

    day, month, year  = map(int, birthday.split('-'))

    # print(f'\n{day}, {month}, {year}')
    
    date = datetime.date(year, month, day)
    # add zero padding to day
    bdate = int("".join((str(date.month), '%02d' % date.day)))

    for z in zodiacs:
        if bdate <= z[0]:
            return z[1]


# Take Name and birthday input
name, bdate = input("Please enter Name and the birthdate(dd-mm-yyyy): ").split()
# bdate = int(bdate)
sign = findZodiac(bdate)
print(f'{name} {sign}')
