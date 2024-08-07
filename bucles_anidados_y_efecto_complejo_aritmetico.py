import time
start_time = time.time()


#Bucle exterior
for i in range(10):
    #bucle interior 
    for j in range(100):
        print(0, end = " ")
    print()

print(round((time.time() - start_time), 2))