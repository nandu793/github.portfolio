import re

def is_valid_email(email: str) -> bool:
    """
    Validates if the given string is a valid email address.
    Checks:
    - Must contain exactly one '@'
    - Local part and domain part must not be empty
    - Domain must contain at least one '.'
    - No spaces allowed
    - Basic allowed characters
    """
    if not isinstance(email, str):
        return False

    if ' ' in email:
        return False

    if email.count('@') != 1:
        return False

    local_part, domain_part = email.split('@')

    if not local_part or not domain_part:
        return False

    if '.' not in domain_part:
        return False

    # Basic regex for valid email pattern
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if not re.match(pattern, email):
        return False

    return True

# ✅ ✅ ✅ Add this part at the end of your file!
if __name__ == "__main__":
    email_to_check = input("Enter an email to validate: ")
    print(is_valid_email(email_to_check))
