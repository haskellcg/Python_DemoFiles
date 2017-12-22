'''
  Information:
  * Date: 2017-12-21
  * Brief: create japanese flag gif with python
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
import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W, H = 200, 200
WSQ = W / 4
D = 2
a = np.pi / 8
points = [(0, 0), (1, 0), (1 - np.cos(a) ** 2, np.sin(2 * a) / 2), (0, 0)]
outputdir = "./output/"

def make_frame(t):
    pass

clip = mpy.VideoClip(make_frame, duration = D)
clip.write_gif(outputdir + "rotate_triangles.gif",
               fps = 15,
               fuzz = 30)
