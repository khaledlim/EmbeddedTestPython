from pathlib import Path
import pytest
import os

def FindFirstFile(pf):
  for path in Path(pf).glob("*.exe"):
    path = str(path)
    #print(path)
    stats = os.stat(path)
    #print('Size of File is', stats.st_size, 'bytes')
    siza_file= stats.st_size
    if stats.st_size < 14680064:   # 14*2^20 = 14680064   16732160
      file = path
      #print("The needed file is "+ file)
      return file
      break
      
def test_FirstExistingFile(): 
  c = FindFirstFile("C:\Games\Pro Evolution Soccer 2017")
  print(c)