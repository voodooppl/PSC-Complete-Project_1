import pandas
from tkinter import *
from year_creation_file import GenerateYear
import messagebox

# # -----------current year --------------#


def current_year_func():
    current_year = year_entry.get()
    selected_psc = psc_entry.get()
    return int(current_year), int(selected_psc)


class PscManagement(GenerateYear):

    def __init__(self, current_year, selected_psc):
        super().__init__(current_year)
        self.current_year = current_year
        self.selected_psc = selected_psc
        self.zile_sarbatoare = self.check_zile_sarbatoare()
        self.zile_lucratoare_nelucratoare = {}
        self.ponderi = []
        self.psc_profile = []
        self.rest = 0
        print(self.zile_sarbatoare)
# #------------------------parsare fisier/preluare date-------------------- #
        xl = pandas.read_excel('profile specifice.xlsx', sheet_name=[0, 1])
        sheet_1 = xl[0]
        sheet_2 = xl[1]
        self.my_dict = sheet_1.to_dict(orient='records')
        self.my_dict_2 = sheet_2.to_dict(orient='records')

# #--------calculeaza totalul de zile lucratoare si nelucratoare------- #
    def get_month_and_day(self):
        total_zile_l = 0
        total_zile_n = 0
        for y in range(len(self.data_15_min)):
            current_month = self.data_15_min[y][0].month
            current_day = self.data_15_min[y][2]
            if current_day in ['S', 'D'] or str(self.data_15_min[y][0]) in self.zile_sarbatoare:
                if f'{current_month}_nelucratoare' in self.zile_lucratoare_nelucratoare.keys():
                    pass
                else:
                    total_zile_n = 0
                total_zile_n += 1/96
                self.zile_lucratoare_nelucratoare[f'{current_month}_nelucratoare'] = round(total_zile_n)
            else:
                if f'{current_month}_lucratoare' in self.zile_lucratoare_nelucratoare.keys():
                    pass
                else:
                    total_zile_l = 0
                total_zile_l += 1/96
                self.zile_lucratoare_nelucratoare[f'{current_month}_lucratoare'] = round(total_zile_l)
        return self.zile_lucratoare_nelucratoare
# #-----------------------calculeaza ponderile----------------------- #

    def get_ponderi(self):
        for x in range(len(self.my_dict)):
            if self.my_dict[x]['PSC'] == self.selected_psc:
                if self.my_dict[x]['inceput'] == 'ponderi':
                    self.ponderi.append([self.my_dict[x]['Primavara'], self.my_dict[x]['Primavara.1'],
                                         self.my_dict[x]['Vara'], self.my_dict[x]['Vara.1'],
                                         self.my_dict[x]['Toamna'], self.my_dict[x]['Toamna.1'],
                                         self.my_dict[x]['Iarna'], self.my_dict[x]['Iarna.1']
                                         ])

    def get_monthly_qty(self, current_month):

        if current_month == 1:
            monthly_qty = int(month_1_entry.get())
            return int(monthly_qty)
        elif current_month == 2:
            monthly_qty = int(month_2_entry.get())
            return monthly_qty
        elif current_month == 3:
            monthly_qty = int(month_3_entry.get())
            return monthly_qty
        elif current_month == 4:
            monthly_qty = int(month_4_entry.get())
            return monthly_qty
        elif current_month == 5:
            monthly_qty = int(month_5_entry.get())
            return monthly_qty
        elif current_month == 6:
            monthly_qty = int(month_6_entry.get())
            return monthly_qty
        elif current_month == 7:
            monthly_qty = int(month_7_entry.get())
            return monthly_qty
        elif current_month == 8:
            monthly_qty = int(month_8_entry.get())
            return monthly_qty
        elif current_month == 9:
            monthly_qty = int(month_9_entry.get())
            return monthly_qty
        elif current_month == 10:
            monthly_qty = int(month_10_entry.get())
            return monthly_qty
        elif current_month == 11:
            monthly_qty = int(month_11_entry.get())
            return monthly_qty
        elif current_month == 12:
            monthly_qty = int(month_12_entry.get())
            return monthly_qty
