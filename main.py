import os
from random import randint
import sys
from PIL import Image
import io

# print(os.path.dirname(os.path.abspath(__file__)))

size = 49
if sys.platform == "win32":
    path = "D:/programms/learn_machine/data/linal1.2.2"
if sys.platform == "darwin":
    path = "/Users/deniskirienko4/Downloads/programms/fefu-study/learn_machine/data/linal1.2.2"

data = [x.replace('\n', '') for x in io.open(f"{path}/data.txt", encoding='utf-8').readlines()]

showed, wrong, gone = 0, [], 0

used = []

while (len(used) < size):
    x = randint(1, size)
    if x not in used:
        used.append(x)

for j in range(len(used)):
    gone += 1
    
    i = used[j]+1
    
    print(data[i-2], f"{j+1}/49")
    
    choice = str(input())
    
    if choice in ["b", "и"]:
        break
        
    elif choice in ["s", "ы"]:
        img = Image.open(f"{path}/img/{i-1}.png")
        img.show()
        
    elif choice in ["j", "о"]:
        img = Image.open(f"{path}/img/{i-1}.png")
        img.show()
        
        showed += 1
        wrong.append(i-1)

    else:
        continue

with open(f"{path}/result.txt", 'w') as file:
    file.write(str(wrong)+'\n')

print(f"showed: {showed}, passed: {gone-showed}, wrong: {wrong}")