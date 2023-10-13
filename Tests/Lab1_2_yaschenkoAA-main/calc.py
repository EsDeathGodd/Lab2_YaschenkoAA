import math

def classifyTriangle(a: float, b: float, c: float) -> int:
    if a + b <= c or a + c <= b or b + c <= a: # not valid

        return 4
    if a == b == c: # equilateral

        return 1
    elif a == b or a == c or b == c: # isosceles

        return 2
    else: # scalene

        return 3

def inputDataValidationAndCalculation(a: float, b: float, c: float) -> str:
    if any(isinstance(arg, str) for arg in [a, b, c]):

        return ""


    if not all(isinstance(arg, float) for arg in [a,b,c]): # if not arguments are defined as float returning false

        return "Arguments must be in a float type"
    
    else:
        triangle_type = classifyTriangle(a,b,c)

        match triangle_type:

            case 1:

                return "Equilateral"
        
            case 2:

                return "Isosceles"
        
            case 3:

                return "Scalene"
            
            case 4:

                return "Not a valid triangle"

        
    
def getTriangleCoordinates(a: float, b: float, c: float):
    if inputDataValidationAndCalculation(a, b, c) == "" or inputDataValidationAndCalculation(a, b, c) == "Arguments must be in a float type":

        return ([-2,-2], [-2,-2], [-2,-2])
    elif inputDataValidationAndCalculation(a, b, c) == "Not a valid triangle":

        return ([-1,-1], [-1,-1], [-1,-1])
    
    else:
        vertices = [[0, 0], [int(a), 0], [int(c*math.cos(b)), int(c*math.sin(b))]]

        return vertices


