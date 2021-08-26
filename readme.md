# Squeeze-and-Residual-Excitation Holistic Attention Network
This repository is for Squeeze-and-Residual-Excitation Holistic Attention Network (HAN)

The model is built in PyTorch 1.8.1.

## Contents
1. [Introduction](#introduction)
2. [Network](#network)
3. [Test](#test)
4. [Results](#results)
5. [Citation](#citation)
6. [Acknowledgements](#acknowledgements)

## Introduction

Super-resolution (SR) provides an excellent approach of improving applications related to remote-sensing imagery. The tasks like object detection, classification and segmentation can greatly benefit from high-performing SR models. Substantial research is being carried out in the field of SR for both natural and remote-sensing imagery where deep convolutional neural networks (CNN) have achieved tremendous improvements. Many deep CNNs employ the attention mechanism in their structure and one such mechanism is the Squeeze-and-Excitation (SE) channel attention. While SE block has shown performance gains in many models, there is still room for improvement in its structure, therefore, in this paper, we propose the Squeeze-and-Residual-Excitation (SRE) attention block. SRE improves upon the SE block by employing residual mechanism within its structure to provide performance gain in SR. Based on our SRE attention mechanism, we propose an enhanced SR framework that outperforms other attention-based deep SR models for two levels of resolution enhancement: 4x- and 8x-upsampling on two diverse aerial imagery datasets: Satellite Imagery Multi-Vehicles Dataset (SIMD) consisting of 5000 high-resolution aerial images, and Cars-Overhead-With-Context (COWC). Moreover, by using YoloV5 object detection model, we perform numerous experiments to validate the effectiveness of our proposed SR model for the task of object detection on SIMD.

## Network

![SRE-HAN Super Resolution Framework](/figures/sre_han_complete.png)