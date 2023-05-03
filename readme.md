# Squeeze-and-Residual-Excitation Holistic Attention Network For Improved Super Resolution in Remote Sensing Imagery
Squeeze-and-Residual-Excitation Holistic Attention Network improves super-resolution (SR) on remote-sensing imagery compared to other state-of-the-art attention-based SR models.

The model is built in PyTorch 1.8.1. 

## Contents
1. [Introduction](#introduction)
2. [Network](#network)
3. [Setup](#setup)
4. [Test](#test)
5. [Results](#results)
6. [Acknowledgements](#acknowledgements)

## Introduction

Super-resolution (SR) provides an excellent approach of improving applications related to remote-sensing imagery. The tasks like object detection, classification and segmentation can greatly benefit from high-performing SR models. Substantial research is being carried out in the field of SR for both natural and remote-sensing imagery where deep convolutional neural networks (CNN) have achieved tremendous improvements. Many deep CNNs employ the attention mechanism in their structure and one such mechanism is the Squeeze-and-Excitation (SE) channel attention. While SE block has shown performance gains in many models, there is still room for improvement in its structure, therefore, in this paper, we propose the Squeeze-and-Residual-Excitation (SRE) attention block. SRE improves upon the SE block by employing residual mechanism within its structure to provide performance gain in SR. Based on our SRE attention mechanism, we propose an enhanced SR framework that outperforms other attention-based deep SR models for two levels of resolution enhancement: 4x- and 8x-upsampling on two diverse remote sensing imagery datasets: Satellite Imagery Multi-Vehicles Dataset (SIMD) consisting of 5000 high-resolution remote sensing images, and Cars-Overhead-With-Context (COWC). Moreover, by using YoloV5 object detection model, we perform numerous experiments to validate the effectiveness of our proposed SR model for the task of object detection on SIMD.

## Setup
The setup can be done through one  of the following methods:

1. A new environment can be created using the 'requirements.yml' file by executing the following command:
   ```bash
   conda env create -f requirements.yml
    ```
2. Or it can also be created through the given "conda_environment.txt" file.
    ```bash
   conda create --name sre-han --file conda_environment.txt
    ```

Use the created environment for testing and performing experiments.

## Test

Place images that you want to upsample in the 'demo/low_res_images' folder

CD to 'src' and run one of the following script

The upsampled images will be found in the 'demo/results/results-Demo' folder.

```bash
#for 4x upsampling
python main.py --template 4X_SRE_HAN --pre_train ../trained_models/sre_han_x4.pt --n_GPUs=2 --data_test Demo --dir_demo ../demo/low_res_images --test_only --save ../demo/results --save_results

#for 8x upsampling
python main.py --template 8X_SRE_HAN --pre_train ../trained_models/sre_han_x8.pt --n_GPUs=2 --data_test Demo --dir_demo ../demo/low_res_images --test_only --save ../demo/results --save_results
```

## Results

### SR Results

The super-resolution performance over the Satellite Imagery Multi-Vehicles Dataset of our model and three previous state-of-the-art models are shown in this section. Our model outperforms the other models for both 4x and 8x upsampling.

![Results](/figures/results.png)

### Object Detection 8x SR Results

We use YoloV5-Medium mopel presented by Glenn Jocher to perform two types of object detection experiments.

#### Experiment 1:
YoloV5-Medium is trained and evaluated on the upsampled versions of the dataset obtained through using the super-resolution models. The results are as follows:

![Detection Results](/figures/8x_Detection_Results.png)

#### Experiment 2:
YoloV5-Medium is trained over the ground truth dataset and then evaluated on the upsampled versions of the test set obtained through using the SR models.

![Detection Results2](/figures/8x_detection_results2.png)

### Visual Results for 8x Upsampling and Consequent Object Detection

The visual results for the performance of the object detection model that has been trained on the ground truth dataset and then evaluated on the images upsampled through bicubic method and SRE-HAN model are shown here. 

![Visual Detection Results](/figures/8x_visual_detection_results.png)
Ground truth trained YoloV5 Object Detection Model is applied over both of the above images and we can see that the detection model is unable to detection any of the vehicles in the bicubic upsampled image. On the other hand, Yolov5 detects many of the objects in the image upsampled through our SRE-HAN model.

![Visual Detection Results2](/figures/8x_visual_detection_results2.png)
Similarly, in the bicubic upsampled image the detection model detects only 1 object, whereas in the SRE-HAN upsampled image all of the objects have been detected except one.
