import time
from datetime import datetime

with open("timer.pipe", "a") as pipe:
    while True:
        time.sleep(1.0)
        timestamp = datetime.now()
        print(timestamp, flush=False)
        pipe.write(timestamp.__str__() + "\n")
        pipe.flush()
