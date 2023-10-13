from loguru import logger
from typing import Tuple
from calc import inputDataValidationAndCalculation, getTriangleCoordinates

logger.add("triangles.log")


def getTriangleTypeAndCoords(a: float, b: float, c: float) -> Tuple[str, Tuple[float,float]]: 

    logger.debug(f"a:{a}, b:{b}, c:{c} result:{inputDataValidationAndCalculation(a, b, c)} , triangle coordinates:{getTriangleCoordinates(a, b, c)}") # logs both tho


    return inputDataValidationAndCalculation(a,b,c), getTriangleCoordinates(a,b,c)

print(getTriangleTypeAndCoords(50.0,60.0, ""))



