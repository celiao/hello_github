
# python3 test_hello_github.py -v

import unittest
import sys
sys.path.append("../hello_github")

import hello_github

class HelloCheck(unittest.TestCase):
    def testHello(self):
        ans = hello_github.theanswer()
        self.assertEqual(ans, 42)

if __name__ == "__main__":
    unittest.main()
