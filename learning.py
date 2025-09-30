import  pandas as pd
import duckdb

# 1️⃣ Users dataset
users = pd.DataFrame({
    "user_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "email": ["alice@mail.com", "bob@mail.com", "charlie@mail.com"]
})

# 2️⃣ Orders dataset
orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "user_id": [1, 2, 1, 3],
    "product": ["Laptop", "Phone", "Headphones", "Tablet"],
    "amount": [1200, 800, 200, 600]
})

# 3️⃣ Delivery dataset
delivery = pd.DataFrame({
    "delivery_id": [1001, 1002, 1003, 1004],
    "order_id": [101, 102, 103, 104],
    "status": ["Delivered", "Shipped", "Pending", "Delivered"],
    "city": ["New York", "LA", "Chicago", "Houston"]
})

print(delivery.filter("status","=", "Delivered"));




