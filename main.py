import os
import requests
from dotenv import load_dotenv
load_dotenv()

import select
from systemd import journal

url = os.getenv('WEBHOOK')

j = journal.Reader()
j.log_level(journal.LOG_INFO)

j.add_match(_SYSTEMD_UNIT=os.getenv('SERVICE'))
j.seek_tail()
j.get_previous()

p = select.poll()
p.register(j, j.get_events())

while p.poll():
    if j.process() != journal.APPEND:
        continue
    for entry in j:
        if entry['MESSAGE'] != "":
            print(entry['MESSAGE'])
            requests.post(url=url, json={"username": "Vader's Test Server", "content": entry['MESSAGE']})