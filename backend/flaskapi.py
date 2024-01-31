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

# Attempt to connect using various host options
hosts_to_try = ["172.24.0.2", "172.24.0.3", "localhost", "mysql", "127.0.0.1", "0.0.0.0"]

for host_to_try in hosts_to_try:
    try:
        db_connection = connect(
            host=host_to_try,
            user="root",
            port=3306,
            password="root",
            database="labdata"
        )
        print(f"Database connection successful using host: {host_to_try}")
        print(cursor)  # Print the cursor object itself
        cursor = db_connection.cursor()
        break  # Exit the loop if a successful connection is made

    except Exception as e:
        print(f"Database connection error using host {host_to_try}: {str(e)}")

if cursor is None:
    print("Unable to establish a connection to the database.")

@app.route('/degree', methods=['GET'])
def get_degrees():
    try:
        # Execute a SELECT query to fetch degree data from the database
        cursor.execute("SELECT * FROM degree")
        degree_data = [{'id': id, 'value': value} for id, value in cursor.fetchall()]
        print(degree_data)
        return jsonify(degree_data), 200
    except Exception as e:
        print(f"Error fetching degree data: {str(e)}") 
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
        print(f"Error fetching timestamp data: {str(e)}") 
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
