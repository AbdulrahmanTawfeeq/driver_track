import openpyxl
import pandas as pd
from datetime import datetime
from translations import TRANSLATIONS

class ReportGenerator:
    def __init__(self, drivers, template_path, language='ar'):
        self.drivers = drivers
        self.template_path = template_path
        self.language = language  # Set the language for the translations

    def generate_report(self):
        report = [driver.get_summary() for driver in self.drivers.values()]
        return pd.DataFrame(report)

    def save_report_to_template(self, report_df, output_path):
        # Load the Excel template
        workbook = openpyxl.load_workbook(self.template_path)
        sheet = workbook.active  # Adjust if you have a specific sheet if needed

        # Update the date in cell B2
        sheet['B2'] = datetime.now().strftime('%Y-%m-%d')

        # Iterate over the rows in the report and fill the template
        for idx, row in enumerate(report_df.itertuples(index=False), start=6):
            sheet[f'B{idx}'] = row[0]  # Driver Name
            sheet[f'C{idx}'] = row[1]  # Branch
            sheet[f'D{idx}'] = row[2]  # Vehicle Type
            sheet[f'F{idx}'] = row[3]  # Notes
            
            # Determine the note type based on the note content using TRANSLATIONS
            note_value = row[3]  # This is the note in the report
            note_key = self.get_note_key(note_value)

            # Set column E based on the identified note key
            if note_key == 'correct_usage':
                sheet[f'E{idx}'] = "a" # it is check symbole when the font is webdings in the template
            elif note_key == 'no_app_usage':
                sheet[f'E{idx}'] = "r" # X sybmole
            else:
                sheet[f'E{idx}'] = "s" # "?" symbole

        # Save the updated workbook to the specified output path
        workbook.save(output_path)

    def get_note_key(self, note_value):
        """Return the note key based on the note value and the selected language."""
        for key, translation in TRANSLATIONS[self.language].items():
            if note_value == translation:
                return key
        return None
