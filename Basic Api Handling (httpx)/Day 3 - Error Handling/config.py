import os 
import httpx 
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('Token')


Base_url = 'https://gorest.co.in/public/v2'

Headers = {
    "Authorization": f"Bearer {api}",
    "Accept": "application/json",
}


Timeout = httpx.Timeout(
    connect=5, read=15, write=10, pool=5
)


