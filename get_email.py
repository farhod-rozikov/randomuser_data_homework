import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    emails = [email['email'] for email in data['results']]
    return emails
data = get_data.get_data('randomuser_data.json')
print(get_email(data))