import sqlite3
import pandas as pd

# Path to the CSV file and the SQLite database
csv_file_path = './studentInfo.csv'
db_path = './db.sqlite3'

# Load the CSV file into a pandas DataFrame and select the first 50 rows
student_info_df = pd.read_csv(csv_file_path).head(50)

# Connect to the SQLite database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Prepare the data insertion query
insert_query = """
INSERT OR IGNORE INTO dashboard_studentinfo (
    code_module, code_presentation, id_student, gender, region,
    highest_education, imd_band, age_band, num_of_prev_attempts,
    studied_credits, disability, final_result
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# Insert data into the 'dashboard_studentinfo' table
data_to_insert = student_info_df.values.tolist()
cursor.executemany(insert_query, data_to_insert)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("The first 50 rows of data have been inserted successfully!")
