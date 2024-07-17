import random
import asyncio
import meraki.aio
import datetime


#It is strongly recommended to not hard code this API key into the script but instead use an environmental variable to store this and import that into the script. This page may be useful to help write that-
#https://community.meraki.com/t5/Developers-APIs/Getting-Started-with-Meraki-API-using-Python-Part-4-Intro-to/m-p/169224
API_KEY = ''

# Template or network ID to configure the users under
#MX and MR template ID = L_1155173304420542230
#MR only template ID = L_1155173304420542233
#If other templates are created in the future you can find the temaplte or network ID running a get call to the appropriate API request. https://api.gov-meraki.com/api/v1/organizations/:organizationId/configTemplates or https://api.gov-meraki.com/api/v1/organizations/1155173304420532455/networks
TEMPLATE_NETWORK_ID = ''

number_of_accounts_to_create = 3
email_at = '@blmguest.com'

def generate_random_email(length=8):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(characters) for i in range(length)) + email_at

def generate_random_password(length=14):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    return ''.join(random.choice(characters) for i in range(length))

def print_colored(message, color):
    colors = {
        'green': '\033[92m',  # Green text
        'red': '\033[91m',    # Red text
        'purple': '\033[95m', # Purple text
    }
    reset_code = '\033[0m'  # Reset to default text color
    print(f"{colors.get(color, '')}{message}{reset_code}")

# Asynchronous function to create accounts
async def main():
    async with meraki.aio.AsyncDashboardAPI(api_key=API_KEY,base_url='https://api.gov-meraki.com/api/v1') as dashboard:
        for _ in range(number_of_accounts_to_create):
            email = generate_random_email()
            name = email.split('@')[0]
            password = generate_random_password()  # Use the new password generator
            expires_at = (datetime.datetime.now() + datetime.timedelta(days=3)).isoformat()
            
            user_data = {
                "email": email,
                "name": name,
                "password": password,
                "accountType": "Guest",
                "emailPasswordToUser": False,
                "isAdmin": False,
                "authorizations": [
                    {
                        "ssidNumber": 1,
                        "expiresAt": expires_at
                    }
                ]
            }
            
            try:
                response = await dashboard.networks.createNetworkMerakiAuthUser(
                    TEMPLATE_NETWORK_ID,
                    **user_data
                )
                # Print the email and password in green and purple respectively
                print_colored(f"Successfully created user: {email}", 'green')
                print_colored(f"Username: {email}", 'purple')
                print_colored(f"Password: {password}", 'purple')

            except meraki.aio.AsyncAPIError as e:
                print_colored(f"API Error for user: {email} - {e}", 'red')

if __name__ == '__main__':
    asyncio.run(main())
