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
import moviepy.editor as mpy
import moviepy.video.tools.cuts as cuts

src_video = "./resources/test.mp4"
outputdir = "./output/"
start_time = (10, 4)
end_time = (10, 14)

clip = mpy.VideoFileClip(src_video).resize(0.3).subclip(start_time, end_time)
# change cuts length by changing parameter "tmin" to 10:14 - 10.4 - 0.1
t_loop = cuts.find_video_period(clip, tmin = 9.9)
clip.subclip(0, t_loop).write_gif(outputdir + "movie_clip_animation.gif",
                                  opt = "OptimizePlus")
