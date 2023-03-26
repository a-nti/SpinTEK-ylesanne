import csv
import holidays
from datetime import date as as_date, timedelta

MIN_YEAR_ALLOWED = 1900     # probably no point in going any lower
MAX_YEAR_ALLOWED = 9999     # datetime module limitation
EXPECTED_PAY_DAY = 10       # 10th day of each month
ESTONIAN_HOLIDAYS = holidays.EE()
MONTH_NAMES = ["Jaanuar", "Veebruar", "Märts", "Aprill", "Mai", "Juuni", "Juuli", "August", "September", "Oktoober",
               "November", "Detsember"]


def main():
    print("Järgnev rakendus leiab ettevõtte Spin TEK palkade väljastamise ja vastavate "
          "meeldetuletuste kuupäevad kuude lõikes.\n")
    year = get_input_year()
    payment_dates = find_payment_dates(year)
    reminder_dates = find_reminder_dates(payment_dates)
    output_to_file(payment_dates, reminder_dates, year)


def get_input_year():
    while True:
        try:
            year = int(input("Palun sisestage vaatlusalune aasta (kujul aaaa): "))
            if year < MIN_YEAR_ALLOWED or year > MAX_YEAR_ALLOWED:
                print("Aasta peab jääma vahemikku", MIN_YEAR_ALLOWED, "kuni", MAX_YEAR_ALLOWED, "\n")
            else:
                return year
        except ValueError:
            print("Kontrollige sisendit! Aasta peab olema täisarvuna kujul aaaa (nt 2023). \n")


def find_payment_dates(year):
    payment_dates = []
    for month in range(1, 13):
        date = as_date(year, month, EXPECTED_PAY_DAY)
        # get previous date until we land on a non-holiday workday
        while is_holiday_or_weekend(date):
            date = get_previous_date(date)
        # when found, add to list
        payment_dates.append(date)
    return payment_dates


def find_reminder_dates(payment_dates):
    reminder_dates = []
    for date in payment_dates:
        # reset counter
        counter = 3
        # store in temp variable to avoid changing loop's iterable
        temp_date = date
        # get previous date until we land on 3rd prior non-holiday workday
        while counter > 0:
            temp_date = get_previous_date(temp_date)
            if not is_holiday_or_weekend(temp_date):
                counter -= 1
        # when found, add to list
        reminder_dates.append(temp_date)
    return reminder_dates


def is_holiday_or_weekend(date):
    # 5 and 6 represent Saturday and Sunday
    if date in ESTONIAN_HOLIDAYS or date.weekday() in (5, 6):
        return True 


def get_previous_date(date):
    # given a date, find the date for the day before
    return date - timedelta(1)


def output_to_file(payment_dates, reminder_dates, year):
    try:
        # open file in write mode
        with open(str(year) + ".csv", "w", encoding="Windows-1252", newline="") as file:
            writer = csv.writer(file)
            # output table header
            writer.writerow(["Kuu", "Palgamaksmise kuupäev", "Meeldetuletuse kuupäev"])
            # output month names along with payment and reminder dates in day-month-year format
            for month, payment_date, reminder_date in zip(MONTH_NAMES, payment_dates, reminder_dates):
                writer.writerow([month, payment_date.strftime("%d.%m.%Y"), reminder_date.strftime("%d.%m.%Y")])
    except Exception as e:
        print("Faili kirjutamine ebaõnnestus!", e)


if __name__ == "__main__":
    main()
