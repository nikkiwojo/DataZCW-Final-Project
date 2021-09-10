# DataZCW-Final-Project
Capstone project for ZCW Data Engineering course.

## Overview of Final Project - Nikki's Brewery

- "Nikki's Brewery" is a recommendation app that runs in the terminal and helps you find a craft beer based on your favorite flavors
- The app will ask you to choose from two different lists of flavor profiles, then recommend five new craft beers for you to try
- The five beers are randomly chosen from a specific list, so you can re-roll for a new list if desired
- Along with a list, the user will be given a simple bar graph that compares the ABV values of the five beers that are given
- "Nikki's Brewery" also has an option that allows users to find a brewery near them
- The user enters their city and state, and the program will show them a list of breweries in their area, along with the address, phone number, and website 

## Languages and Frameworks Used

- Python, SQLite, Pandas, Matplotlib, Jupyter Notebook, Apache Airflow

## How it works

- Run "python3 main.py" in the command line
- The data is imported and organized using pandas, then stored in a SQLite database
- Part of the table is extracted based on your choices, using SQL queries
- The data is presented to the user as a dataframe
- If you choose to find new beers to try, the abv values are displayed in a simple bar graph that is created using matplotlib
- The brewery data is extracted from an API and is narrowed down by city, which is then organized by state


  
  
  
