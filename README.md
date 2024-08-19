## 畸变图片:

<img src="./README.assets/image-20240819173746385.png" alt="image-20240819173746385" style="zoom:80%;" />

## 去畸变后的图片：

<img src="./README.assets/image-20240819173800961.png" alt="image-20240819173800961" style="zoom:80%;" />

## 1. 总体流程

![image-20240819174215839](./README.assets/image-20240819174215839.png)

## 2. 安装所需依赖

```shell
pip install opencv-python 
pip install numpy 
pip install scipy
```

## 3. 执行推理代码

```shell
python undistorted_img.py
```

执行后会弹出一个显示窗口左边为畸变的图片， 右边为去畸变的图片：

![image-20240819173941268](./README.assets/image-20240819173941268.png)

同时上图会保存到当前目录，名称为：`distorted_image_and_undistorted_image.jpg`



