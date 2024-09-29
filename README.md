## API Automation Framework

This project tests that all users from the city `FanCode` have more than half of their todos completed using a Python automation framework with `pytest` and `requests`.

## Scenario

- **Given**: User has todo tasks
- **And**: User belongs to the city FanCode
- **Then**: User's completed task percentage should be greater than 50%

FanCode city can be identified by latitude between -40 to 5 and longitude between 5 to 100 in the users API.

## Prerequisites

 - Python 3 or higher
 - Pytest
 - Request
 - Git

## Setup

1. Clone the repository.
   ```
   git clone https://github.com/deepakshi730/fancode-api-automation.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Running the Tests
To execute the tests, use the following command:

`pytest`

## Project Structure

```
 └── fancode-api-automation
       ├── src
       |    └── fancode
       |        └── users_todos_task_test.py
       ├── pytest.ini
       ├── README.md
       ├── requirements.txt
```

## Files

**users_todos_task_test.py** Contains test
**pytest.ini** Contains initial point to run tests
**requirements.txt** Contains requirements

## Test Execution

The test verifies that all users from FanCode city have completed more than 50% of their todos

## License

This project is licensed under the MIT License.

This README.md file provides comprehensive instructions for setting up and running the tests, including a description of the scenario, project structure, dependencies, and how to execute tests.


  
