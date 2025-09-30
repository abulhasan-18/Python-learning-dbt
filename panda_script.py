import pandas as pd
from tabulate import tabulate

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
    'milage' : [25,34,38]
}

myvar = pd.DataFrame(mydataset)


filtered = myvar[(myvar['milage']>25) & (myvar['passings']<6)]
print("===============================================================")
print("===============================================================")
print(tabulate(filtered, headers='keys', tablefmt='grid'))

sorted_table = myvar.sort_values(by='cars', ascending= True)
print("===============================================================")
print("===============================================================")
print(tabulate(sorted_table, headers='keys', tablefmt='grid'))

sorted_table = myvar.sort_values(by=["milage", "cars"], ascending=[False, False])
print("===============================================================")
print("===============================================================")
print(tabulate(sorted_table, headers='keys', tablefmt='grid', showindex= False))

sorted_table = sorted_table.reset_index(drop=True)
print("===============================================================")
print("===============================================================")
print(tabulate(sorted_table, headers='keys', tablefmt='grid'))