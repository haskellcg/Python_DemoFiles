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
    将bin目录加入环境变量
  
'''

import gizeh
import moviepy.editor as mpy

W, H = 128, 128
duration = 2.35
outputdir = "./output/"

# 注意Surface函数首字母大写
surface = gizeh.Surface(width = 320, height = 260)
circle = gizeh.circle(r = 40, xy = [156, 200], fill = (1, 0, 0))
circle.draw(surface)
surface.get_npimage()
surface.write_to_png(outputdir + "japanese_flag_1.png")

def make_frame(t):
    surface = gizeh.Surface(W, H)
    radius = W * (1 + (t * (duration - t)) ** 2) / 6
    circle = gizeh.circle(radius, xy = (W / 2, H / 2), fill = (1, 0, 0))
    circle.draw(surface)
    return surface.get_npimage()
    
clip = mpy.VideoClip(make_frame, duration = duration)
clip.write_gif(outputdir + "japanese_flag_1.gif", fps = 80, opt = "OptimizePlus", fuzz = 10)

