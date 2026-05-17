import os
import matplotlib.pyplot as plt
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, 'expense.csv')

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH, index_col='Date')
else:
    df = pd.DataFrame(columns=['Category', 'Venue', 'Amount'])
    df.index.name = 'Date'
    df.to_csv(CSV_PATH)

print(df)

def save_expenses():
    df.to_csv(CSV_PATH)


def add_expense():
    date = input('Enter the date (YYYY-MM-DD): ')
    category = input('Enter the category of expense: ')
    venue = input('Enter the venue of expense: ')

    try:
        amount = float(input('Enter the amount spent: '))
    except ValueError:
        print('Invalid amount. Please enter a number.')
        return

    df.loc[date] = [category.capitalize(), venue.capitalize(), amount]
    save_expenses()
    print('Expense added successfully.')


def view_expenses():
    if df.empty:
        print('No expenses recorded yet.')
    else:
        print(df)


def plot_expenses():
    category = input('Enter the category to plot: ').capitalize()
    if category in df['Category'].values:
        category_data = df[df['Category'] == category]
        plt.bar(category_data.index, category_data['Amount'])
        plt.xlabel('Date')
        plt.ylabel('Amount Spent')
        plt.title(f'Expenses for {category}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print('Category not found.')


while True:
    print('\nChoose an option:')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Plot Expenses by Category')
    print('4. Exit')

    choice = input('Enter your choice (1/2/3/4): ')

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        plot_expenses()
    elif choice == '4':
        break
    else:
        print('Invalid choice. Please try again.')
