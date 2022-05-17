import unittest as u
import main as m


class MyTestCase(u.TestCase):

    def test01(self):
        self.assertEqual("I", m.intToRoman(1))

    def test02(self):
        self.assertEqual("LIII", m.intToRoman(53))

    def test03(self):
        self.assertEqual("LXXXI", m.intToRoman(81))

    def test04(self):
        self.assertEqual("DCCXLVI", m.intToRoman(746))

    def test05(self):
        self.assertEqual("CCXXXIX", m.intToRoman(239))

    def test06(self):
        self.assertEqual("MMMCDXCVI", m.intToRoman(3496))

    def test07(self):
        self.assertEqual("MDXIX", m.intToRoman(1519))

    def test08(self):
        self.assertFalse(m.validation("-96"))

    def test09(self):
        self.assertFalse(m.validation("1f5"))

    def test10(self):
        self.assertTrue(m.validation("136"))

    def test11(self):
        self.assertFalse(m.validation("6794"))

    def test12(self):
        self.assertFalse(m.validation("0"))


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTestCase)
    u.TextTestRunner(verbosity=3).run(suite)

run()
