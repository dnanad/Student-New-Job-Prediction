from google.oauth2.service_account import Credentials
import csv
import streamlit as st
import pandas as pd

# Import DictWriter class from CSV module
from csv import DictWriter

from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

from datetime import datetime
import gspread

scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

path_cred = "C:/Users/DAnand/AppData/Roaming/gspread/credentials.json"

credentials = Credentials.from_service_account_file(
    path_cred,
    scopes=scopes
)

gc = gspread.authorize(credentials)
sheet = gc.open("stud_data").sheet1

# function to get current time


def date_now():
    now = datetime.now()
    mydate = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    return mydate


if __name__ == "__main__":
    # make an application
    st.title(
        "Factors related to getting the first job for the froien (master)students")
    st.write(
        "Kindly select Yes/No for the factors that you think are important in getting the first job. ")

    stream = st.selectbox(
        "Does the student's stream of study have a direct relation to the job?", ["No", "Yes"])
    uni = st.selectbox("Dose the university matter?", ["No", "Yes"])
    grade = st.selectbox("Does the student's grades matter?", ["No", "Yes"])
    old_job = st.selectbox(
        "Dose having a job in India before your first job in Germany matter?", ["No", "Yes"])
    internship = st.selectbox(
        "Does doing/not doing an internship matter?", ["No", "Yes"])
    num_experience = st.selectbox(
        "Does the number of internships?", ["No", "Yes"])
    age = st.selectbox("Does the age matter?", ["No", "Yes"])
    thesis = st.selectbox(
        "Does the student's master's thesis topic matter?", ["No", "Yes"])
    projects = st.selectbox(
        "Does the other project work matter?", ["No", "Yes"])
    language = st.selectbox(
        "Does the student's language skills matter?", ["No", "Yes"])
    network = st.selectbox(
        "Does the student's network matter?", ["No", "Yes"])
    other = st.text_input('Anything else you think could be important', None)
    date = date_now()

    input_dict = {
        "stream": stream,
        "uni": uni,
        "grade": grade,
        "old_job": old_job,
        "internship": internship,
        "num_experience": num_experience,
        "age": age,
        "thesis": thesis,
        "projects": projects,
        "language": language,
        "network": network,
        "other": other,
        "date": date
    }

    field_names = [
        "stream",
        "uni",
        "grade",
        "old_job",
        "internship",
        "num_experience",
        "age",
        "thesis",
        "projects",
        "language",
        "network",
        "other",
        "date"
    ]
    if st.button('Save the information'):
        with open('stud_data.csv', 'a', newline='') as f_object:
            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            # Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(input_dict)
            # collect = [height,sex_no,shoe_size,date_time]
            sheet.insert_row(input_dict, 2)
        st.success("Data saved successfully")
