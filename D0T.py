from datetime import datetime
now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print('Current course in the Universe: ' + mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

print('Hello Boss')
print('What is your name')
yourName = input()
print('It is good to meet you, ' + yourName)
print('What is your Age, ' + yourName)
yourAge = input()

from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = 42

# Rows can also be appended
ws.append([1, 2, 3])

# Python types will automatically be converted
ws['A2'] = datetime.now()

# Save the file
wb.save("sample.xlsx")