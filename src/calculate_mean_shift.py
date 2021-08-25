import os
import glob
from torch.utils.data import DataLoader, Dataset
from torchvision.transforms import ToTensor
from tqdm import tqdm
from PIL import Image
import numpy as np
import cv2

import torch

dir = "D:\Bostan\COWC\COWC_NEW\COWC_SR_Blurr_downsampled\COWC\COWC_train_HR"
img_list=sorted(os.path.join(dir, file) for file in os.listdir(dir) if
             os.path.isfile(os.path.join(dir, file)) and os.path.splitext(file)[1] == '.png')

print(len(img_list))

mean = 0.
std = 0.
nb_samples = 0.
i=0
rgb = [0,0,0]
for j in range(3):
    i=0
    mean = 0
    for _,path in enumerate(tqdm(img_list)):
        image = cv2.imread(path)
        val = np.reshape(image[:, :, j], -1)
        img_mean = np.mean(val)
        #img_std = np.std(val)
        mean += img_mean
        i=i+1
    rgb[j] = mean/i

print(rgb)
