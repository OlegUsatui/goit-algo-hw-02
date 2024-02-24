from queue import Queue
import time

queue = Queue()

def generate_request(request_id):
    req = f"Request {request_id}"
    print(f"Generated {req}")
    queue.put(req)
    time.sleep(1)

def process_request():
    if not queue.empty():
        req = queue.get()
        print(f"Processed {req}")
        time.sleep(2)
    else:
        print('Queue is empty')

request_id = 1
while True:
    generate_request(request_id)
    process_request()
    request_id += 1

    user_input = input("Continue? (y/n): ")
    if user_input.lower() != 'y':
        print("Program terminated.")
        break
