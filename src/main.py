from data_loader import DataLoader
from driver import Driver
from trip import Trip
from report_generator import ReportGenerator
from utils import get_downloads_folder, add_note

def main():
    # Set the language for the application (e.g., 'ar' for Arabic, 'kr' for Kurdish Sorani)
    language = 'ar'

    # Get the Downloads folder dynamically
    downloads_folder = get_downloads_folder()
    trip_file_path = downloads_folder / 'export.xlsx'
    template_path = 'data/template.xlsx'  # Template file path
    output_file_path = downloads_folder / 'driver_track.xlsx'
    driver_file_path = 'data/drivers_info.xlsx'

    # Load data
    data_loader = DataLoader(trip_file_path, driver_file_path)
    trip_data = data_loader.load_trip_data()
    driver_data = data_loader.load_driver_data()

    # Initialize drivers with the selected language
    drivers = {
        row['Driver Name']: Driver(row['Driver Name'], row['Branch'], row['Vehicle Type'], language)
        for _, row in driver_data.iterrows()
    }

    # Identify drivers who have not used the app
    drivers_in_data = set(trip_data['Driver Name'].unique())
    for driver_name in set(drivers.keys()) - drivers_in_data:
        add_note(drivers[driver_name], 'no_app_usage')

    # Process each driver's trip data
    for driver_name, driver_trip_data in trip_data.groupby('Driver Name'):
        driver = drivers.get(driver_name)
        if not driver:
            continue
        
        for trip_name, trip_data in driver_trip_data.groupby('Trip Name'):
            trip_type = Trip.classify_trip(trip_name)
            if not trip_type:
                continue

            trip = Trip(driver, trip_data)
            trip.process_trip(trip_type)

    # Finalize notes for drivers
    for driver in drivers.values():
        driver.evaluate_usage()

    # Generate the report
    report_generator = ReportGenerator(drivers, template_path)
    report_df = report_generator.generate_report()

    # Save the report to the template
    report_generator.save_report_to_template(report_df, output_file_path)

if __name__ == '__main__':
    main()