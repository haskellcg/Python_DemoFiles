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

W, H = 256, 256
R = 1.0 * W / 3
D = 4
outputdir = "./output/"

yingyang = gz.Group([
                        gz.arc(R, 0, np.pi, fill = (0, 0, 0)),
                        gz.arc(R, -np.pi, 0, fill = (1, 1, 1)),
                        gz.circle(R / 2, xy = (-R / 2, 0), fill = (0, 0, 0)),
                        gz.circle(R / 2, xy = (R / 2, 0), fill = (1, 1, 1))
                    ])

fractal = yingyang

for i in range(5);
    fractal = gz.Group([
                        fractal.rotate(np.pi).scale(0.25).translate([R / 2, 0]),
                        fractal.scale(0.25).translate([-R / 2, 0]),
                        gz.circle(0.26 * R,
                                  xy = (-R / 2, 0),
                                  stroke = (1, 1, 1),
                                  stroke_width = 1),
                        gz.circle(0.26 * R,
                                  xy = (R / 2, 0),
                                  stroke = (0, 0, 0),
                                  stroke_width = 1)
                       ])

fractal = fractal
