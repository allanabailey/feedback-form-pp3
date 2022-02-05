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

    scores = []
    scores_with_headers = {}
    headers = month_worksheet.row_values(1)[2:10]

    for num, header in zip(range(3,11), headers):
        score = month_worksheet.col_values(num)[1:]
        scores.append(score)
        for score in scores:
            int_score = [int(num) for num in score]
            scores_with_headers[header] = int_score

    return scores_with_headers


def present_data(score_data):
    """
    Collate the data and present it to the user in a more readable format.
    """
    for key, value in score_data.items():
        print(key, " : ", value)
    print("\n")

def calculate_average(score_data):
    """
    Using the dictionary created containing all of the headers and scores,
    calculate the average score for each area
    """
    print("Calculating average scores...\n")
    average_dict = {}
    for key, value in score_data.items():
        average_dict[key] = sum(value) / float(len(value))

    print("Average scores: \n")
    present_data(average_dict)
    
    return average_dict


def check_if_update(question):
    """
    Check to see if the user would like to update the worksheet with these averages
    or wait until a later date.
    """
    ans = input(question).strip().lower()
    try:
        if(ans not in ["y", "n"]):
            raise ValueError(
                f"Please enter either 'y' for Yes, or 'n' for No. You entered: {ans}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return check_if_update(question)

    if(ans == "y"):
        update_worksheet(month, average_scores)
    else:
        print("Spreadsheet not updated.")


def update_worksheet(month, average_scores):
    """
    Update the 'Averages' worksheet with the averages of the month the user is
    currently investigating.
    """
    print("Updating 'Averages' worksheet...\n")
    avg_worksheet = SHEET.worksheet("Averages")
    cell = avg_worksheet.find(calendar.month_name[month])
    row = cell.row

    averages = []
    colno = 2
    i = 0
    for key, value in average_scores.items():
        averages.append(value)
        avg_worksheet.update_cell(row, colno, averages[i])
        colno += 1
        i += 1

    print("Worksheet updated successfully.\n")



month = get_month()
score_data = get_scores(month) # Dictionary with header and scores
print("All scores for the month...\n")
data_for_user = present_data(score_data) # Print scores in a readable format to the user
average_scores = calculate_average(score_data) # Calculate averages and present to the user
update_yes_no = check_if_update("Would you like to update the worksheet with the averages? (y/n): ")