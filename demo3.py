import os
import glob
import natsort
import numpy as np
import matplotlib as plt
from util.camera_pose_visualizer import CameraPoseVisualizer
from util.camera_parameter_loader import CameraParameterLoader

DATASET = "poses_tiger"

def plot_framewise():
    loader = CameraParameterLoader()
    visualizer = CameraPoseVisualizer([-5, 5], [-5, 5], [-5, 5])

    flist = natsort.natsorted(os.listdir(DATASET))

    for idx_frame, pose_file in enumerate(flist):
        if idx_frame % 10 == 0:
            pose = np.loadtxt(f"{DATASET}/{pose_file}")
            pose = np.linalg.inv(pose)
            visualizer.extrinsic2pyramid(pose, plt.cm.rainbow(idx_frame / len(flist)), 0.05)

    visualizer.show()

plot_framewise()