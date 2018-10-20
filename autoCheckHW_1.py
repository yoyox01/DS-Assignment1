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
    program1 = dirs[i] + '_1.c'

    # compile the 1st program with Linux command
    cd(dirs[i])
    subprocess.call('gcc '+program1+' -o '+dirs[i], shell=True)
    subprocess.call('cat ../../ans/input_1.txt | ./'+dirs[i]+' > ../../temp/tmpOut_1.txt', shell=True)

    cd('../../compare')
    print()
    print()
    print("====================",program1,"====================")
    subprocess.call('python3 autoCompare_1.py', shell=True)
    cd('../')
    cd('stuAns')

