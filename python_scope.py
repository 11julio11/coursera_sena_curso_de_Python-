#global scope
my_global = 10

def fn1():
    
    enclosed_v = 8
    
    def fn2():
        local_v = 5
        print('access to global', my_global)
        print('access to enclosed', enclosed_v)
    fn2()

fn1()
      
    
