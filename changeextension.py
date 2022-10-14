import os

k = os.listdir("./InputImages")
l = str(k[0])
c = "3c9dd9ddf1bfef052b4f64eeffc40abc"
d = "cp2.jpeg"
os.rename(k[0],d)

j = os.listdir("./InputImages")

print(j)