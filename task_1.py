from queue import Queue
import time

queue = Queue()

def generate_request():
    req = "Request " + str(time.time())
    queue.put(req)


def process_request():
    if not queue.empty():
        req = queue.get()
        print(f"Serve request {req}")
    else:
        print('Queue is empty')

while True:
    generate_request()
    process_request()
