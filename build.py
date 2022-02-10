import subprocess
import os
import shutil


if os.path.isdir('./dist'):
    shutil.rmtree('./dist')

if os.path.isdir('./build'):
    shutil.rmtree('./build')

if os.path.isdir('./sikfa.egg-info'):
    shutil.rmtree('./sikfa.egg-info')

subprocess.run('pip freeze > requirements.txt', shell=True)
subprocess.run('python setup.py sdist bdist_wheel', shell=True)