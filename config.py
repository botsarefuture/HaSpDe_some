import json

class Config:
    def __init__(self, config_file='config.json'):
        with open(config_file, 'r') as file:
            config = json.load(file)
        
        # Flask settings
        self.FLASK_DEBUG = config.get('flask_debug', True)
        self.FLASK_PORT = config.get('flask_port', 5000)

        # MongoDB settings
        self.MONGO_URI = config.get('mongodb_uri', 'mongodb://localhost:27017/')
        self.MONGO_DBNAME = config.get('db_name', 'comment_moderation')

        # Instagram settings
        self.INSTAGRAM_ACCESS_TOKEN = config.get('instagram_access_token', '')
        self.INSTAGRAM_API_VERSION = config.get('instagram_api_version', 'v20.0')
        self.INSTAGRAM_VERIFY_TOKEN = config.get('instagram_verify_token', '')

        # Other settings
        self.IMPROVE = config.get('improve', True)
        self.HUMAN_REVIEW = config.get('human_review', False)
        self.CERTAINTY_NEEDED = config.get("certainty_needed", 80)
        self.MODE = config.get("mode", "full")

# Example usage:
# config = Config()
# print(config.FLASK_PORT)
