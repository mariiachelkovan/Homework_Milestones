import csv
import random
from faker import Faker

fake = Faker()

num_employees = 100

departments = ["HR", "Finance", "Engineering", "R&D", "Sales"]

with open("database.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Hire Date", "Department", "Birthday"])
    for _ in range(num_employees):
        name = fake.name()
        hiring_date = fake.date_between(start_date='-20y', end_date='today')
        department = random.choice(departments)
        birthday = fake.date_of_birth(minimum_age=20, maximum_age=60)
        writer.writerow([name, hiring_date, department, birthday])

print(f"{num_employees} employee records generated in 'database.csv'")
