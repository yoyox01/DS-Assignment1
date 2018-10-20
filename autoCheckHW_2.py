from sh import cd, ls
from natsort import natsorted
import os
import subprocess

cd('stuAns')
dirs = [d for d in
        os.listdir() if
        os.path.isdir(d)]
dirs = natsorted(dirs)
print(dirs)

for i in range(0, 5):
    program1 = dirs[i] + '_2.c'

    # compile the 1st program with Linux command
    print()
    print()
    print("====================",program1,"====================")
    cd(dirs[i])
    subprocess.call('gcc '+program1+' -o '+dirs[i], shell=True)
    subprocess.call('cat ../../ans/input_2.txt | ./'+dirs[i]+' > ../../temp/tmpOut_2.txt', shell=True)

    cd('../../compare')
    subprocess.call('python3 autoCompare_2.py', shell=True)
    cd('../')
    cd('stuAns')
