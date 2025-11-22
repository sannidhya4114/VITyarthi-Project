VITyarthi Mess Comparison Tool
💡 Overview of the Project
The VITyarthi Mess Comparison Tool is a simple Python script designed to help college students compare 
food options across various campus messes (cafeterias). It reads pricing and rating data from structured 
Excel files and allows the user to quickly identify the cheapest mess for a specific dish or the mess 
offering the best-rated version of that dish.

✨ Features
Price Comparison: Automatically finds and displays the mess offering the minimum price for each dish listed.

Rating Comparison: Automatically finds and displays the mess with the maximum rating for each dish listed.

Interactive Menu: Provides a command-line interface for the user to select whether they want to compare prices or ratings.

Data Processing: Utilizes the robust pandas library for efficient data ingestion and manipulation from Excel files.

💻 Technologies/Tools Used
Language: Python 3.x

Libraries: pandas (for data manipulation) and openpyxl (pandas dependency for reading .xlsx files).

Data Format: Microsoft Excel (.xlsx files).

🛠️ Steps to Install & Run the Project
Prerequisites

You must have Python 3.x installed on your system.

1. Install Dependencies

Open your terminal or command prompt and install the necessary Python libraries:

Bash
pip install pandas openpyxl
2. File Setup

Ensure the following three files are present in the same directory:

VITyarthi project.py (The main script)

Price.xlsx (Excel file for prices)

Rating.xlsx (Excel file for ratings)

3. Run the Script

Execute the main Python file from your terminal:

Bash
python "VITyarthi project.py"
🧪 Instructions for Testing
After running the script, the program will prompt you for input:

Enter the no. to comparison price and ratings: 1.Price 2.Ratings
Test Case 1: Price Comparison

Input: Enter 1.

Expected Output: The script should iterate through all dishes and print the cheapest mess and its price for each dish.

Example Output: Dosa: Cheapest at Mess B (₹30)

Test Case 2: Rating Comparison

Input: Enter 2.

Expected Output: The script should iterate through all dishes and print the best-rated mess and its rating for each dish.

Example Output: Dosa: Best rated at Mess A (4.2 stars)

