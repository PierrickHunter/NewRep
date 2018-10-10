import unittest
import mycode as m

class mytest(unittest.TestCase):

    def test_hello_world():
        self.assertEqual(m.hello(), "hello world")


    def test_score_joseph(self):
        self.assertEqual(m.calculer_score("Joseph", "16"), "66")		#MODIFIE

    def test_score_marie(self):
        self.assertEqual(m.calculer_score("Marie", "33"), "50")

    def test_score_marc(self):
        self.assertEqual(m.calculer_score("Marc", "60"), "43")

    def test_score_ely(self):
        self.assertEqual(m.calculer_score("Broly", "28"), "75")


if __name__ == '__name__':
    unittest.main()