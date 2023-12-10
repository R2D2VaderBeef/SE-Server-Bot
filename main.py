import os
from dotenv import load_dotenv
load_dotenv()

import select
from systemd import journal

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
            #str(entry['__REALTIME_TIMESTAMP'] )+ ' ' +
            print(entry['MESSAGE'])