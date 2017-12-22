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

W, H = 300, 75
D = 2
r = 22
outputdir = "./output/"

gradient = gz.ColorGradient("linear",
                            ((0, (0, 0.5, 1)), (1, (0, 1, 1))),
                            xy1 = (0, -r),
                            xy2 = (0, r))
polygon = gz.regular_polygon(r, 5, stroke_width = 3,
                             fill = gradient)

def make_frame(t):
    surface = gz.Surface(W, H, bg_color = (1, 1, 1))
    for i, letter in enumerate("GIZEH"):
        angle = max(0, min(1, 2 * t/D - 1.0 * i / 5)) * 2 * np.pi
        txt = gz.text(letter, "Amiri", 3 * r / 2, fontweight = "bold")
        group = (gz.Group([polygon, txt])
                   .rotate(angle)
                   .translate((W * (i + 1) / 6, H / 2)))
        group.draw(surface)

    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration = D)
clip.write_gif(outputdir + "rotate_words.gif",
               fps = 20,
               opt = "OptimizePlus")
