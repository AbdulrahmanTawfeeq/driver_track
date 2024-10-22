from pathlib import Path
from translations import TRANSLATIONS

def add_note(driver, note_key):
    """Adds a note to the driver based on the language and note key."""
    note = TRANSLATIONS[driver.language].get(note_key, "")
    if note:
        driver.notes.add(note)  # Add notes to the set for uniqueness

def get_downloads_folder():
    """Return the path to the Downloads folder of the current user."""
    home = Path.home()
    downloads_folder = home / "Downloads"
    return downloads_folder
