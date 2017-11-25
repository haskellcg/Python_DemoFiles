import os
import os.path
import subprocess

git_cmd = "git -C {0} pull origin master"

parent_dir_abspath = os.path.abspath(".")
subdir_names = os.listdir(parent_dir_abspath)

for subdir_name in subdir_names:
	workdir_path = os.path.join(parent_dir_abspath, subdir_name)
	subprocess.run(["cmd.exe", "/C", git_cmd.format(workdir_path)])
