from dotenv import load_dotenv
import os

load_dotenv()

FILE_PATH = os.getenv('FILE_PATH')
SHEET = os.getenv('SHEET')
COLUMN = os.getenv('COLUMN')
ROW = int(os.getenv('ROW'))
