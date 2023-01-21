from webbrowser import get
import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    users = [user for user in data['login']]
    return len(users)
data = get_data.get_data('randomuser_data.json')
get_count_users(data)