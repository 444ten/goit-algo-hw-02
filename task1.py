from queue import Queue
import time
import random

request_queue = Queue()
request_id = 1  # Counter for unique request IDs

def generate_request():
    global request_id
    request = f"Request #{request_id}"
    request_queue.put(request)
    print(f"[+] Created {request}")
    request_id += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[✓] Processing {request}")
    else:
        print("[!] The queue is empty — no requests to process.")

def simulate_service(run_seconds=20, gen_interval=1.0, proc_interval=1.0):
    """
    Run the service center simulation for a given amount of time.

    Parameters:
    - run_seconds: total simulation duration (seconds)
    - gen_interval: delay between generating requests
    - proc_interval: delay between processing requests
    """
    end_time = time.time() + run_seconds

    try:
        while time.time() < end_time:
            # Randomly generate 0 to 2 new requests to simulate real flow
            for _ in range(random.randint(0, 2)):
                generate_request()
                time.sleep(0.1)  # short pause between generated requests

            # Process a single request
            process_request()

            # Wait before next cycle
            time.sleep(max(gen_interval, proc_interval))

    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")

if __name__ == "__main__":
    print("Service center simulation started (press Ctrl+C to stop).")
    simulate_service(run_seconds=10, gen_interval=1.0, proc_interval=1.0)
    print("Simulation finished.")
