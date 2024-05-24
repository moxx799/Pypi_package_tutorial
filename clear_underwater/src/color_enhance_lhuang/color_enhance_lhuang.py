import torch
import numpy as np
import cv2
from torchvision import transforms
import numpy as np
from .model import PhysicalNN
import importlib.resources as pkg_resources
from color_enhance_lhuang import package_data

class Color_enhance_lhuang():
    
    def __init__(self,resize:int = -1):
        self.device = 'cpu' 
        self.unloader = transforms.ToPILImage()
        if resize == -1:            
            self.testtransform = transforms.Compose([transforms.ToTensor()])            
        else:            
            self.testtransform = transforms.Compose([transforms.ToTensor(),
                                                    transforms.Resize((resize))
                                                   ])
        self.model = self.conf_model()        
        
    def color_frame(self,frame):
        with torch.no_grad():
            frame = self.testtransform(frame).unsqueeze(0)
            frame = frame.to(self.device)        
            output_data = self.model(frame).squeeze().numpy()
            output_data = (np.transpose(output_data, [1, 2, 0]) * 255).astype(np.uint8)
        return cv2.cvtColor(output_data, cv2.COLOR_RGB2BGR)
          
    def conf_model(self,):    
        model = PhysicalNN()
        model = torch.nn.DataParallel(model).to(self.device)  
        with pkg_resources.path(package_data, 'model_best_2842.pth') as model_path:
        #checkpoint = 'model_best_2842.pth'  
            checkpoint = torch.load(model_path, map_location=self.device)
        model.load_state_dict(checkpoint['state_dict'])    
        model = model.module
        model.eval()        
        return model
