from random import randint
import subprocess
import sys
from PIL import Image

size, path = 49, "/Users/deniskirienko4/Downloads/programms/fefu-study/learn_machine/img/linal1.2.2"

data = [x.replace('\n', '') for x in open(f"{path}/data.txt").readlines()]

showed, wrong, gone = 0, [], 0

used = []

while (len(used) < size):
    x = randint(1, size)
    if x not in used:
        used.append(x)

if sys.platform == "darwin":
    for j in range(len(used)):
        gone += 1
        
        i = used[j]+1
        
        print(data[i-2])
        
        choice = str(input())
        
        if choice == "b":
            break
            
        elif choice == "s":
            img = Image.open(f"{path}/{i-1}.png")
            img.show()
            
            showed += 1
            wrong.append(i-1)

        else:
            continue
        
print(f"showed: {showed}, passed: {gone-showed}, wrong: {wrong}")