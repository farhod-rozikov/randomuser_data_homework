from unicodedata import name
import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    i = 0
    users_data = [{"first_name": u_d['name']['first'], "last_name": u_d['name']['last'], "phone_number": u_d['phone']}  for u_d in data['results']]
    return users_data
data = get_data.get_data('randomuser_data.json')
print(get_users_data(data))