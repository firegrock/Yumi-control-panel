from __future__ import print_function
import argparse
import time
from RAPID import abb
from Python.triad_openvr import triad_openvr
import openvr
from pythonosc import osc_bundle_builder
from pythonosc import udp_client
from reprint import output
from colorama import Fore, Back, Style

print(Back.CYAN + Fore.WHITE + Style.BRIGHT +
"""                            \n      OpenVR OSC 1.0        \n                            \n""" + Style.RESET_ALL)

LeftHand = abb.Robot(ip='192.168.125.1', port_motion=5000)
RightHand = abb.Robot(ip='192.168.125.1', port_motion=5001)

moveAllowedL = False
moveAllowedR = True

firstLaunchL = True
firstLaunch = True

openHand = False

prevPose = [0, 0, 0, 0, 0, 0, 0]

# Initialize Tria's OpenVR wrapper and print discovered objects
v = triad_openvr.triad_openvr()
print(Style.DIM)
v.print_discovered_objects()
print(Style.RESET_ALL)

# Sort through all discovered devices and keep track by type
deviceCount = 0
devices = {
    'tracker': [],
    'hmd': [],
    'controller': [],
    'tracking reference': []
}

for deviceName, device in v.devices.items():
    device._id = deviceName.split("_").pop()
    devices[device.device_class.lower()].append(device)
    deviceCount += 1

def get_controller_ids(vrsys=None):
    if vrsys is None:
        vrsys = openvr.VRSystem()
    else:
        vrsys = vrsys
    left = None
    right = None
    for i in range(openvr.k_unMaxTrackedDeviceCount):
        device_class = vrsys.getTrackedDeviceClass(i)
        if device_class == openvr.TrackedDeviceClass_Controller:
            role = vrsys.getControllerRoleForTrackedDeviceIndex(i)
            if role == openvr.TrackedControllerRole_RightHand:
                right = i
            if role == openvr.TrackedControllerRole_LeftHand:
                left = i
    return left, right

if __name__ == "__main__":
    # Parse CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="ip of the OSC server")
    parser.add_argument("--port", type=int, default=7000, help="port the OSC server is listening on")
    parser.add_argument("--track", nargs="*", default=["hmd", "tracker", "controller"], help="devices to track (hmd, tracker, controller)")
    parser.add_argument("--freq", type=int, default=250, help="tracking frequency (in ms)")
    parser.add_argument("--mode", choices=['euler', 'quaternion'], default="quaternion", help="get pose data in euler angles or quaternions")
    args = parser.parse_args()

    # pose tracking interval
    interval = 1/250

    # initialize OSC client
    client = udp_client.SimpleUDPClient(args.ip, args.port)

    # print some stuff
    print(Fore.GREEN + "\rSending OSC tracking data on " + args.ip + ":" + str(args.port), end="\n\n")
    vrsystem = openvr.VRSystem()
    left_id, right_id = get_controller_ids(vrsystem)
    with output(output_type="list", initial_len=5, interval=0) as output_list:
        while(True):
            start = time.time()

            bundle = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)
            di = 0

            try:
                resultL, pControllerStateL = vrsystem.getControllerState(left_id)
                resultR, pControllerStateR = vrsystem.getControllerState(right_id)

                if bool(pControllerStateL.ulButtonPressed >> 2 & 1) is True:
                    moveAllowedL = False

                if bool(pControllerStateR.ulButtonPressed >> 2 & 1) is True:
                    moveAllowedR = False

                if pControllerStateL.rAxis[1].x == 1.0:
                    LeftHand.closeHand()

                if pControllerStateR.rAxis[1].x == 1.0:
                    RightHand.closeHand()
                # else:
                #     RightHand.openHand()

                for deviceType in args.track:
                   for device in devices[deviceType]:
                        if deviceType == 'controller' and device._id == '1':
                            poseEulerL = device.get_pose_euler()

                            if bool(pControllerStateL.ulButtonPressed >> 1 & 1) is True:
                                moveAllowedL = True

                                if firstLaunchL == True:
                                    zeroPoseL = [poseEulerL[0], poseEulerL[1], poseEulerL[2], poseEulerL[3],
												 poseEulerL[4], poseEulerL[5]]
                                    firstLaunchL = False

                            if firstLaunchL == False:
                            #bundle.add_content(msg.build())

                            ### report devicэe pose in the cons
                            #txt = Fore.CYAN + '{0: <13}'.format(deviceType + device._id) + Fore.WHITE + Style.BRIGHT

                            #output_list[di] = txt

                                curPoseL = [round(poseEulerL[0] - zeroPoseL[0], 4),
									   round(poseEulerL[1] - zeroPoseL[1], 4),
									   round(poseEulerL[2] - zeroPoseL[2], 4),
									   round(poseEulerL[3] - zeroPoseL[3], 4),
									   round(poseEulerL[4] - zeroPoseL[4], 4),
									   round(zeroPoseL[5] - poseEulerL[5], 4)]

                                controllerOffsetsL = [curPoseL[2], curPoseL[0], curPoseL[1], curPoseL[3], curPoseL[5], curPoseL[4]]

                                yumiTargetL = [controllerOffsetsL[0] * 1000,
										   controllerOffsetsL[1] * 1000,
										   controllerOffsetsL[2] * 1000,
										   controllerOffsetsL[3],
										   controllerOffsetsL[4],
										   controllerOffsetsL[5]]
                                if moveAllowedL is True:
                                    LeftHand.set_offsets(yumiTargetL)
                                else:
                                    pass

                        if deviceType == 'controller' and device._id == '2':

                            poseEuler = device.get_pose_euler()

                            if bool(pControllerStateR.ulButtonPressed >> 1 & 1) is True:
                               moveAllowedR = True
                               poseEuler = device.get_pose_euler()

                               if firstLaunch == True:
                                   zeroPose = [poseEuler[0], poseEuler[1], poseEuler[2], poseEuler[3],
												 poseEuler[4], poseEuler[5]]
                                   firstLaunch = False

                            if firstLaunch == False:
                            #msg = osc_message_builder.OscMessageBuilder(address="/" + deviceType + "/" + device._id)
                            #msg.add_arg(device.get_pose_quaternion())
                            #bundle.add_content(msg.build())

                            #txt = Fore.CYAN + '{0: <13}'.format(deviceType + device._id) + Fore.WHITE + Style.BRIGHT

                            #output_list[di] = txt

                                curPose = [round(poseEuler[0] - zeroPose[0], 4),
                                       round(poseEuler[1] - zeroPose[1], 4),
                                       round(poseEuler[2] - zeroPose[2], 4),
                                       round(poseEuler[3] - zeroPose[3], 4),
                                       round(zeroPose[4] - poseEuler[4], 4),
                                       round(poseEuler[5] - zeroPose[5], 4)]

                                controllerOffsets = [curPose[2], curPose[0], curPose[1], curPose[3], curPose[5], curPose[4]]

                            #print("right controllerOffsets: ", controllerOffsetsL)
                            #print("right POSE euler: ", poseEulerL)

                                yumiTarget = [controllerOffsets[0]*1000, controllerOffsets[1]*1000, controllerOffsets[2]*1000, controllerOffsets[3], controllerOffsets[4], controllerOffsets[5]]

                                if moveAllowedR is True:
                                    RightHand.set_offsets(yumiTarget)
                                else:
                                    pass
                        di += 1
                   # Send the bundle
                   client.send(bundle.build())
            except Exception as e:
                print(e)

            # wait for next tick
            sleep_time = interval-(time.time()-start)
            if sleep_time>0:
                time.sleep(sleep_time)