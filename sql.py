import pandas as pd
import mysql.connector

# Read the Excel file
df = pd.read_excel('dataset.xlsx')

# Establish a database connection
db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="candidates_db"
)
cursor = db_conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS candidates (
    Name VARCHAR(255),
    Contact_Details VARCHAR(255),
    Location VARCHAR(255),
    Job_Skills TEXT,
    Experience TEXT,
    Projects TEXT,
    Comments TEXT
);
''')

# Insert data into the table
for index, row in df.iterrows():
    cursor.execute('''
    INSERT INTO candidates (Name, Contact_Details, Location, Job_Skills, Experience, Projects, Comments)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', tuple(row))

# Commit the transaction
db_conn.commit()

# Close the cursor and connection
cursor.close()
db_conn.close()

print("Data inserted successfully.")
