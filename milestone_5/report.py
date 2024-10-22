import csv
from datetime import datetime
import sys
from collections import defaultdict


def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        employees = [row for row in reader]
    return employees


def get_birthdays_and_anniversaries(employees, month):
    birthdays = defaultdict(list)
    anniversaries = defaultdict(list)
    
    for employee in employees:
        birthday = datetime.strptime(employee['Birthday'], '%Y-%m-%d')
        hire_date = datetime.strptime(employee['Hire Date'], '%Y-%m-%d')
        
        if birthday.strftime('%B').lower() == month:
            birthdays[employee['Department']].append(employee['Name'])
        
        if hire_date.strftime('%B').lower() == month:
            anniversaries[employee['Department']].append(employee['Name'])
    
    return birthdays, anniversaries


def print_report(month, birthdays, anniversaries, verbose=False):
    print(f'Report for {month.capitalize()} generated')
    
    print('--- Birthdays ---')
    total_birthdays = sum(len(v) for v in birthdays.values())
    print(f'Total: {total_birthdays}')
    for department, names in birthdays.items():
        print(f'- {department}: {len(names)}')
        if verbose:
            print('  ', ', '.join(names))
    
    print('--- Anniversaries ---')
    total_anniversaries = sum(len(v) for v in anniversaries.values())
    print(f'Total: {total_anniversaries}')
    for department, names in anniversaries.items():
        print(f'- {department}: {len(names)}')
        if verbose:
            print('  ', ', '.join(names))


def main():
    if len(sys.argv) < 3:
        print("Usage: python report.py <database.csv> <month> [-v]")
        return
    
    filename = sys.argv[1]
    month = sys.argv[2].lower()
    verbose = '-v' in sys.argv
    
    employees = load_data(filename)
    birthdays, anniversaries = get_birthdays_and_anniversaries(
        employees, month)
    print_report(month, birthdays, anniversaries, verbose)


if __name__ == '__main__':
    main()
