from sqlalchemy import inspect
import pandas as pd

class DataExtractor():
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def list_db_tables(self):
        engine = self.db_conn.init_db_engine()
        inspector = inspect(engine)
        rds_tables = inspector.get_table_names()
        return rds_tables
    
    def read_rds_table(self, table_name):
        engine = self.db_conn.init_db_engine
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, engine)

        return df
