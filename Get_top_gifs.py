import requests
import os

url = 'https://reddit.com/r/gifs/top.json'
params = {"t": "day"}
headers = {'User-Agent': 'serge'}

resp = requests.get(url, headers=headers, params=params)

resp_json = resp.json()
resp_data = resp_json["data"]
children = resp_data["children"]

total_len = len(children)

for index, child in enumerate(children, 1):
    print(f"Processing {index} / {total_len}")
    child_data = child["data"]
    filename = os.path.join(
        "gifs",
        f'{child_data["name"]}.mp4'
    )
    url = child_data["url"]
    if 'imgur' not in url:
        continue
    url = url.replace('.gifv', '.pm4')
    with open(filename, "wb") as fw:
        file_resp = requests.get(url, stream=True)
        for chunk in file_resp:
            fw.write(chunk)
    print("Saved {filename}")
