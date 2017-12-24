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
  * TypeError: Cannot cast ufunc add output from dtype('float64') to 
    dtype('uint8') with casting rule 'same_kind' => 

    change file "C:/Users/haskell/AppData/Local/Programs/Python/Python36/lib
    /site-packages/gizeh/gizeh.py", 40L, 

    from "arr += image.flatten()" to "arr += image.flatten().astype(uint8)"
  
'''

import numpy as np
import gizeh as gz
import moviepy.editor as mpy

outputdir = "./output/"

clip = mpy.VideoFileClip(outputdir + "movie_clip_animation.gif")
(w, h), d = clip.size, clip.duration
center = np.array([w / 2, h / 2])


def my_filter(get_frame, t):
    """
    Transform a frame (given by get_frame(t)) into
    a different frame, using vertor graphics
    """
    surface = gz.Surface(w, h)
    fill = (gz.ImagePattern(get_frame(t), pixel_zero = center)
              .scale(1.5, center = center))
    for (nfaces, angle, f) in ([3, 0, 1.0 / 6],
                               [5, np.pi / 3, 3.0 / 6],
                               [7, 2 * np.pi / 3, 5.0 / 6]):
        xy = (f * w, h * (0.5 + 0.05 * np.sin(2 * np.pi * (t / d + f))))
        shape = gz.regular_polygon(w / 6, nfaces, xy = xy,
                                   fill = fill.rotate(angle, center))

        shape.draw(surface)
    return surface.get_npimage()


clip.fl(my_filter).write_gif(outputdir + "animation_shapes_creation.gif")
