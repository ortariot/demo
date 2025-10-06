from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ.get("DB_NAME"))
print(os.environ.get("DB_PORT"))