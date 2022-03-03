import unittest
import combiningcsvsinfolder as comb
import sys


class TestCombine_pdf (unittest.TestCase):
    def combine_pdf_test(self):
        self.assertAlmostEqual(comb.combine_pdf(sys.argv[1],"temp.csv"),1)

if __name__=="__main__":
    unittest.main()