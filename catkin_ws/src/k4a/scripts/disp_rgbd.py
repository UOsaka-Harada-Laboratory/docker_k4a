#!/usr/bin/env python3

import k4a
import cv2
import numpy as np


if __name__ == '__main__':
    # open Device
    device = k4a.Device.open()

    # start Cameras
    device_config = k4a.DEVICE_CONFIG_BGRA32_1080P_NFOV_UNBINNED_FPS15
    device.start_cameras(device_config)

    # get Calibration
    calibration = device.get_calibration(
        depth_mode=device_config.depth_mode,
        color_resolution=device_config.color_resolution)

    # create Transformation
    transformation = k4a.Transformation(calibration)

    # display Images
    while True:
        # Get a new capture.
        capture = device.get_capture(-1)
        if capture is None:
            break

        # get color and depth images
        color_image = capture.color
        color_image = color_image.data

        depth_image = capture.depth
        depth_image = depth_image.data

        # show depth image using opencv
        depth_image = depth_image * (-255.0 / 5000.0) + 255.0
        depth_image = depth_image.astype(np.uint8)
        cv2.imshow("color image", color_image)
        cv2.imshow("depth image", depth_image)
        cv2.waitKey(1)

    # Get a new capture.
    capture = device.get_capture(-1)
