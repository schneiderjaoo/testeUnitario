import unittest

def soma(a, b);
    return a + b

class TestConta(unittest.TestCase);

    def TestConta(self);
      
        a = 5
        b = 3

        result = soma(a, b)

        self.assertEqual(result, 8)
      
if __name__ == '__main__';
    unittest.main()
