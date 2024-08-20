import os
import pandas as pd

class DataManager:
    FILE_PATH = os.path.join('data', 'students.csv')

    @staticmethod
    def save_data(students):
        """Save student data to a CSV file."""
        df = pd.DataFrame(students)
        df.to_csv(DataManager.FILE_PATH, index=False)

    @staticmethod
    def load_data():
        """Load student data from a CSV file."""
        if os.path.exists(DataManager.FILE_PATH):
            return pd.read_csv(DataManager.FILE_PATH).to_dict(orient='records')
        return []
