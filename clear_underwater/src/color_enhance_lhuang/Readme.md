This package is grab from the original exellent work on https://github.com/xueleichen/PyTorch-Underwater-Image-Enhancement.git by Xuelei Chen.
May.2024, Liqiang Huang

The package is to use a deep learning pretrained model to preprocess the underwater image.
This version is set to work in the cpu, the code can also be run in gpu, but need to change the cpu to cuda, and use a gpu-based pytorch environment.
The main part is in Color_enhance_lhuang (python class), which is in the `src/color_enhance_lhuang/color_enhance_lhuang.py`, it involves three steps
* config the pretrained model:  conf_model(self,)
* preprocessing the tensor: testtransform = transforms.Compose
* prediction: color_frame(self,frame)

The model in `model.py` and the pretrained parameters in `package_data/model_best_2842.pth` is taken from the Xuelei chen and you can replace them with other models.
The transform(preprocessing) step should also keep the same as the author who provide the code.
The prediction part is predicted frame by frame and the I/O are all in the type of cv2.BGR.

After install it, you can use the code `clear_underwater/tests/pred_mp4_hp.py` to process the video in our cpu device.
