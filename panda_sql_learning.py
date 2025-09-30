# pip install pandasql


import pandas as pd
from pandasql import sqldf

mydataset = {
  'cars': ["BMW", "Volvo", "Ford", "Audi"],
  'passings': [3, 7, 2, 5],
  'milage': [25, 34, 38, 29]
}

cars = pd.DataFrame(mydataset)

query = "Select * from cars where milage > 25 and passings > 4;"
result = sqldf(query,locals())

print(result)

