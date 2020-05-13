import sys
import subprocess

for i in range(0, 5):
    subprocess.check_call([sys.executable, 'example.py'])