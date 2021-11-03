# Pacemaker_Development

In this project, we're developing a pacemaker using an NXP FRDM-K64F microcontroller board and a simulated heart. Using a predefined physical parameters list, my team and I are implementing state flows for various pacemaker modes, in addition to, applying hardware hiding principles using Simulink subsystems. Also, we are in the process of developing an intuitive graphical user interface (GUI) using the Python library PySimpleGui.

Progress:
- User Interface:
	- Developed a complete login and signup system
	- Implemented safety mechanisms such as password masking and a maximum of 10 users
	- Configured pacing modes AOO, VOO, AAI, VVI
	- Completed physical parameters checking based on aforementioned list
	- Designed an indicator for serial communication

- Simulink state flows:
	- Completed the simulink state flow for pacing modes AOO, VOO, VVI, AAI

Future Updates:
- Implement state flows for pacing modes AOOR, VOOR, AAIR, VVIR and DOOR
- Complete serial communication protocols using Python Serial library
- Password strength verification
	- Currently users are allowed to enter any password as long as it is not blank or contains a space. This is can lead to weak and insecure user passwords. We 		plan to add a measure to ensure that the passwords users’ chose have a minimum length of 8 characters, include one number, and a special character.
- Multi-Factor Authentication Login
	- In addition to increasing password strength verification, we plan to add a 2FA to boost the security of the product.
- User customization settings
	- As of right now there is no option to change a users’ username or password, we plan on developing customization settings to add these options.
- Should have a check to make sure no invalid characters are allowed when registering new user
	- Currently, users can use any non-blank value as a username. We plan to add checks to ensure usernames do not have any invalid characters like (@!#$%*&^) 		and are a minimum of three characters long.
- Admin user role
	- We plan to implement an admin user role that will give that user the ability to manage and delete users from the app.
- Generate a log of actions for each pacemaker
	- Before the next release, a log of pacemaker actions feature will be added. This text file will document all parameter changes, the user that made the 	changes, and the times that they occurred at. This will create a central place for doctors to view all previous pacemaker changes.

- Caps Lock Indicator
	- When inputting a password while logging in/signing up a notification can be displayed to a user that caps lock is enabled.
