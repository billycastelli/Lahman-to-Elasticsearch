import sqlite3


class SQLiteWrapper:
    # Wrapper around SQLite to provide 'with' context management
    def __init__(self, location):
        self.location = location
        self.cursor = None
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.Connection(self.location)

        # Use row factory to later obtain data in dict format
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, traceback):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()
