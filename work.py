def triangle(a, b, c):
    if a + b <= c:
        return "错误"
    triangle_type = ""
    if a == b == c:
        triangle_type = "等边"
    elif a == b or b == c or a == c:
        triangle_type = "等腰"
    else:
        triangle_type = "一般"

    if a ** 2 + b ** 2 == c ** 2:
        triangle_type += "直角"
    return triangle_type

print(triangle(1, 1, 1))
print(triangle(1, 2, 3))
print(triangle(3, 3, 3))
print(triangle(3, 4, 5))

import unittest

class TestTriangle(unittest.TestCase):
    def test_triangle1(self):
        self.assertEqual(triangle(0, 0, 0), "错误")
    def test_triangle2(self):
        self.assertEqual(triangle(1, 1, 1), "等边")
    def test_triangle3(self):
        self.assertEqual(triangle(1, 3, 2), "错误")
      suite = unittest.TestLoader().loadTestsFromTestCase(TestTriangle)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

def triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    if a + b <= c:
        return "错误"
    triangle_type = ""
    if a == b == c:
        triangle_type = "等边"
    elif a == b or b == c or a == c:
        triangle_type = "等腰"
    else:
        triangle_type = "一般"

    if a ** 2 + b ** 2 == c ** 2:
        triangle_type += "直角"
    return triangle_type
suite = unittest.TestLoader().loadTestsFromTestCase(TestTriangle)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
