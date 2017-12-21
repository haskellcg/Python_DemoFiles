'''
  Information:
  * Date: 2017-12-21
  * Brief: create black white circles gif with python
  * Author: haskellcg

  Platform: 
  * Windows7_x64
  * Python3.6_x64
      
  Libs:
  * moviepy (pip install moviepy)
    * decorator
    * imageio
    * olefile
    * pillow
    * tqdm
  * gizeh (VC++ 14.0: http://landinghub.visualstudio.com/visual-cpp-build-tools)
    * cairocffi
    * cffi
    * pycparser
    
  Problems:
  * OSError: dlopen() failed to load a library: cairo / cairo-2 => 下载GTK+，并
    将bin目录加入环境变量(http://win32builder.gnome.org/)
  
'''

import gizeh
import numpy as np
import moviepy.editor as mpy

W, H = 128, 128
duration = 2
ncircles = 100
outputdir = "./output/"

def make_frame(t):
    surface = gizeh.Surface(W, H)
    
    for i in range(ncircles):
        angle = 6 * np.pi * ((1.0 * i / ncircles) + (t / duration))
        center = W * (0.5 + gizeh.polar2cart(0.1, angle))
        circle = gizeh.circle(r = W * (1.0 - 1.0 * i / ncircles),
                              xy = center,
                              fill = (i % 2, i % 2, i % 2))
        circle.draw(surface)
        
    return surface.get_npimage()
    
clip = mpy.VideoClip(make_frame, duration = duration)
clip.write_gif(outputdir + "black_white_circles.gif", fps = 15, opt = "OptimizePlus", fuzz = 10)

