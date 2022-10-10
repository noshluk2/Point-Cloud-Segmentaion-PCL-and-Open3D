
import numpy as np
import open3d as o3d


## Loading pcd file
pcd = o3d.io.read_point_cloud("scan.pcd")
print(pcd)
print(np.asarray(pcd.points))

# simple plotting
# o3d.visualization.draw_geometries([pcd],zoom=0.3412,front=[0.4257, -0.2125, -0.8795],lookat=[2.6172, 2.0475, 1.532],up=[-0.0694, -0.9768, 0.2024])


## Voxel Downsampling
downpcd = pcd.voxel_down_sample(voxel_size=0.1)
# o3d.visualization.draw_geometries([downpcd],zoom=0.3412,front=[0.4257, -0.2125, -0.8795],lookat=[2.6172, 2.0475, 1.532],up=[-0.0694, -0.9768, 0.2024])


## Normal Estimation
downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([downpcd],zoom=0.3412,front=[0.4257, -0.2125, -0.8795],lookat=[2.6172, 2.0475, 1.532],up=[-0.0694, -0.9768, 0.2024])

