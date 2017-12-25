"""
  Information:
  * Date: 2017-12-25
  * Brief: create up down thermal map gif with python
  * Author: haskellcg

  Platform: 
  * Windows7_x64
  * Python3.6_x64
      
  Libs:
  * vtk (pip install vtk)
  * mayavi (pip install mayavi)
    * apptools
    * traits
    * traitsui
    * configobj
    * pyface
    * six
    * pygments
    
  Problems:
  * ImportError: Could not import backend for traits => 
    目前无法解决,只支持python2.7
  
"""

from traits.etsconfig.api import ETSConfig
ETSConfig.toolkit = "wx"

import numpy as np
import mayavi.mlab as mlab
import moviepy.editor as mpy

# duration of the animation in seconds (it will loop)
duration = 2
outputdir = "./output/"

# Make a figure with mayavi

fig_myv = mlab.figure(size = (220, 220),
                      bgcolor = (1, 1, 1))
X, Y = np.linspace(-2, 2, 200), np.linspace(-2, 2, 200)
XX, YY = np.meshgrid(X, Y)
ZZ = lambda d: np.sinc(XX ** 2 + YY ** 2) + np.sin(XX + d)

# Animate the figure with moviepy, write an animated gif

def make_frame(t):
    # clear the figure (to reset the colors)
    mlab.clf()
    mlab.mesh(YY, XX, ZZ(2 * np.pi * t / duration), figure = fig_myv)
    return mlab.screenshot(antialiased = True)

animation = mpy.VideoClip(make_frame, duration = duration)
animation.write_gif(outputdir + "up_down_thermal_map_animation.gif",
                    fps = 20)
