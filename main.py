from datetime import datetime


def calc_and_display_age(year_born, month_born, day_born):
    age_in_years = datetime.now().year - year_born
    if month_born > datetime.now().month:
        age_in_years -= 1
    elif month_born == datetime.now().month and day_born > datetime.now().day:
        age_in_years -= 1
    # print('You are ' + age_in_years + ' years old') <- doesn't work
    print('You are ' + str(age_in_years) + ' years old')
    print(f'You are {age_in_years} years old')


year_born = int(input('Insert your year of birth: '))
month_born = int(input('Insert your month of birth: '))
day_born = int(input('Insert your day of birth: '))
calc_and_display_age(year_born, month_born, day_born)



