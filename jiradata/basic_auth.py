import requests
from requests.auth import HTTPBasicAuth
import json

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


auth = HTTPBasicAuth(os.getenv('email'), os.getenv('auth_token'))