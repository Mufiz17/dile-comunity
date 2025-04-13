import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def fetch_drone_data():
    try:
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
        session.mount('https://', HTTPAdapter(max_retries=retries))

        response = session.get(
            "https://k31kdl3eukazsfrf.public.blob.vercel-storage.com/data-CCJDY2MzsjFXXOX1DK62vw1o1eOPhn.json",
            timeout=5
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed with status: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching drone data: {e}")
        return []
