
This package is to do the color enhancement in cpu device for each frame.
The input/output are all cv2.BGR format and the values are from [0,255].
This package is grab from the original exellent work from https://github.com/xueleichen/PyTorch-Underwater-Image-Enhancement.git by Xuelei Chen.

It only works in cpu, if you want to use GPU, I assume you know how deep learning works and you can find how to use it in my github repo.

# Requirements
["Pillow=9.4.0",
"pytorch=2.2.2" -c pytorch,
"torchvision=0.17.2",
opencv-python==4.9.0.80,
]
and install our package by pip
`pip install -i https://test.pypi.org/simple/ color-enhance-lhuang`
# How to use it
After install the packages,
`from color_enhance_lhuang.color_enhance_lhuang import Color_enhance_lhuang`
you need to create a instance of the class,
`color_enh = Color_enhance_lhuang(args.model_size)`
`output = color_enh.color_frame(frame)`
args.model_size is to determine the model_size, if it is -1, then the model will handle the image with the original one,
you can specific the model size such as the common one (256,512, etc..).
The output is the Deep learning color enhancement results as the same of the frame which is captured by cv2.

Please see more details in the github
`https://github.com/moxx799/Pypi_package_tutorial.git`
