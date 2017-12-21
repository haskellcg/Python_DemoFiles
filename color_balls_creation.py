'''
  Information:
  * Date: 2017-12-21
  * Brief: create color balls gif with python
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

import gizeh as gz
import numpy as np
import moviepy.editor as mpy

W, H = 150, 150
duration = 2
nballs = 60
outputdir = "./output/"

# generate random values of radius, color, center
radiuses = np.random.randint(0.1 * W, 0.2 * W, nballs)
colors = np.random.rand(nballs, 3)
centers = np.random.randint(0, W, (nballs, 2))

def make_frame(t):
    surface = gz.Surface(W, H)
    for radius, color, center in zip(radiuses, colors, centers):
        angle = 2 * np.pi * ((t / duration * np.sign(color[0] - 0.5)) + color[1])
        xy = center + gz.polar2cart(W / 5, angle)
        gradient = gz.ColorGradient(type = "radial",
                                    stops_colors = [(0, color), (1, color / 10)],
                                    xy1 = [0.3, -0.3],
                                    xy2 = [0, 0],
                                    xy3 = [0, 1.4])
        ball = gz.circle(r = 1, fill = gradient).scale(radius).translate(xy)
        ball.draw(surface)
        
    return surface.get_npimage()
    
clip = mpy.VideoClip(make_frame, duration = duration)    
clip.write_gif(outputdir + "color_balls_creation.gif", fps = 15, opt = "OptimizePlus")