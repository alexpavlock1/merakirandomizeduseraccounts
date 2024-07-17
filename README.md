Meraki Guest Auth User Create Accounts

Prerequisites
Python version 3
Dashboard admin with write permissions
API key created for your admin account
Install the Meraki python SDK – Terminal command: pip3 install meraki

Description:

This script is designed to create guest user accounts in mass for SSID’s in Meraki dashboard. For SSID’s where users are prompted for username and password and authenticated against the Meraki Cloud this script can create those accounts and assign randomly generated values for usernames and passwords. The characteristics of the usernames and the passwords can be customized within the script. 

A use case for running this script is: A company has a guest SSID in use. The company is running a conference with 200 guests coming in. For compliance purposes the guest SSID requires a username and password to join the network. This company does not have typical radius servers in the environment, or they just simply want the convenience of using Meraki Dashboard to configure user accounts. Once an account is created, the admin can then communicate the email/username and password to the guest to login with. Once an account is successfully created the script will print to your terminal the username and password that was automatically created.

Customizing usernames and password requirements:
-Line 20 and line 24 (length=X): This will set the how many characters to put in the username and password.
-Line 21 and 22 are the characters that will be choosen from to randomly generate username and password.
-Line 17 you specify the number of accounts the script will create.
-Line 18 you can specify the @ portion of the email address that is created

Line 55 is a required line that will need to match you specific network. The accounts generated are approved for specific SSID’s. In dashboard if you navigate to Wireless>SSID’s page, the first SSID listed would equal 0, the second SSID would be 1 in the script, the third SSID would be 2, so on and so forth.

The script is also written to use asyncio which will avoid any rate limit errors and other such errors. Use govcreaterandomaccounts.py when working with government accounts

Instructions:

1.	Open script and edit your API key in line 9. Its recommended to pull in your API key from and environmental variable and not hard code the API key to the script for security purposes.
2.	Edit line 15 and input the network ID for the network we would like to configure the users for. Template ID’s are supported.
3.	Edit line 17 and specify the number of accounts you would like the script to create
4.	Edit line 18 and specify the email domain.
5.	Edit line 20, 24, and 44 to specify how many characters the username and password are along with how many days the account will be authorized for. To authorize indefinitely use the word ‘never’ in line 56 and comment out line 44
6.	Save the script and execute
![image](https://wwwin-github.cisco.com/storage/user/52239/files/68a259f3-d9b7-434a-8366-17466233cecd)

