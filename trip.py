from constants import TIME_TOLERANCE, VEHICLE_MIN_STUDENTS, MORNING_TIME_RANGE, AFTERNOON_TIME_RANGE
from utils import add_note
import pandas as pd

class Trip:
    def __init__(self, driver, trip_data):
        self.driver = driver
        self.trip_data = trip_data

    def validate_short_time_span(self, time_column, trip_type):
        """Check if all timestamps fall within an unrealistically short time span."""
        if not self.trip_data[time_column].isnull().all():
            min_time = self.trip_data[time_column].min()
            max_time = self.trip_data[time_column].max()
            if (max_time - min_time) <= TIME_TOLERANCE:
                note_key = 'short_time_span_morning' if trip_type == 'morning' else 'short_time_span_afternoon'
                add_note(self.driver, note_key)

    # def validate_time_ranges(self, time_column, time_range, trip_type):
    #     """Validate that the timestamps are within the expected time range."""
    #     for _, row in self.trip_data.iterrows():
    #         if pd.notna(row[time_column]) and not (time_range[0] <= row[time_column].time() <= time_range[1]):
    #             note_key = 'outside_expected_time_morning' if trip_type == 'morning' else 'outside_expected_time_afternoon'
    #             add_note(self.driver, note_key)
                
    def validate_time_ranges(self, time_column, time_range, trip_type):
        """Validate that the timestamps are within the expected time range."""
        min_time, max_time = None, None
        
        if not self.trip_data[time_column].isnull().all():
        # Get the minimum and maximum times from the column
            min_time = self.trip_data[time_column].min().time()
            max_time = self.trip_data[time_column].max().time()
        
            # Check if the min or max time is outside the expected range
            if min_time < time_range[0] or max_time > time_range[1]:
                note_key = 'outside_expected_time_morning' if trip_type == 'morning' else 'outside_expected_time_afternoon'
                add_note(self.driver, note_key)
                
    def validate_interactions(self, trip_type):
        """Validate the number of student interactions for each trip using 'Is Present In Bus'."""
        # Check if all values in the 'Is Present In Bus' column are False
        if not self.trip_data['Is Present In Bus'].any():
            # If all values are False, it means no students were present on the bus
            note_key = 'no_interactions_morning' if trip_type == 'morning' else 'no_interactions_afternoon'
            add_note(self.driver, note_key)
            return  # Exit early if this condition is met

        # Count the number of non-null 'In Date' values to determine interactions
        interacted_students = self.trip_data['In Date'].notna().sum()
        min_interactions = VEHICLE_MIN_STUDENTS.get(self.driver.vehicle_type, 0)
        
        # Check if the number of interactions is below the minimum threshold
        if interacted_students < min_interactions:
            add_note(self.driver, 'insufficient_interactions')
        
    # def validate_interactions(self):
    #     """Validate the number of student interactions for each trip."""
    #     # Check if all values in both 'In Date' and 'Out Date' are null
    #     if self.trip_data['In Date'].isna().all() and self.trip_data['Out Date'].isna().all():
    #         add_note(self.driver, 'no_interactions')
    #         return  # Exit early if this condition is met

    #     # Count the number of non-null 'In Date' values to determine interactions
    #     interacted_students = self.trip_data['In Date'].notna().sum()
    #     min_interactions = VEHICLE_MIN_STUDENTS.get(self.driver.vehicle_type, 0)
        
    #     # Check if the number of interactions is below the minimum threshold
    #     if interacted_students < min_interactions:
    #         add_note(self.driver, 'insufficient_interactions')


    # def validate_trip_data(self):
    #     """Check for specific trip errors (boarding/dropping mismatches)."""
    #     for _, row in self.trip_data.iterrows():
    #         if pd.notna(row['In Date']) and pd.isna(row['Out Date']):
    #             add_note(self.driver, 'missing_drop_off')
    #         elif pd.isna(row['In Date']) and pd.notna(row['Out Date']):
    #             add_note(self.driver, 'unexpected_drop_off')
    
    def validate_trip_data(self):
        """Check for specific trip errors (boarding/dropping mismatches)."""
        # Filter rows where 'Is Present In Bus' is True
        present_in_bus = self.trip_data['Is Present In Bus']

        # Check if any 'In Date' is missing where 'Is Present In Bus' is True
        if (self.trip_data.loc[present_in_bus, 'In Date'].isna()).any():
            add_note(self.driver, 'unexpected_drop_off')
        
        # Check if any 'Out Date' is missing where 'Is Present In Bus' is True
        if (self.trip_data.loc[present_in_bus, 'Out Date'].isna()).any():
            add_note(self.driver, 'missing_drop_off')

    def process_trip(self, trip_type):
        """Process the trip and apply all validations."""
        time_range = MORNING_TIME_RANGE if trip_type == 'morning' else AFTERNOON_TIME_RANGE
        self.driver.mark_trip_usage(trip_type)

        if trip_type == 'morning':
            self.validate_short_time_span('In Date', trip_type)
            self.validate_time_ranges('In Date', time_range, trip_type)
            self.validate_time_ranges('Out Date', time_range, trip_type)
        elif trip_type == 'afternoon':
            self.validate_short_time_span('Out Date', trip_type)
            self.validate_time_ranges('In Date', time_range, trip_type)
            self.validate_time_ranges('Out Date', time_range, trip_type)

        self.validate_trip_data()
        self.validate_interactions(trip_type)
        
    @staticmethod
    def classify_trip(trip_name):
        """Classify the trip as morning or afternoon."""
        if "الذهاب الى المدرسة" in trip_name:
            return "morning"
        elif "العودة من المدرسة" in trip_name:
            return "afternoon"
        return None
