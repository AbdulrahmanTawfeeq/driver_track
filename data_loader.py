import pandas as pd

class DataLoader:
    def __init__(self, trip_file_path, driver_file_path):
        self.trip_file_path = trip_file_path
        self.driver_file_path = driver_file_path

    def load_trip_data(self):
        """Load and preprocess the trip data."""
        data = pd.read_excel(self.trip_file_path)
        # Convert the 'In Date' and 'Out Date' columns to datetime objects
        data['In Date'] = pd.to_datetime(data['In Date'], errors='coerce', format='%d-%m-%Y %I:%M %p')
        data['Out Date'] = pd.to_datetime(data['Out Date'], errors='coerce', format='%d-%m-%Y %I:%M %p')
        return data

    def load_driver_data(self):
        """Load the driver information from the Excel file."""
        driver_data = pd.read_excel(self.driver_file_path)
        # Ensure the columns match: Driver Name, Branch, Vehicle Type
        driver_data = driver_data[['Driver Name', 'Branch', 'Vehicle Type']]
        return driver_data