# #-------------add psc values to datetime values ---------- #

    def generate_psc(self):
        for date, time, day in self.data_15_min:
            current_date = date
            current_month = date.month
            current_time = time
            current_day = day
            monthly_qty = self.get_monthly_qty(current_month)
            for y in range(len(self.my_dict)):
                if self.my_dict[y]['PSC'] == self.selected_psc:
                    if current_month in [12, 1, 2]:
                        anotimp_l = 'Iarna'
                        anotimp_nl = 'Iarna.1'
                        pondere_nelucratoare = self.ponderi[0][7]
                        pondere_lucratoare = self.ponderi[0][6]
                        nr_zile_l = self.zile_lucratoare_nelucratoare[f'{current_month}_lucratoare']
                        nr_zile_n = self.zile_lucratoare_nelucratoare[f'{current_month}_nelucratoare']
                    elif current_month in [3, 4, 5]:
                        anotimp_l = 'Primavara'
                        anotimp_nl = 'Primavara.1'
                        pondere_nelucratoare = self.ponderi[0][1]
                        pondere_lucratoare = self.ponderi[0][0]
                        nr_zile_l = self.zile_lucratoare_nelucratoare[f'{current_month}_lucratoare']
                        nr_zile_n = self.zile_lucratoare_nelucratoare[f'{current_month}_nelucratoare']
                    elif current_month in [6, 7, 8]:
                        anotimp_l = 'Vara'
                        anotimp_nl = 'Vara.1'
                        pondere_nelucratoare = self.ponderi[0][3]
                        pondere_lucratoare = self.ponderi[0][2]
                        nr_zile_l = self.zile_lucratoare_nelucratoare[f'{current_month}_lucratoare']
                        nr_zile_n = self.zile_lucratoare_nelucratoare[f'{current_month}_nelucratoare']
                    elif current_month in [9, 10, 11]:
                        anotimp_l = 'Toamna'
                        anotimp_nl = 'Toamna.1'
                        pondere_nelucratoare = self.ponderi[0][5]
                        pondere_lucratoare = self.ponderi[0][4]
                        nr_zile_l = self.zile_lucratoare_nelucratoare[f'{current_month}_lucratoare']
                        nr_zile_n = self.zile_lucratoare_nelucratoare[f'{current_month}_nelucratoare']

                    if current_day in ['S', 'D'] or str(current_date) in self.zile_sarbatoare:
                        if str(current_time) == str(self.my_dict[y]['inceput']):
                            cons_1 = self.my_dict[y][anotimp_nl] * pondere_nelucratoare/nr_zile_n * monthly_qty
                            cons_intreg = int(cons_1 + self.rest)
                            new_data = [current_date, current_time, current_day,
                                        self.my_dict[y][anotimp_nl] * pondere_nelucratoare/nr_zile_n,
                                        cons_intreg]
                            self.psc_profile.append(new_data)
                            self.rest += cons_1 - cons_intreg
                    else:
                        if str(current_time) == str(self.my_dict[y]['inceput']):
                            cons_2 = self.my_dict[y][anotimp_l] * pondere_lucratoare/nr_zile_l * monthly_qty
                            cons_intreg = int(cons_2 + self.rest)
                            new_data = [current_date, current_time, current_day,
                                        self.my_dict[y][anotimp_l] * pondere_lucratoare/nr_zile_l,
                                        cons_intreg]
                            self.psc_profile.append(new_data)
                            self.rest += cons_2 - cons_intreg
            for y in range(len(self.my_dict_2)):
                total_zile_luna = int(self.zile_lucratoare_nelucratoare[f'{current_month}_lucratoare']) + \
                                  int(self.zile_lucratoare_nelucratoare[f'{current_month}_nelucratoare'])
                if self.my_dict_2[y]['PSC'] == self.selected_psc:
                    if current_month in [12, 1, 2]:
                        anotimp = 'Iarna'
                    elif current_month in [3, 4, 5]:
                        anotimp = 'Primavara'
                    elif current_month in [6, 7, 8]:
                        anotimp = 'Vara'
                    elif current_month in [9, 10, 11]:
                        anotimp = 'Toamna'
                    if str(current_time) == str(self.my_dict_2[y]['inceput']):
                        cons_3 = self.my_dict_2[y][anotimp]/total_zile_luna * monthly_qty
                        cons_intreg = int(cons_3 + self.rest)
                        new_data = [current_date, current_time, current_day,
                                    self.my_dict_2[y][anotimp]/total_zile_luna,
                                    cons_intreg]
                        self.psc_profile.append(new_data)
                        self.rest += cons_3 - cons_intreg
