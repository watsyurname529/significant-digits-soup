from datetime import date, timedelta
import dateutil.parser as dateutil
import requests

start_date = date(2016, 1, 1)
end_date = date(2016, 1, 15)
delta = timedelta(days=1)

current_date = start_date

while(current_date <= end_date):
    format_date = current_date.strftime('%A-%b-%d-%Y').lower()
    if(current_date.isoweekday() < 6):
        url = 'http://fivethirtyeight.com/features/significant-digits-for-{}/'.format(format_date)
        page = requests.get(url)
        print('URL: ', url)
        print('Status: ', page.status_code)
    current_date = current_date + delta

