import color_enhance_lhuang.color_enhance_lhuang
import numpy as np
import time
import argparse
import cv2
import numpy as np
from color_enhance_lhuang.color_enhance_lhuang import Color_enhance_lhuang

parser = argparse.ArgumentParser()
parser.add_argument('--video_path', type=str,default='C:/Users/50274/Desktop/underwater/rspi_develop/original_video/WIN_20230913_18_46_41_Pro.mp4', help='video path')
parser.add_argument('--ttime', type=int, default=30, help='Time of operation')
parser.add_argument('--cap_size', type=tuple, default=(1280, 960), help='The capture video resolution')
parser.add_argument('--model_size', type=int, default=256, help='The input shape of the model')
parser.add_argument('--fps', type=float, default=20.0, help='fps')
args = parser.parse_args()
  
def main():
    
    cap = cv2.VideoCapture(args.video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # or 'XVID'
    out = cv2.VideoWriter(args.video_path.replace('.mp4','_enh.avi'), fourcc, args.fps, args.cap_size)
    timecosts = []
    color_enh = Color_enhance_lhuang(args.model_size)
   
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_start = time.time()        
        output = color_enh.color_frame(frame)   
        output = cv2.resize(output, args.cap_size) 
        out.write(output)  
        frame_cost = time.time() - frame_start
        timecosts.append(frame_cost)
        
    cap.release()
    out.release()
    print('Average color enhancement time costs:', sum(timecosts) / len(timecosts))
    
if __name__ == '__main__':
    main()
