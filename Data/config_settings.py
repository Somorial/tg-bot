import configparser

class Config:
    def __init__(self, file_name):
        self.config = configparser.ConfigParser()
        self.config.read(file_name)
    
    def get_token(self):
        return self.config.get('settings', 'token')
    
    def get_accountent(self):
        return self.config.get('settings', 'accountant')
    

config = Config(r'config.ini')
