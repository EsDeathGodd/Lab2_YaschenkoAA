import unittest
from calc import classifyTriangle,inputDataValidationAndCalculation,getTriangleCoordinates

class TestIfValidClass(unittest.TestCase):

    def test_classify(self):

        self.assertEqual(classifyTriangle(1,90,1),(4))
        self.assertEqual(classifyTriangle(1,1,1),(1))
        self.assertEqual(classifyTriangle(5,5,3),(2))
        self.assertEqual(classifyTriangle(3,4,5),(3))


class TestInputDataValid(unittest.TestCase):

    def test_inputData(self):
        #invalid
        self.assertEqual(inputDataValidationAndCalculation("a",90,1),(''))
        self.assertEqual(inputDataValidationAndCalculation(-2,90,1),('Arguments must be in a float type'))
        self.assertEqual(inputDataValidationAndCalculation((1,2,3),90,1),('Arguments must be in a float type'))
        self.assertEqual(inputDataValidationAndCalculation([1,2],90,1),('Arguments must be in a float type'))
        self.assertEqual(inputDataValidationAndCalculation({1:2},90,1),('Arguments must be in a float type'))
        self.assertEqual(inputDataValidationAndCalculation({1,2},90,1),('Arguments must be in a float type'))
        self.assertEqual(inputDataValidationAndCalculation(False,90,1),('Arguments must be in a float type'))
        #valid
        self.assertEqual(inputDataValidationAndCalculation(5.0,5.0,3.0),('Isosceles'))
        self.assertEqual(inputDataValidationAndCalculation(2.0,2.0,2.0),('Equilateral'))
        self.assertEqual(inputDataValidationAndCalculation(3.0,5.0,4.0),('Scalene'))


class TestGetTriangleCoords(unittest.TestCase):

    def test_coordinates(self):
        self.assertEqual(getTriangleCoordinates(2.0, 2.0, 2.0), [[0, 0], [2, 0], [0, 1]])
        self.assertEqual(getTriangleCoordinates(2.0,2.0,2.0),[[0, 0], [2, 0], [0, 1]])
        self.assertEqual(getTriangleCoordinates(3.0,5.0,4.0),[[0, 0], [3, 0], [1, -3]])
        self.assertEqual(getTriangleCoordinates(300000.0,5.0,4.0),([-1, -1], [-1, -1], [-1, -1]))
        self.assertEqual(getTriangleCoordinates(3.0,4.0,5.0),[[0, 0], [3, 0], [-3, -3]])
        self.assertEqual(getTriangleCoordinates(5.0,5.0,5.0),[[0, 0], [5, 0], [1, -4]])





