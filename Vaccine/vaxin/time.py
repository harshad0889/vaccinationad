class date_n:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


month_Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def count_Leap_Years(day):
    years = day.year

    if (day.month <= 2):
        years -= 1

    return int(years / 4) - int(years / 100) + int(years / 400)


def get_difference(date_1, date_2):
    n_1 = date_1.year * 365 + date_1.day

    for K in range(0, date_1.month - 1):
        n_1 += month_Days[K]

    n_1 += count_Leap_Years(date_1)

    n_2 = date_2.year * 365 + date_2.day
    for K in range(0, date_2.month - 1):
        n_2 += month_Days[K]
    n_2 += count_Leap_Years(date_2)

    return (n_2 - n_1)


# Driver program
s = date_n(1, 5, 2022)
e = date_n(1, 5, 2025)

print("Number of Days between the given Dates are: ", get_difference(s, e), "days")

a = get_difference(s, e)
b = a - 3

print(b)
