# Allana - Feedback Form Portfolio Project 3 with Code Institute


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


## Technologies Used


## Testing

### Manual Testing

### Bugs and Fixes

### User Testing

### Validation


## Deployment


## Credits and Acknowledgements