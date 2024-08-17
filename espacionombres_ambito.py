'''
animalfarm.py
'''

def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("inside nesten function " + animal)
        
    print("defore calling function: " + animal)
    e()
    print("After nested function: " + animal)

animal  = "camel"
d()
print("Global animal: " + animal)