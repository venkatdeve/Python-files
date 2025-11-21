#requests used f  or api's
import requests
#used for date and time
import time
from datetime import datetime

# Configuration for base API URL
config = {"base_url": "https://reqres.in"}
print(requests.get(config["base_url"]).status_code)

# Utility function to log test results with timestamp
def log_result(test_name, status):
    print(f"{datetime.now()} | {test_name} | {status}")

# API function to fetch users (GET request)
def get_users():
    return requests.get(config["base_url"] + "/api/users?page=2")

# API function to create a user (POST request)
def create_user():
    data = {"name": "Satish", "job": "Lead Engineer"}
    return requests.post(config["base_url"] + "/api/users", json=data)

# Run both tests and log results
def run_tests():
    r = get_users()
    # print statement says status weather status is success or not
    print("GET Status Code:", r.status_code)
    if r.status_code == 200:
        log_result("test_get_users", "PASS")
    else:
        log_result("test_get_users", "FAIL")

    r = create_user()
    #create user is failed because it was pass the data to the api key
    #their may be some fault other side (API Side)
    print("POST Status Code:", r.status_code)
    if r.status_code == 201:
        log_result("test_create_user", "PASS")
    else:
        log_result("test_create_user", "FAIL")
# Entry point: measure execution time
if __name__ == "__main__":
    start = time.time()
    run_tests()
    end = time.time()
    print(f"Execution Finished in {round(end - start, 2)} seconds")