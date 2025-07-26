import requests

url = "http://127.0.0.1:5000/predict"
sample_text = "NASA has confirmed that aliens have arrived on Earth."

response = requests.post(url, json={"text": sample_text})
print("Response:", response.json())
