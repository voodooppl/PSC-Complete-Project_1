import requests
import calendar
import datetime
import datetime as dt


class GenerateYear:
    def __init__(self, current_year):
        self.current_year = current_year
        self.zile_sarbatoare = []
        self.data_15_min = []

    # # # ------------ is leap year -------------------- #
    def is_leap_year(self):
        is_leap = calendar.isleap(int(self.current_year))
        if is_leap:
            nr_intervals = (366*96)-4
        else:
            nr_intervals = (365*96)-4
        return nr_intervals

# # # -----------------daylight saving ----------------- #
#
    def daylight_savings(self):

        dls = {
            '2021': {
                'DST Start': [2021, 3, 2],
                'DST End': [2021, 10, 31]
            },
            '2022': {
                    'DST Start': [2022, 3, 27],
                    'DST End': [2022, 10, 30]
                },
            '2023': {
                    'DST Start': [2023, 3, 26],
                    'DST End': [2023, 10, 29]
            },
            '2024': {
                    'DST Start': [2024, 3, 31],
                    'DST End': [2024, 10, 27]
            },
            '2025': {
                    'DST Start': [2025, 3, 30],
                    'DST End': [2025, 10, 26]
            },
            '2026': {
                    'DST Start': [2026, 3, 29],
                    'DST End': [2026, 10, 25]
            },
            '2027': {
                    'DST Start': [2027, 3, 28],
                    'DST End': [2027, 10, 31]
            },
            '2028': {
                    'DST Start': [2028, 3, 26],
                    'DST End': [2028, 10, 29]
                },
            '2029': {
                    'DST Start': [2029, 3, 25],
                    'DST End': [2029, 10, 28]
                }
        }
        dls_start_day = dls[f'{self.current_year}']['DST Start'][2]
        dls_start_date = f'{self.current_year}-03-{dls_start_day}'
        dls_end_day = dls[f'{self.current_year}']['DST End'][2]
        dls_end_date = f'{self.current_year}-10-{dls_end_day}'

        return dls_start_date, dls_end_date
# # # -------------- create the year generation function ------------------ #

    def create_year(self):

        nr_intervals = self.is_leap_year()
        dls_start_date, dls_end_date = self.daylight_savings()
        luna_start = 1
        zi_start = 1
        ora_start = 00
        minut_start = 00
        weekdays = ['0', 'L', "Ma", 'Mi', 'J', 'V', 'S', 'D']
        data = dt.datetime(int(self.current_year), luna_start, zi_start, ora_start, minut_start)
        for n in range(0, nr_intervals):
            new_data = [data.date(), data.time(), weekdays[data.isoweekday()]]

            if str(data.date()) == dls_start_date and str(data.time()) == '03:00:00':
                data = data + datetime.timedelta(0, 3600)
                new_data = [data.date(), data.time(), weekdays[data.isoweekday()]]
            else:
                pass

            if str(data.date()) == dls_end_date and str(data.time()) == '04:00:00':
                time1 = data + datetime.timedelta(0, -3600)
                time2 = data + datetime.timedelta(0, -2700)
                time3 = data + datetime.timedelta(0, -1800)
                time4 = data + datetime.timedelta(0, -900)
                time5 = data + datetime.timedelta(0, 0)
                new_data = [data.date(), time1.time(), weekdays[data.isoweekday()]]
                self.data_15_min.append(new_data)
                new_data = [data.date(), time2.time(), weekdays[data.isoweekday()]]
                self.data_15_min.append(new_data)
                new_data = [data.date(), time3.time(), weekdays[data.isoweekday()]]
                self.data_15_min.append(new_data)
                new_data = [data.date(), time4.time(), weekdays[data.isoweekday()]]
                self.data_15_min.append(new_data)
                new_data = [data.date(), time5.time(), weekdays[data.isoweekday()]]
            else:
                pass
            self.data_15_min.append(new_data)
            data = data + datetime.timedelta(0, 900)

        return self.data_15_min

    # # -------------------zile sarbatoare------------------------------- #

    # def check_zile_sarbatoare_old(self):
    #     api_link = 'https://us-central1-romanian-bank-holidays.cloudfunctions.net/romanian_bank_holidays'
    #     api_params = {
    #         'year': self.current_year
    #     }
    #     result = requests.get(api_link, params=api_params)
    #     result.raise_for_status()
    #     my_data = result.json()
    #
    #     for line in my_data:
    #         data_libera = line['date']
    #         new_data = f"{data_libera.split('/')[2]}-{data_libera.split('/')[1]}-{data_libera.split('/')[0]}"
    #         self.zile_sarbatoare.append(new_data)
    #     return self.zile_sarbatoare

    def check_zile_sarbatoare(self):
        api_link = 'https://romanian-bank-holidays.backdevs.net'
        api_params = {
            'year': self.current_year,
        }
        result = requests.get(api_link, params=api_params)
        result.raise_for_status()
        my_data = result.json()
        for data in range(len(my_data)):
            data_libera = my_data[data]['date']
            self.zile_sarbatoare.append(data_libera)
        return self.zile_sarbatoare
