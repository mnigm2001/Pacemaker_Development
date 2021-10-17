# Pacemaker_Development

This project project, we're developing a pacemaker using an NXP FRDM-K64F microcontroller board and a simulated heart. Using a predefined physical parameters list, my team and I are implementing state flows for various pacemaker modes, in addition to, applying hardware hiding principles using Simulink subsystems. Also, we are in the process of developing an intuitive graphical user interface (GUI) using the Python library PySimpleGui.

Progress:
- User Interface:
	- Developed a complete login and signup system
	- Implemented safety mechanisms such as password masking and a maximum of 10 users
	- Configured pacing modes AOO, VOO, AAI, VVI
	- Completed physical parameters checking based on aforementioned list
	- Designed an indicator for serial communication

- Simulink state flows:
	- Completed the simulink state flow for pacing mode AOO

Future Updates:
- Implement state flows for pacing modes AOOR, VOOR, AAIR, VVIR and DOOR
- Complete serial communication protocols using Python Serial library