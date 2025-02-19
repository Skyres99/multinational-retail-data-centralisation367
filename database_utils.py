import yaml
from sqlalchemy import create_engine

class DatabaseConnector():
    def read_db_creds(self):

        with open('db_creds.yaml', 'r') as y:
            creds_yaml = yaml.safeload(y)
        return creds_yaml

    def init_db_engine(self):
        creds_yaml = self.read_db_creds()
        
        creds = (f"postgresql://{creds_yaml['RDS_DATABASE']}://{creds_yaml['RDS_USER']}:{creds_yaml['RDS_PASSWORD']}:{creds_yaml['RDS_HOST']}:{creds_yaml['RDS_PORT']}")
        read_engine = create_engine(creds)
        return read_engine