# 3D Object Detection with Pointformer

This repository contains the code for the paper VG-TAMP: Visually-Grounded Task-and-Motion Planning in 3D Household Environments.

This work is developed on the top of [MMDetection3D](https://github.com/open-mmlab/mmdetection3d) toolbox, the model is based on [Pointformer](https://github.com/Vladimir2506/Pointformer), and we edited it to apply on the **ALFRED** dataset in the paper. 

## Installation and Usage

### Dependencies

- NVIDIA GPU + CUDA 11.2
- Python 3.8 (Recommend to use Anaconda)
- PyTorch == 1.10.0+cu113
- [mmcv-full](https://github.com/open-mmlab/mmcv) == 1.3.17
- [mmdet](https://github.com/open-mmlab/mmdetection) == 2.18.1
- [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) == 0.19.0

### Installation

1. Install dependencies following their guidelines.
2. Clone and install [mmdet3d](https://github.com/open-mmlab/mmdetection3d) in develop mode.

```
git clone https://github.com/open-mmlab/mmdetection3d.git
cd mmdetection3d
python setup.py develop
```

3. Update the files in this repo into the directories in mmdet3d.

### Data Preprocessing

Please refer to [alfred](./data/alfred/README.md) for more detail

#### Train and Test

```
# Training
bash tools/dist_train.sh configs/pointformer/votenet_ptr_alfred-3d-class.py 8

# Testing 
bash tools/dist_test.sh configs/pointformer/votenet_ptr_alfred-3d-class.py checkpoints/votenet_ptr_alfred-3d-class.pth 8 --eval mAP
```

## Acknowledgement

This code is based on [MMDetection3D](https://github.com/open-mmlab/mmdetection3d) and [Pointformer](https://github.com/Vladimir2506/Pointformer)
