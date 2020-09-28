This project based on abb.py and triad_openvr.

GUI is developed with using of pyqt5.

ABB-open protocol:
'01 ' - Executes a move immediately from the current pose, to 'pose', with units of millimeters.
'02 ' - Executes a move immediately, from current joint angles, to 'joints', in degrees. 
'03 #' - Returns the current pose of the robot, in millimeters 
'04 #' - returns the current angles of the robot's joints, in degrees
'05 #' - get external axis
'06 ' - set tool
'07 ' - set workobject
'08 ' - set speed
'09 ' - set motion zone of the robot
'30 ' - add a single pose to remote buffer
'31 #' - clear remote buffer of positions
'32 #' - Returns the length (number of poses stored) of the remote buffer 
'33 #' - start immediate moving to every pose in the remote buffer
'34 ' - set external axis
'35 pose_onarc' - set pose_onarc as the begging of the circle  
'36 pose_end' - set the pose_end as the end of the circle  
'97 #' - set a physical DIO line on the robot. For this to work you're going to need to edit the RAPID function and fill in the DIO you want this to switch.         
'98 #' - get robot info
'99 #' - close socket

firegrock's extensions:
'101 ' - set offsets
'102 ' - set cartesian in Eulers angles
'1098 #' - close hand
'1099 #' - Open hand
'201 ' - set leadthough mode is on/off
'301 'int' - set current case