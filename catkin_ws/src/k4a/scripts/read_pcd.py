#!/usr/bin/env python3

import numpy as np
import open3d as o3d
import os.path as osp


if __name__ == '__main__':
    xyz_data = np.loadtxt(
        osp.join(osp.dirname(__file__), 'data.txt'), 
        delimiter=' ')

    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(xyz_data)

    visualizer = o3d.visualization.Visualizer()
    visualizer.create_window(window_name="point cloud")
    visualizer.add_geometry(point_cloud)
    visualizer.run()
