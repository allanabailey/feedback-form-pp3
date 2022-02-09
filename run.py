import gspread
from google.oauth2.service_account import Credentials
import calendar
import time

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
        if(month.isnumeric() is False):
            raise TypeError(
                f"You must enter a number between 1 and 12. You entered: '{month}'"
            )
        month_chosen_num = int(month)
        if(month_chosen_num < 1 or month_chosen_num > 12):
            raise ValueError(
                f"The number entered must be between 1 and 12. You entered: {month_chosen_num}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False
    except TypeError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False

    return True


def check_if_manual_form(month, question):
    """
    Check to see if the user would like to update the worksheet with a new feedback form manually,
    for instance if a customer handed them a physical feedback form rather than completing the online
    google form.
    """
    ans = input(question).strip().lower()
    try:
        if(ans not in ["y", "n"]):
            raise ValueError(
                f"Please enter either 'y' for Yes, or 'n' for No. You entered: {ans}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return check_if_manual_form(month, question)

    if(ans == "y"):
        get_manual_scores(month)
    else:
        print("No manual insert needed. Moving on to calculate scores.")


def get_manual_scores(month):
    """
    Gather the scores from the user for the month they have chosen in the case where
    a physical feedback form has been returned rather than the online feedback form being filled
    out by the customer.
    """
    month_name = calendar.month_name[month]
    while True:
        print(f"Please enter the scores for {month_name}")
        print("There should be 8 numbers separated by commas all between 1 and 10. Numbers must be whole numbers")
        print("Example: 7,8,6,5,4,3,8,9\n")

        data = input("Enter your scores here:\n")

        scores_data = data.split(",")

        if validate_manual_data(scores_data):
            print("Data is valid!")
            break

    update_worksheet_manual(month, scores_data)
    return scores_data


def validate_manual_data(scores_data):
    """
    Ensure the scores submitted by the user for manually inputted feedback forms is correct.
    Numbers must be between 1 and 10.
    There must be 8 numbers separated by commas.
    Numbers must be whole numbers.
    """
    try:
        for score in scores_data:
            if(score.isnumeric() is False):
                raise TypeError(
                    f"Exactly 8 round numbers are required. You provided {scores_data}"
                )
        [int(score) for score in scores_data]
        if(len(scores_data) != 8):
            raise ValueError(
                f"Exactly 8 values are required. You provided {len(scores_data)}"
            )
        if(int(score) < 0 or int(score) > 10):
            raise ValueError(
                f"Please insert numbers between 1 and 10. You provided {score}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    except TypeError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet_manual(month, scores_data):
    """
    Update the main 'AllResponses' spreadsheet with the manual form data the user
    has inputted.
    """
    print("Updating 'AllResponses' worksheet with new manual data provided...\n")
    month_name = calendar.month_name[month]
    timest = time.gmtime()
    timestamp = (time.strftime("%d/%m/%Y %H:%M:%S", timest))
    scores = [int(score) for score in scores_data]
    data = [timestamp, month_name]
    data.extend(scores)

    worksheet_to_update = SHEET.worksheet("AllResponses")
    worksheet_to_update.append_row(data)
    print("Main responses ('AllResponses') worksheet updated successfully.\n")


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

    for num, header in zip(range(3, 11), headers):
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
    print()


def calculate_average(score_data):
    """
    Using the dictionary created containing all of the headers and scores,
    calculate the average score for each area
    """
    print("Calculating scores...\n")
    average_dict = {}
    for key, value in score_data.items():
        average_dict[key] = round((sum(value) / float(len(value))), 2)

    print("Average scores: \n")
    present_data(average_dict)

    return average_dict


def calculate_highest_score(average_scores):
    """
    Alert the user to the highest scoring area based on the averages calculated
    including all areas that have the same highest average score.
    """
    scores = average_scores.values()
    highest_score = max(scores)
    highest_scores = {}
    for key, value in average_scores.items():
        if(value == highest_score):
            highest_scores[key] = value

    print("Highest Scoring Area(s): \n")
    present_data(highest_scores)

    return highest_scores


def calculate_lowest_score(average_scores):
    """
    Alert the user to the lowest scoring area based on the averages calculated
    including all areas that have the same lowest average score.
    """
    scores = average_scores.values()
    lowest_score = min(scores)
    lowest_scores = {}
    for key, value in average_scores.items():
        if(value == lowest_score):
            lowest_scores[key] = value

    print("Lowest Scoring Area(s): \n")
    present_data(lowest_scores)

    return lowest_scores


def check_if_update(month, average_scores, question):
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
        return check_if_update(month, average_scores, question)

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


def main():
    """
    Run all functions.
    """
    month = get_month()
    check_if_manual_form(month, "Would you like to manually enter a new feedback form? (y/n): ")
    score_data = get_scores(month)
    print("All scores for the month...\n")
    present_data(score_data)
    average_scores = calculate_average(score_data)
    calculate_highest_score(average_scores)
    calculate_lowest_score(average_scores)
    check_if_update(month, average_scores, "Would you like to update the worksheet with the averages? (y/n): ")


print("Welcome to your feedback form collector and analyser!")
print("Please note that any updates are only accurate at the time of updating the worksheet, ")
print("so if any further data or feedback is collected, please return here.")
main()
