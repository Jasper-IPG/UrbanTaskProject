# "Заморозка кейсов"
import unittest
import tests_12_3


module12ST = unittest.TestSuite()
module12ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
module12ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

module_12 = unittest.TextTestRunner(verbosity=2)

module_12.run(module12ST)
