"""
  Information:
  * Date: 2017-12-24
  * Brief: create black white flowers gif with python
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
  
"""

import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W, H = 400, 400
D = 5
ncircles = 10
outputdir = "./output/"

def make_frame(t):
    surface = gz.Surface(W, H)
    for angle in np.linspace(0, 2 * np.pi, ncircles + 1)[:-1]:
        center = np.array([W / 2, H / 2]) + gz.polar2cart(0.2 * W, angle)
        for i in [0, 1]:
            circle = gz.circle(W * 0.45 * (i + t / D),
                               xy = center,
                               fill = (1, 1, 1, 1.0 / 255))
            circle.draw(surface)
    return 255 * ((surface.get_npimage() + 1) % 2)

clip = mpy.VideoClip(make_frame, duration = D).resize(0.5)
clip.write_gif(outputdir + "black_white_flowers_creation.gif", fps = 15, fuzz = 30, opt = "OptimizePlus")
