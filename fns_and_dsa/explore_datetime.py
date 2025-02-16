# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format "YYYY-MM-DD HH:MM:SS".
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates the future date, and prints it in the format "YYYY-MM-DD".
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main():
    """
    Main function to demonstrate the datetime module functionality.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
