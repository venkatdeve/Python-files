import json
import logging

# Configure logging to display INFO level and above messages with a simple format
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

# Inline JSON data as a multiline string
data = '''
[
    {"name": "Satish", "age": 25, "department": "Lead Engineer"},
    {"name": "Venkat", "department": "CSE"},
    {"age": 25, "department": "TECH"}
]
'''

try:
    # Parse the JSON string into a Python list of dictionaries
    employees = json.loads(data)
    logging.info("JSON data parsed successfully")

    # Iterate through each employee dictionary
    for emp in employees:
        # Use .get() with default "N/A" to handle missing fields
        name = emp.get("name", "N/A")
        age = emp.get("age", "N/A")
        dept = emp.get("department", "N/A")

        # Print employee details
        print(f"Name: {name}, Age: {age}, Department: {dept}")

except json.JSONDecodeError as e:
    # Log an error if JSON parsing fails
    logging.error(f"Failed to parse JSON: {e}")