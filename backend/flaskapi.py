import os
from flask import Flask, jsonify
from mysql.connector import connect
from datetime import datetime

app = Flask(__name__)

# Load database configuration from environment variables
user = os.environ.get("user")
password = os.environ.get("password")
db_hostname = os.environ.get("db_hostname")

if user is None or password is None or db_hostname is None:
    raise ValueError("Database environment variables not set")

# Debugging print statements
print(f"db_hostname: {db_hostname}")
print(f"user: {user}")
print(f"password: {password}")

# Define the cursor variable outside of the try block
cursor = None

try:
    db_connection = connect(
        host="mysql",
        user="root",
        port=3306,
        password="root",
        database="labdata"
    )
    print("Database connection successful")  # Add this print statement

    # Create a cursor for executing SQL queries
    cursor = db_connection.cursor()

except Exception as e:
    print(f"Database connection error: {str(e)}")  # Add this print statement

@app.route('/degree', methods=['GET'])
def get_degrees():
    try:
        # Execute a SELECT query to fetch degree data from the database
        cursor.execute("SELECT * FROM degree")
        degree_data = [{'id': id, 'value': value} for id, value in cursor.fetchall()]
        print(degree_data)
        return jsonify(degree_data), 200
    except Exception as e:
        print(f"Error fetching degree data: {str(e)}")  # Add this print statement
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@app.route('/timestamp', methods=['GET'])
def get_timestamps():
    try:
        # Execute a SELECT query to fetch timestamp data from the database
        cursor.execute("SELECT * FROM timestamp")
        timestamp_data = [{'id': id, 'time': time.strftime('%Y-%m-%d %H:%M:%S')} for id, time in cursor.fetchall()]
        print(timestamp_data)
        return jsonify(timestamp_data), 200
    except Exception as e:
        print(f"Error fetching timestamp data: {str(e)}")  # Add this print statement
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
