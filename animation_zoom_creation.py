"""
  Information:
  * Date: 2017-12-24
  * Brief: create animation zoom gif with python
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
  
"""

import gizeh as gz
import numpy as np
import moviepy.editor as mpy

outputdir = "./output/"

def add_zoom(clip, target_center, zoom_center, zoom_radius, zoomx):
    w, h = clip.size

    def fl(im):
        """
        transform the image by adding a zoom
        """
        surface = gz.Surface.from_image(im)
        fill = gz.ImagePattern(im,
                               pixel_zero = target_center,
                               filter = "best")
        line = gz.polyline([target_center, zoom_center], stroke_width = 3)
        circle_target = gz.circle(zoom_radius,
                                  xy = target_center,
                                  fill = fill,
                                  stroke_width = 2)
        circle_zoom = (gz.circle(zoom_radius,
                                 xy = zoom_center,
                                 fill = fill,
                                 stroke_width = 2)
                         .scale(zoomx, center = zoom_center))
        for e in line, circle_zoom, circle_target:
            e.draw(surface)

        return surface.get_npimage()

    return clip.fl_image(fl)


clip = mpy.VideoFileClip(outputdir + "movie_clip_animation.gif")
w, h = clip.size
clip_with_zoom = clip.fx(add_zoom,
                         target_center = [w * 2.5 / 7, h * 1/ 2],
                         zoomx = 3,
                         zoom_center = [5 * w / 6, h / 4],
                         zoom_radius = 30)
clip_with_zoom.write_gif(outputdir + "animation_zoom_creation.gif")
