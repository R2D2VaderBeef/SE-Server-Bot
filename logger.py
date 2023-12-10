import select
from systemd import journal
from bot import log_line

print("one was run")

def attach(service):
    print("attaching now boss")
    j = journal.Reader()
    j.log_level(journal.LOG_INFO)

    j.add_match(_SYSTEMD_UNIT=service)
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
                log_line(str(entry['__REALTIME_TIMESTAMP'] )+ ' ' + entry['MESSAGE'])