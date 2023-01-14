import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numba import jit
import time
from multiprocessing import Pool 


@jit(nopython=True)
def blurfilter(in_img, out_img): 
    """ For each pixel in in_img calc the mean intensity values  
             using square 7x7 stencil""" 
    for c in range(3): 
        for x in range(in_img.shape[1]): 
            for y in range(in_img.shape[0]): 
                val = 0
                Range = [-3, -2, -1, 4, 5, 6] #0,1,2,3 are missing in the stencil (they are the dropouts)
                for i in Range: 
                    for j in Range: 
                        if ((x+i) < img.shape[1]) and (x+i >= 0) and ((y+j) < img.shape[0] ) and (y+j >= 0): 
                            val += (int(img[(y+j),(x+i),c] )) 
                          
            out_img[y,x,c] = val // 36

    
if __name__ == '__main__':
    start = time.time() 
    img = np.array(Image.open('noisy1.jpg'))
    print(img.shape)
    imgblur= img.copy()
    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    imgplot = plt.imshow(img)
    ax.set_title('Before')
    ax = fig.add_subplot(1, 2, 2)
    imgplot = plt.imshow(imgblur)
    ax.set_title('After')
    img2= Image.fromarray(imgblur)
    img2.save('blurred.jpg')
    end = time.time() 
    print("Execution time: ", end - start, " seconds")    