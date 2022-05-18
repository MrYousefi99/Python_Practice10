class Shape ():
    
    def __init__(self,length,width,redius):
        self.length = length
        self.width = width
        self.redius = redius
    

class Circle(Shape):
     def __init__(self,length,width,redius):
            super().__init__(length,width,redius)
        
     
     def env (self):
         res = self.redius*3.14*2
         print("\nCircles Environment is : ",res)      
     def are(self):
         res = self.redius*self.redius*3.14
         print("\nCircles Area is : ",res)    


class Rectangle(Shape):
     def __init__(self,length,width,redius):
        super().__init__(length,width,redius)
  
     
     def env (self):
         res = (  self.length+self.width)*2
         print("\nRectangles Environment is : ",res)      
     def are(self):
         res =   self.length*self.width
         print("\nRectangle Area is : ",res)    



print("Please Insert the numbers \n")

a = int(input("Please insert the length :"))
b = int(input("Please insert the width :"))
c = int(input("Please insert the redius :"))

while True :
    print("\n1 - Circle  2- Rectangle\n")

    n = int(input("Please insert the number :")) 
        
    if n == 1 :
            cr = Circle(a,b,c)
            print("1 - Environment  2- Area\n")
            m = int(input("Please insert the number :\n")) 
            
            if m == 1 :
                cr.env()
            elif m == 2 :
                cr.are()    
        
    elif n == 2 :
            rt = Rectangle(a,b,c)
            print("1 - Environment  2- Area\n")
            m = int(input("Please insert the number :\n")) 
            
            if m == 1 :
                rt.env()
            elif m == 2 :
                rt.are()   


        
                    