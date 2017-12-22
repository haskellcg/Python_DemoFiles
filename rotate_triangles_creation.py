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
    surface = gz.Surface(W, H)
    for k, (c1, c2) in enumerate([[(0.7, 0.05, 0.05), (1, 0.5, 0.5)], 
                                  [(0.05, 0.05, 0.7), (0.5, 0.5, 1)]]):
        grad = gz.ColorGradient("linear",
                                xy1 = (0, 0),
                                xy2 = (1, 0),
                                stops_colors = [(0, c1), (1, c2)])
        r = min(np.pi / 2, max(0, np.pi * (t - D / 3) / D))
        triangle = gz.polyline(points,
                               xy = (-0.5, 0.5),
                               fill = grad,
                               angle = r,
                               stroke = (1, 1, 1),
                               stroke_width = 0.02)
        square = gz.Group([triangle.rotate(i * np.pi / 2) for i in range(4)])
        squares = (gz.Group([square.translate((2 * i + j + k, j)) 
                             for i in range(-3, 4) 
                             for j in range(-3, 4)])
                     .scale(WSQ)
                     .translate((W / 2 - WSQ * t / D, H / 2)))
        squares.draw(surface)

    return surface.get_npimage()


clip = mpy.VideoClip(make_frame, duration = D)
clip.write_gif(outputdir + "rotate_triangles.gif",
               fps = 15,
               fuzz = 30)
