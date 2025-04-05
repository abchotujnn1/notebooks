import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.
# the format for that file is (without the comment)
#API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_google_api_key():
    load_env()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    return google_api_key