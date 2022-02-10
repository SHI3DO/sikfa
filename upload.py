import subprocess


subprocess.run('twine upload dist/*',shell=True)