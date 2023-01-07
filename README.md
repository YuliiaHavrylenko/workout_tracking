<h1 align="center">WORKOUT TRACKER</h1>

## Description
This app allows a user to track their workouts by inputting the exercise they did and recording the details (duration, calories burned) in a Google Sheets spreadsheet. 

### About the project.
The app uses the Nutritionix API to retrieve the duration and calories burned for the inputted exercise, and the Sheety API to add a new row to a Google Sheets spreadsheet with the date, time, exercise name, duration, and calories burned.

## Project setup
To set up and run this script, you will need to do the following:

1. Obtain API keys for the Nutritionix and Sheety APIs. You will need to create an account and a new app for each API to receive your API keys.
2. Replace the placeholder values for APP_ID, API_KEY, USER_ID, PASS, GENDER, WEIGHT_KG, HEIGHT_CM, and AGE in the script with your own values.
3. Replace the placeholder value for the nutritionix_endpoint and add_row_endpoint variables with the appropriate URLs for the Nutritionix and Sheety APIs.
4. Run the script using a Python interpreter. The user will be prompted to input the exercise they did, and the script will retrieve the duration and calories burned for that exercise using the Nutritionix API. The script will then add a new row to the specified Google Sheets spreadsheet with the date, time, exercise name, duration, and calories burned using the Sheety API.