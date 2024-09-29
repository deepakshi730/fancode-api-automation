import requests
import pytest

# Base Url
BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users_by_city(city):
    """
        Fetch users detail living in a city
        Parameters: 
            city : (string) // city name
        Returns:
            list : list of users living in the city
    """
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()
    users = response.json()
    return [user for user in users if user['address']['city'] == city]

def get_todos_by_user(user_id):
    """
        Returns todos tasks of a user
        Parameters: 
            user_id : (string) // user id
        Returns:
            obj : todos tasks of a user
    """
    response = requests.get(f"{BASE_URL}/todos", params={"userId": user_id})
    response.raise_for_status()
    return response.json()

def test_fancode_users_todos_completion():
    """ 
        Test all the users of City `FanCode` should have more than half of their todos task completed.
    """
    city = "FanCode"
    users = get_users_by_city(city)
    
    for user in users:
        todos = get_todos_by_user(user['id'])
        completed_todos = [todo for todo in todos if todo['completed']]
        assert len(completed_todos) > len(todos) / 2, f"User {user['name']} hasn't completed more than half of their tasks."