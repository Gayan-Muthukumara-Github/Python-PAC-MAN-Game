
x = 1
y = 256

while True:
    print(x)
    if x > 255:
        x = 0
        
    if y > 255:
        y = 0
        
    if y == x:
        break
    
    x += 1