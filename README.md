# 📊 Data Redundancy Removal System

## 📌 Overview

This project was developed as part of the CodeAlpha Cloud Computing Internship.
The system identifies and removes duplicate data entries, ensuring that only unique and valid data is retained.

## 🎯 Objective

To design a simple data validation mechanism that prevents redundancy and improves data accuracy.

## 🚀 Features

* Accepts user input as comma-separated values
* Identifies duplicate entries
* Removes redundant data
* Displays both unique data and removed duplicates
* Lightweight and efficient

## 🛠 Technologies Used

* Python 3

## 🧠 Working Principle

1. User inputs data separated by commas
2. Input is converted into a list
3. Each item is checked:

   * If not present → added to unique list
   * If already present → marked as duplicate
4. Final output displays cleaned data

## ▶️ How to Run

1. Open terminal in project folder
2. Run the command:
   python data_cleanup.py
3. Enter data when prompted

## 📊 Example

Input:
a, b, a, c, b

Output:
Unique Data: ['a', 'b', 'c']
Removed Duplicates: ['a', 'b']

## 📂 Project Structure

CodeAlpha_DataRedundancy/
│
└── data_cleanup.py

## 💡 Applications

* Data preprocessing
* Database cleaning
* Removing duplicate records

## 🔮 Future Improvements

* Add file input (CSV support)
* Integrate with database
* Build UI for visualization

## 🙌 Acknowledgement

This project was completed as part of the CodeAlpha Internship program.
