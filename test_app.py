import unittest
from app import add_patient


class TestPatientRegistration(unittest.TestCase):

    def test_valid_patient(self):
        patient = add_patient("Ravi", 25)
        self.assertEqual(patient["name"], "Ravi")
        self.assertEqual(patient["age"], 25)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            add_patient("", 25)

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            add_patient("Ravi", 0)


if __name__ == "__main__":
    unittest.main()
