# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY ./frontend /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8501

# Run the Streamlit app when the container launches
CMD ["streamlit", "run", "streamlit.py"]
