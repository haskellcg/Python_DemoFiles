"""
  Information:
  * Date: 2017-11-25
  * Brief: use python script to pull all the updates to local disks
  * Author: haskellcg

  Platform: 
  * Windows7_x64
  * Python3.6_x64

"""

import os
import os.path
import sys
import subprocess

git_cmd = "git -C {0} pull git@github.com:haskellcg/{1}.git"

parent_dir_abspath = os.path.abspath(".")
subdir_names = os.listdir(parent_dir_abspath)

for subdir_name in subdir_names:
	if sys.argv[0] == subdir_name:
		continue

	workdir_path = os.path.join(parent_dir_abspath, subdir_name)
	subprocess.run(["cmd.exe", "/C", git_cmd.format(workdir_path, subdir_name)])
