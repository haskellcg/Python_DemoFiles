"""
  Information:
  * Date: 2017-12-22
  * Brief: create stacked circles gif with python
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
DURATION = 2.0
NDISKS_PER_CYCLE = 8
SPEED = 0.05
outputdir = "./output/"

def make_frame(t):
    dt = 1.0 * DURATION / 2 / NDISKS_PER_CYCLE
    N = int(NDISKS_PER_CYCLE / SPEED)
    t0 = 1.0 / SPEED

    surface = gz.Surface(W, H)
    for i in range(1, N):
        a = (np.pi / NDISKS_PER_CYCLE) * (N - i - 1)
        r = np.maximum(0, 0.05 * (t + t0 - dt * (N - i - 1)))
        center = W * (0.5 + gz.polar2cart(r, a))
        color = 1 * ((1.0 * i / NDISKS_PER_CYCLE) % 1.0, 1, 0)
        circle = gz.circle(r = 0.3 * W,
                           xy = center,
                           fill = color,
                           stroke_width = 0.01 * W)
        circle.draw(surface)

    contour1 = gz.circle(r = 0.65 * W,
                         xy = [W / 2, W / 2],
                         stroke_width = 0.5 * W)
    contour2 = gz.circle(r = 0.42 * W,
                         xy = [W / 2, W / 2],
                         stroke_width = 0.02 * W,
                         stroke = (1, 1, 1))
    contour1.draw(surface)
    contour2.draw(surface)
    return surface.get_npimage()




clip = mpy.VideoClip(make_frame, duration = DURATION)
clip.write_gif(outputdir + "stacked_circles.gif", 
               fps = 20, 
               opt = "OptimizePlus", 
               fuzz = 10)
