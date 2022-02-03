import gspread
from google.oauth2.service_account import Credentials
import calendar

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('feedback-form-pp3')

def get_averages():
    """
    Collate the average scores for each area in the feedback form
    based on the month selected by the user.
    """
    print("Please enter the month that you would like to view the feedback for...\n")
    print("Note that months are numbered, e.g 1 = January, 2 = February... 11 = November\n")

    month_chosen_str = input("Enter your choice of month here:\n")
    print(f"Month chosen: {month_chosen_str}")
    month_chosen_num = int(month_chosen_str)
    print(f"Month chosen: {month_chosen_num}")
    month_chosen_name = calendar.month_name[month_chosen_num]
    print(month_chosen_name)

get_averages()