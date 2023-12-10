import os
import select
import asyncio
from systemd import journal

def attach(log_function):
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
        
        print("the condition is append!")

        for entry in j:
            if entry['MESSAGE'] != "":
                print(str(entry['__REALTIME_TIMESTAMP'] )+ ' ' + entry['MESSAGE'])
                asyncio.create_task(log_function(str(entry['__REALTIME_TIMESTAMP'] )+ ' ' + entry['MESSAGE']))