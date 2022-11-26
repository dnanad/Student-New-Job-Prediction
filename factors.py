import csv
import streamlit as st
import pandas as pd

# Import DictWriter class from CSV module
from csv import DictWriter


if __name__ == "__main__":
    # make an application
    st.title(
        "Factors related to getting the first job for the froien (master)students")
    st.write(
        "Kindly select Yes/No for the factors that you think are important in getting the first job. ")

    stream = st.selectbox(
        "Does the studnet's stream of study have a direct relation to the job?", ["No", "Yes"])
    uni = st.selectbox("Dose the university matters?", ["No", "Yes"])
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
        "other": other
    }

    field_names = ["stream", "uni", "grade", "old_job", "internship",
                   "num_experience", "age", "thesis", "projects", "language", "network", "other"]
    if st.button('Save the information'):
        with open('stud_data.csv', 'a', newline='') as f_object:
            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            # Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(input_dict)
        st.success("Data saved successfully")
