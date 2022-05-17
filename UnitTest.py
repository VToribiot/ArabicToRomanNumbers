import unittest as u
import main as m


class MyTestCase(u.TestCase):

    def test01(self):
        self.assertEqual("I", m.intToRom(1))

    def test02(self):
        self.assertEqual("LIII", m.intToRom(53))

    def test03(self):
        self.assertEqual("LXXXI", m.intToRom(81))

    def test04(self):
        self.assertEqual("DCCXLVI", m.intToRom(746))

    def test05(self):
        self.assertEqual("CCXXXIX", m.intToRom(239))

    def test06(self):
        self.assertEqual("MMMCDXCVI", m.intToRom(3496))

    def test07(self):
        self.assertEqual("MDXIX", m.intToRom(1519))

    def test08(self):
        self.assertFalse(m.validation("-96"))

    def test09(self):
        self.assertFalse(m.validation("1f5"))

    def test10(self):
        self.assertTrue(m.validation("136"))


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTestCase)
    u.TextTestRunner(verbosity=3).run(suite)

run()
