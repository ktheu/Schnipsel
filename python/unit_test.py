import unittest
class MyClassTest(unittest.TestCase):
    def test_init(self):
        m = MyClass(....)
        self.assertEqual(m.attribut,...)

    def test_methods(self):
        p = Punkt(-1,3)
        self.assertEqual(p.quadrant(),2)
        self.assertFalse(p.liegtAufAchse())
        self.assertIs(type(r),Rikscha)
        self.assertIs((r.__class__.__base__),Fahrzeug)
        self.assertListEqual(fp.fahrzeuge,[])
        # assertDictEqual,assertSetEqual,assertTupelEqual,assertAlmostEqual
    def test_funktion01(self):
        with self.assertRaises(RuntimeError):
           funktion01(-1)
if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main(exit=False)    # für Thonny