# # # ---------------- generate a year --------------------- #


def generate_a_year():
    year, psc = current_year_func()
    my_class = PscManagement(year, psc)
    my_class.create_year()
    my_class.get_month_and_day()
    my_class.get_ponderi()
    my_class.generate_psc()
    an_selectat = my_class.psc_profile

    full_year = pandas.DataFrame(an_selectat)
    full_year.to_excel(f'full_year_{year}_psc_{psc}.xlsx', header=['Data', 'Ora', 'Zi', f'PSC: {psc}', 'LP'])
    messagebox.showinfo(title='Info', message='File created')
# # -------------------- UI ----------------------- #


window = Tk()
window.title('Generare PSC')
window.config(padx=50, pady=50)

year_label = Label(text='Year ')
year_label.grid(row=0, column=0, padx=10, pady=10)
psc_label = Label(text='PSC no.')
psc_label.grid(row=0, column=2, padx=10, pady=10)
month_label = Label(text='Luna')
month_label.grid(row=1, column=0)

month_1 = Label(text='01')
month_1.grid(row=1, column=1)
month_2 = Label(text='02')
month_2.grid(row=1, column=2)
month_3 = Label(text='03')
month_3.grid(row=1, column=3)
month_4 = Label(text='04')
month_4.grid(row=1, column=4)
month_5 = Label(text='05')
month_5.grid(row=1, column=5)
month_6 = Label(text='06')
month_6.grid(row=1, column=6)
month_7 = Label(text='07')
month_7.grid(row=1, column=7)
month_8 = Label(text='08')
month_8.grid(row=1, column=8)
month_9 = Label(text='09')
month_9.grid(row=1, column=9)
month_10 = Label(text='10')
month_10.grid(row=1, column=10)
month_11 = Label(text='11')
month_11.grid(row=1, column=11)
month_12 = Label(text='12')
month_12.grid(row=1, column=12)

quantity_label = Label(text='Energie')
quantity_label.grid(row=2, column=0)

year_entry = Entry(width=8)
year_entry.focus()
year_entry.grid(row=0, column=1, padx=10, pady=10)
psc_entry = Entry(width=8)
psc_entry.grid(row=0, column=3)

month_1_entry = Entry(width=8)
month_1_entry.insert(0, 0)
month_1_entry.grid(row=2, column=1)
month_2_entry = Entry(width=8)
month_2_entry.insert(0, 0)
month_2_entry.grid(row=2, column=2)
month_3_entry = Entry(width=8)
month_3_entry.insert(0, 0)
month_3_entry.grid(row=2, column=3)
month_4_entry = Entry(width=8)
month_4_entry.insert(0, 0)
month_4_entry.grid(row=2, column=4)
month_5_entry = Entry(width=8)
month_5_entry.insert(0, 0)
month_5_entry.grid(row=2, column=5)
month_6_entry = Entry(width=8)
month_6_entry.insert(0, 0)
month_6_entry.grid(row=2, column=6)
month_7_entry = Entry(width=8)
month_7_entry.insert(0, 0)
month_7_entry.grid(row=2, column=7)
month_8_entry = Entry(width=8)
month_8_entry.insert(0, 0)
month_8_entry.grid(row=2, column=8)
month_9_entry = Entry(width=8)
month_9_entry.insert(0, 0)
month_9_entry.grid(row=2, column=9)
month_10_entry = Entry(width=8)
month_10_entry.insert(0, 0)
month_10_entry.grid(row=2, column=10)
month_11_entry = Entry(width=8)
month_11_entry.insert(0, 0)
month_11_entry.grid(row=2, column=11)
month_12_entry = Entry(width=8)
month_12_entry.insert(0, 0)
month_12_entry.grid(row=2, column=12)

generate_button = Button(text='Generate file', command=generate_a_year)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
close_button = Button(text='Close', command=window.destroy)
close_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
