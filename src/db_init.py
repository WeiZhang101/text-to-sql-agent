# db_setup.py

import os
import pandas as pd
from sqlalchemy import create_engine


def initialize_database(database_file_path):
    file_urls = [
        "./data/GITS_Delivery_Hub_resource_management-Resource_management.csv",
    ]
    # Create an engine to connect to the SQLite database
    engine = create_engine(f"sqlite:///{database_file_path}")

    # Ensure the database directory exists
    os.makedirs(os.path.dirname(database_file_path), exist_ok=True)

    # Iterate through each file and write to the database
    for file_url in file_urls:
        # Read the CSV file and fill missing values
        df = pd.read_csv(file_url).fillna(value=0)

        # Generate table name from filename (remove path and extension)
        table_name = os.path.splitext(os.path.basename(file_url))[0]

        # Write DataFrame to database
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)

    print("Database initialized successfully!")


database_file_path = "./db/test_1.db"
initialize_database(database_file_path)
