import pandas as pd
import duckdb   # 🦆

mydataset = {
    'cars': ["BMW", "Volvo", "Ford", "Audi"],
    'passings': [3, 7, 2, 5],
    'milage': [25, 34, 38, 29]
}

cars = pd.DataFrame(mydataset)

result = duckdb.query( "Select * from cars where milage > 25 and passings > 4;").to_df()

print(result)
