cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(pcd_write)

find_package(PCL 1.2 REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable (pcl_learning pcl_src.cpp)
target_link_libraries (pcl_learning ${PCL_LIBRARIES})
add_executable (clustering clustering.cpp)
target_link_libraries (clustering ${PCL_LIBRARIES})
add_executable (plane_segment plane_segment.cpp)
target_link_libraries (plane_segment ${PCL_LIBRARIES})