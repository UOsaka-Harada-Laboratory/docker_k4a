#!/usr/bin/env python3

import k4a
import numpy as np
import open3d as o3d
import os.path as osp


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

    # get a new capture.
    capture = device.get_capture(-1)

    # get Point Cloud
    xyz_image = transformation.depth_image_to_point_cloud(capture.depth, k4a.ECalibrationType.DEPTH)

    # save Point Cloud To Ascii Format File. Interleave the [X, Y, Z] channels into [x0, y0, z0, x1, y1, z1, ...]
    height, width, channels = xyz_image.data.shape
    xyz_data = xyz_image.data.reshape(height * width, channels)
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(xyz_data)

    visualizer = o3d.visualization.Visualizer()
    visualizer.create_window(window_name="point cloud")
    visualizer.add_geometry(point_cloud)
    visualizer.run()

    np.savetxt(osp.join(osp.dirname(__file__), 'data.txt'), 
               xyz_data,
               delimiter=' ',
               fmt='%u') # save ascii format (x y z\n x y z\n x y z\n ...)

    # stop Cameras
    device.stop_cameras()
