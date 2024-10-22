class Driver:
    def __init__(self, name, branch, vehicle_type, language='ar'):
        self.name = name
        self.branch = branch
        self.vehicle_type = vehicle_type
        self.notes = set()  # Use a set to keep notes unique
        self.morning_used = False
        self.afternoon_used = False
        self.language = language

    def mark_trip_usage(self, trip_type):
        if trip_type == 'morning':
            self.morning_used = True
        elif trip_type == 'afternoon':
            self.afternoon_used = True

    def evaluate_usage(self):
        """Evaluates overall usage and adds appropriate notes."""
        from utils import add_note  # Import the utility function where needed
        if self.morning_used and self.afternoon_used and not self.notes:
            add_note(self, 'correct_usage')
        elif self.morning_used and not self.afternoon_used:
            add_note(self, 'morning_only')
        elif not self.morning_used and self.afternoon_used:
            add_note(self, 'afternoon_only')

    def get_summary(self):
        return {
            'Driver Name': self.name,
            'Branch': self.branch,
            'Vehicle Type': self.vehicle_type,
            'Notes': '; '.join(sorted(self.notes))  # Convert the set to a sorted list for consistency
        }
