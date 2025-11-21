# requests used for API calls
import requests
# used for timing and timestamps
import time
from datetime import datetime

# Configuration dictionary
config = {"base_url": "https://reqres.in"}

# Store test results
results = []

# Utility function to record and print test results
def record_result(test_name, status):
    results.append((test_name, status))  # Append as tuple
    print(f"{datetime.now()} | {test_name} | {status}")

# Reusable API method: GET users
def get_users():
    return requests.get(config["base_url"] + "/api/users?page=2")

# Reusable API method: POST create user
def create_user():
    data = {"name": "Satish", "job": "Lead Engineer"}
    return requests.post(config["base_url"] + "/api/users", json=data)

# Run tests and log results
def run_tests():
    r = get_users()
    #r.status_code saves 200 or 400 and prints status code
    print("GET Status Code:", r.status_code)
    if r.status_code == 200:
        record_result("test_get_users", "PASS")
    else:
        record_result("test_get_users", "FAIL")

    r = create_user()
    # r.status_code saves 400 because it was not posting the details or content , so it was returning 400
    print("POST Status Code:", r.status_code)
    if r.status_code == 201:
        record_result("test_create_user", "PASS")
    else:
        record_result("test_create_user", "FAIL")

# Entry point: measure execution time and print summary
if __name__ == "__main__":
    start = time.time()
    #start time before calling run_tests() function
    run_tests()
    end = time.time()
    # end time after completing run_tests() function
    print(f"\nExecution Finished in {round(end - start, 2)} seconds")
    print("\nTest Summary ")
    for test_name, status in results:
        print(f"{test_name}: {status}")