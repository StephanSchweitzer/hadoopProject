def extractint(x):
    if isinstance(x, str):
        the_number = ''
        for i in x:
            if i.isdigit():
                the_number += i
        if the_number == '':
            return 0
        else:
            return int(the_number)
    else:
        return x


def howmanydigits(x):
    return len(str(x))


def givethegoodyear(numbers):
    numbers = extractint(numbers)
    final_date = 0
    if numbers == '':
        return 0
    if (numbers // 100) % 100 <= 12:
        final_date = numbers % 100
        if final_date > 9:
            final_date = '20' + str(final_date)
        else:
            final_date = '200' + str(final_date)
    else:
        final_date = numbers % 10000

    return final_date

def cut_years(the_whole_date):
    if not isinstance(the_whole_date, str):
        print("Not string")
        return

    the_whole_date = the_whole_date[:4]
    return the_whole_date

def get_pollution_by_city_and_year(city = '', year = ''):
    print(city)
    print(year)
