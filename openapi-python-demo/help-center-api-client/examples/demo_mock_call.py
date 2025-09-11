# examples/demo_mock_call.py
import base64
from help_center_api_client import Client
from help_center_api_client.api.articles import list_articles

BASE_URL = "http://127.0.0.1:4010"

creds = base64.b64encode(b"dummy:dummy").decode("ascii")
headers = {"Authorization": f"Basic {creds}"}

client = Client(base_url=BASE_URL, headers=headers)

resp_detailed = list_articles.sync_detailed(client=client, locale="en-us")

print("STATUS:", resp_detailed.status_code)
print("PARSED TYPE:", type(resp_detailed.parsed))
print("PARSED VALUE:", resp_detailed.parsed)
