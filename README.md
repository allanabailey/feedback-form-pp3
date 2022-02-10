# Allana - Feedback Form Portfolio Project 3 with Code Institute
[Live Site: ](https://feedback-form-pp3.herokuapp.com/)
[Google Sheet: ](https://docs.google.com/spreadsheets/d/1SuufnXVcUSAv-D7TQ263iKqIZ6QtZMmzCQ3DEbpjX1U/edit?usp=sharing)
[Google Form: ](https://forms.gle/rwPaeUjjCHc74TEw5) 

## Brief Overview  
This project was created as part of Code Institute’s Diploma in Full Stack Software Development. This is portfolio project 3, a project requiring us to create a back end application in Python and deploy it on Heroku. The deployed site can be found [here](https://feedback-form-pp3.herokuapp.com/).
  
![Spreadsheet Collecting all Feedback](/assets/images/features/all-responses-worksheet.png) 

### Description
A web application built and designed for business owners and/or those in the hospitality industry to gather, enter and analyse feedback from customers more easily than traditional manual processes. It has been designed to work in conjunction with both manually and digitally submitted forms and present average scores to the user to provide useful insights into their business and custom satisfaction.

### Features
As a back end web application, there are no front end features as this utilises the template terminal supplied by Code Institute. However the application itself provides a mixture of average scores, analyses the highest and lowest scores of the organisation, and produces both a readable print for users, as well as updating a user friendly google sheet that would be accessible to all in a real world application.

### Goals
* Application Goals:
    * Provide users with an option to manually enter feedback data not submitted digitally via the google form.
    * Allow users/companies to easily identify their highest and lowest scoring areas on a monthly basis.
    * Provide insights to areas of improvement for companies.
    * Offer a more user-friendly view of data via an updated google sheet linked to both the terminal application and the google forms submitted.
  
* Personal Goals:
    * Create a back end web application using Python for my portfolio.
    * Build on and improve my knowledge in Python.
    * Learn about the various libraries and modules available in Python.
    * Become comfortable with the deployment process on Heroku.
    * Create a back end web application with potential real world application.


## Users
Companies/Clients could use this application to:
* Gain useful insights into areas succeeding/failing in their business.
* Analyse customer feedback to implement improvements in areas that are underperforming.
* View statistics on a month by month basis to identify problem areas and to ascertain if new implementations or procedures that have been put in place have increased customer satisfaction.
* Allow customers to submit feedback both manually and digitally.
* Update a user friendly interface (google sheetws) for all members of the organisation to be able to review the feedback.

### User Stories
* As a company I would like customers to be able to submit feedback forms easily so that we can improve our customer satisfaction and ensure good business.
* As a company I would like to be able to view the overall and average scores in different areas of the business to easily identify areas that need to improve.
* As a company I would like to easily identify my highest and lowest scoring areas so that focus can be placed on these in the future.
* As a customer I would like to be able to submit my form once I get home online so that I don't have to stand and fill out a form before leaving.
* As a customer I would like to be able to hand a paper feedback form back to the organisation as I do not own a computer at home.


## Project Flow and Purpose
### Purpose and Real World Application
The main purpose of this project was to build an application that could be **used by organisations** to **gather feedback from customers** in all different areas of the business. Customers would be able to fill out both **online and paper feedback forms**, both of which interact and work with the application. 
  
The **google sheet** allows for a more **user-friendly** view of the data which can be **updated from the application** or **automatically from online google forms submitted**. The application has been designed to **present data in a readable format** to the user, however the google sheet allows for a broken-down view on a **month by month** basis, as well as a sheet dedicated to **average scores**.
  
The project was based on an **outdoor activity centre** with the initial data showcasing the importance of custom feedback. For example the **first 5 scores (Jan - May)** could illustrate the following reasons behind the feedback gathered:
* January - Washing and showering facilities were the lowest scoring areas, however a new shower block was built for February where the scores can be seen to have improved.
* February - A new staff member was taken on and was still in training for the month, explaining the low score for staff knowledge.
* March - There was an issue with stock in the on-site shop resulting in a lack of choice and quantity of items for many customers, resulting ina  low average for shop scores.
* April - The stock issue was resolved, and the new staff member now fully trained, so all scores improved with very high overall averages across the different areas.
* May - Due to bad weather and an issue with the address not being registered with the post office, only half of the car park was utilised, and many customers were unable to find the site with their sat navs / google maps. This resulted in a low score for the venue.

### Flow and Processes
Prior to starting the project, a **rough flow chart** was created using **pen and paper** to begin understanding the **logic and flow** of the project. A more comprehensive and digital flowchart was then created using **Lucid Chart** as seen below.
  
![Flow Chart by Lucid Chart](/assets/images/flow-chart/flow-chart.png) 


## Features
* User Interface
    * The user interface of the terminal is the standard template **designed and created by Code Institute**.
  
![User Interface](/assets/images/features/user-interface.png) 
  
* Terminal Scores and Data
    * In addition to the **google sheet** providing a user-friendly presentation of the data, the terminal has been designed to **print scores and data to the user in a readable format** with a dedicated **present_data()** function.
  
![Terminal Scores and Data](/assets/images/features/scores-presented-to-user.png) 
  
* Main Google Sheet with All Scores Recorded
    * The first and main sheet of the **google sheet** contains **every single slice of feedback data** ever submitted and entered for **all months**. This is a very **user-friendly** presentation of the data which is **automatically updated**. This would currently only be suitable for months **within the same year** but this is expanded on in the **future implementations** section of the readme.
  
![Main Google Sheet with All Scores](/assets/images/features/all-responses-worksheet.png) 
  
* Google Sheet Displaying Averages
    * Once the user or company is happy that **all feedback for the month** has been **collected and inputted** there is an option to **update the averages worksheet**. This shows all **12 months, side-by-side, across all areas** to allow for a user-friendly view of data and **ease of analysis**. This worksheet can be **updated again if further feedback is received** by the user simply returning to the application and updating the same month again.
  
![Averages Sheet](/assets/images/features/averages-worksheet.png)

* Monthly Sheets
    * By using a **query** on the first cell of the **monthly sheets**, data for each month can be vewed **individually** and is **updated automatically from the main AllResponses sheet**. Whilst this could have been achieved with code and iteration for the scores, this allowed for a more desireable **user interface and display** to the user which was more appropriate in a **real world application**
  
![Monthly Sheets](/assets/images/features/monthly-worksheet.png)


## Future Implementations
* Cater for expansion of data collection for **more than one year** as it currently only distinguishes by month and not year.
* Allow users to **compare one month against another** to see improvements or the affects or any implementations undertaken by the organisation / company have had.
* Allow users to interact with the application and gain insight into feedback for a **collection of months e.g January - March** to allow more seasonal business better data analysis.
* The use of **Pandas DataFrames** would allow for better iteration over large data sets and control over data anlysis.
* Implement the ability to **share and compare data** between different company sites where an organisation may have **multiple branches**.


## Technologies Used
* Programming Languages Used: Python
* [GitPod](https://gitpod.io)
    * GitPod was used as the IDE to develop and write the project which was then pushed to GitHub.
* [GitHub](https://github.com/)
    * GitHub was used for version control and to host the pushed code which was then deployed to Heroku.
* [Heroku](https://www.heroku.com/)
    * Heroku was used as a PaaS to deploy the application.
* [Google Forms](https://www.google.co.uk/intl/en-GB/forms/about/)
    * Google Forms was used to create the feedback form for customers to submit digitally.
* [Google Sheets](https://www.google.co.uk/intl/en-GB/sheets/about/)
    * Google Sheets was used to display and update data in a user-friendly manner.
* [Gyazo](https://gyazo.com/en)
    * Gyazo was used to take screenshots and create the images.


## Testing

### Manual Testing
* For each addition to the code, multiple **print** statements were implemented to test the **values of variables** and whether **functions were being called correctly**.
* For every **data validaiton** step, both correct and incorrect data was supplied to the application to check that **errors were handled correctly**. This would include offering strings, characters and integers where they were both expected and unexpected.
* All **routes of the flow** of the application were undertaken where the user was given an **option to update or enter** data, for all possible scenarios.
* All of the above was completed both **before and after initial deployment** to ensure the deployment did not alter the workings of the application.

### Bugs and Fixes
* Initially when checking that the user inputted a month value **between 1 and 12** a range method was used. However, this did not work for all cases and so this was changed to a **logical condition** where it checked whether the value was greater than **or** smaller than these figures. As well as resolving the issue, this also made the code more readable.
* When choosing the option to **update the averages sheet**, the data was updating the row below the one intended when using this statement alone:
    * avg_worksheet.update_cell(row, colno, averages[i])
    * To resolve this, these variables were implemented:
        * colno = 2
        * i = 0
    * Which incremeneted on each iteration of the list, setting the row to be:
        * cell = avg_worksheet.find(calendar.month_name[month])
        * row = cell.row
* Following passing my code through **PEP8 validation** I removed multiple trailing white spaces, reduced line length, and removed unneeded parentheses to ensure my code exhibited **best coding practices**.

### User Testing
Once I had completed my own testing of the application, I asked three different people to use the application as a form of **User Testing** to check that both correct and incorrect use resulted in the **intended output** and to **offer suggestions for improvements** and/or identify areas that were not clear. The following areas were improved and altered based on feedback:
* Altered some of the **print statements to be on multiple lines** rather than one long line to more clearly state instructions and prevent overflow.
* Improve the **error messages** to be more **readable** by a generic user that is not knowledgeable of computing factors such as base 10 or literal ints.
* Added a print statement explaining the **order of areas for manual scores** implemented by the user so that it was clear what each of the 8 scores represented.

### Validation
All of my python code in the **run.py** file was passed through the **PEP8 Validator** and corrections made until all errors and warnings were gone.
  
![PEP8 Validation](/assets/images/testing/pep8-validation.png)


## Deployment
This project was developed in [GitPod](https://gitpod.io) where everything was committed and pushed to [GitHub Repository](https://github.com/allanabailey/feedback-form-pp3) using the built in capabilties. The Code Institute offered a [template](https://github.com/Code-Institute-Org/python-essentials-template) which could then be pulled and used for the main structure of the repository, and created into a GitPod repository by using this as a template. The main deployment was then completed on [Heroku](https://www.heroku.com/). Please see the process followed below for deployment:
1. Add newline (\n) characters to any input statements to ensure the deployed code worked in the template application terminal.
2. Create a list of dependencies into requirements.txt by running the python3 freeze > requirements.txt command.
3. Commit these final changes to GitHub.
4. Create a new app on Heroku.
5. Add the appropriate ConfigVars under the "Settings" section to include the creds.json information stored in git.ignore, as well as the additional key,value information provided. This part allowed access to the APIs used to access the google forms and google sheets utilised.
6. Add the python and nodejs buildpacks to the application.
7. Connect the appropriate GitHub repository to the application.
8. Click manual deploy for the first deployment, with a further manual deployment being undertaken after all updates to the project have been finalised.


## Credits and Acknowledgements
I would like to thank my **mentor Miguel Martinez at Code Institute** for all of the support and calls throughout the duration of the project and providing feedback throughout.

I would also like to thank **Code Institute** for providing a brilliant course and to all of the **fellow students** for their additional support and encouragement in the slack community. The Code Institude provided a fanstastic **walkthrough project** which this project could be largely based on as well as multiple **useful lessons** as part of the **diploma in full stack software development**.
  
I would also like to say thank you to the **tutor, John at Code Institute** who helped explain the Heroku deployment process.
  
The following links below are all of the sites I visited for help with understanding the different python concepts and ideas for the code:
* [Stack Overflow Article](https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers) - Checking numbers between a certain range.
* [DelftStack Article](https://www.delftstack.com/howto/python/python-add-to-dictionary-in-loop/) - Adding to a dictionary within a loop.
* [Geeks for Geeks Article](https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/) - Printing a comma separated list of ints rather than displaying them as a list.
* [Stack Overflow Article](https://stackoverflow.com/questions/30687244/python-3-4-how-to-get-the-average-of-dictionary-values) - Calculating averages within a dictionary
* [Code Forests Article](https://www.codeforests.com/2020/11/22/gspread-read-write-google-sheet/) - Updating a specific row of a google sheet.
* [Timestamp Online](https://timestamp.online/article/how-to-convert-timestamp-to-datetime-in-python) - Printing and creeating a timestamp for the current date and time in a particular format.