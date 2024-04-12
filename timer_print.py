import time
from datetime import datetime

while True:
    time.sleep(1.0)
    timestamp = datetime.now()
    print(timestamp, flush=True)
