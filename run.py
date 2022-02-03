import gspread
from google.oauth2.service_account import Credentials
import calendar

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("feedback-form-pp3")

def get_month():
    """
    Collate the scores for each area in the feedback form
    based on the month selected by the user.
    """

    while True:
        print("Please enter the month that you would like to view the feedback for...\n")
        print("Note that months are numbered, e.g 1 = January, 2 = February... 11 = November\n")

        month_chosen_str = input("Enter your choice of month here: ")
        
        if(check_month(month_chosen_str)):
            print("Valid month chosen.")
            break

    return int(month_chosen_str)


def check_month(month):
    """
    Check the user has inputted a valid month when prompted.
    It must be an integer between 1 - 12 inclusive.
    """
    try:
        month_chosen_num = int(month)
        if(month_chosen_num < 1 or month_chosen_num > 12):
            raise ValueError(
                f"The number entered must be between 1 and 12. You entered: {month_chosen_num}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False
    
    return True


def get_scores(month):
    """
    Access the google sheet and return all of scores for each different
    area as a comma separated list of values. 
    """
    month_chosen_name = calendar.month_name[month]
    print(f"Gathering data for the month: {month_chosen_name}...\n")
    month_worksheet = SHEET.worksheet(month_chosen_name)
    month_data = month_worksheet.get_all_values()

    columns = []
    headers = month_worksheet.row_values(1)[2:10]
    for num, header in zip(range(3,11), headers):
        score = month_worksheet.col_values(num)[1:]
        print(f"{header}:  {score}")

    print(f"Month data: {month_data}")
    print(f"Headers: {headers}")


month = get_month()
print(month)
test_data = get_scores(month)
# print(test_data)
# month_chosen_name = calendar.month_name[month_chosen_num]