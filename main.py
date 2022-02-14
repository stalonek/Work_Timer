from datetime import date, datetime
from Time_Class import TimeCreator
import xlsxwriter
import os.path
import pandas as pd


if os.path.exists('C:/Users/ssojka/PycharmProjects/Work_timer/time_sheet.xlsx'):
    pass

else:
    print('File not exist.... creating file')
    excel_file = xlsxwriter.Workbook('time_sheet.xlsx')
    excel_file.close()

df = pd.read_excel('time_sheet.xlsx')

def updating_dummy_excel():
    global df
    if df.empty:
        print("creating a file with updates")
        df = pd.DataFrame(
            {"Date": ['dzisiaj', 'jutro', 'pojutrze'],
             "Topic": ['python1', 'klasy2', 'cos innego']}
        )
        print(df.columns)
        df.to_excel('time_sheet.xlsx')

    else:
        print(f'File is not empty')


condition = True


while condition:
    print(f'Hello please select what do You want to do: \n'
          'Start learning -> 1 \n'
          'Quit program -> 2 \n')

    user_input = int(input("Use a keyboard to select an option ...\n"))
    print(f'User has selected {user_input}\n')

    if user_input == 1:

        updating_dummy_excel()
        condition = False

    else:
        print('quitting program')
        condition = False









# today = datetime.now()
#
#
# entry1 = TimeCreator('Python', today)
#
# print(repr(entry1))
