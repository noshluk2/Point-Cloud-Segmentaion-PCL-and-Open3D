## Point Cloud Segmentation
---
This directory contains source codes for processing point Clouds using
- python with library open3d
- CPP with library PCL



## Obtaining the Point Cloud
---
We obtain point cloud in a ".pcd" formate and it's source is ROS simulation
- Running the drone simulation
    ```
    roslaunch uav_sim 6_Point_cloud_Segmentation.launch
    ```
- Saving the current view infront of Drone
    ```
    rosrun pcl_ros pointcloud_to_pcd input:=/asus_depth_camera/depth/points
    ```

## Processing Point Cloud and Visualizing
For processing we have two option
1. CPP Executable creation
    - Inside of build folder
        ```
        cmake ..
        make
        ./<name of executable>
        ```
    - Visualizing
        ```
        pcl_viewer -multiview 2 table_scene_lms400_downsampled.pcd  cloud_cluster0.pcd cloud_cluster1.pcd cloud_cluster2.pcd cloud_cluster3.pcd cloud_cluster4.pcd
        ```
2. Python
    ```
    python3 1_visualize_pc.py
    ```