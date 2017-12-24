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

import colorsys
import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W, H = 256, 256
NFACES = 5
R = 0.3
NSQUARES = 100
DURATION = 2
outputdir = "./output/"

def half(t, side = "left"):
    points = list(gz.geometry.polar_polygon(NFACES, R, NSQUARES))
    ipoint = 0 if side == "left" else NSQUARES // 2
    points = (points[ipoint:] + points[:ipoint])[::-1]

    surface = gz.Surface(W, H)
    for (r, th, d) in points:
        center = W * (0.5 + gz.polar2cart(r, th))
        angle = -(6 * np.pi * d + t * np.pi / DURATION)
        color = colorsys.hls_to_rgb((2 * d + t / DURATION) % 1, 0.5, 0.5)
        square = gz.square(l = 0.17 * W,
                           xy = center,
                           angle = angle,
                           fill = color,
                           stroke_width = 0.005 * W,
                           stroke = (1, 1, 1))
        square.draw(surface)
    im = surface.get_npimage()
    return (im[:, :W // 2] if side == "left" else im[:, W // 2:])

def make_frame(t):
    return np.hstack([half(t, "left"), half(t, "right")])


clip = mpy.VideoClip(make_frame, duration = DURATION)
clip.write_gif(outputdir + "rotate_squares_creation.gif", fps = 15, opt = "OptimizePlus")
