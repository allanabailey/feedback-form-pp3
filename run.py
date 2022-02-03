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

def get_scores():
    """
    Collate the scores for each area in the feedback form
    based on the month selected by the user.
    """
    print("Please enter the month that you would like to view the feedback for...\n")
    print("Note that months are numbered, e.g 1 = January, 2 = February... 11 = November\n")

    month_chosen_str = input("Enter your choice of month here:\n")
    check_data(month_chosen_str)


def check_data(scores):
    """
    Check the user has inputted a valid month when prompted.
    It must be an integer between 1 - 12 inclusive.
    """
    try:
        month_chosen_num = int(scores)
        if(month_chosen_num < 1 or month_chosen_num > 12):
            raise ValueError(
                f"The number entered must be between 1 and 12. You entered: {month_chosen_num}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
    # print(scores)

get_scores()
# month_chosen_name = calendar.month_name[month_chosen_num]