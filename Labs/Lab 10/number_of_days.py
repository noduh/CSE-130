day_start = None
month_start = None
year_start = None
day_end = None
month_end = None
year_end = None


def is_leap_year(year):
    assert year > 1752, "year must not be less than 1753"

    if year % 100:
        if year % 400:
            return True
    if year % 4:
        return True
    return False


def days_in_month(month, year):
    assert 0 < month < 13, "invalid month"
    months = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month - 1]


def days_in_year(year):
    return 365 + is_leap_year(year)

