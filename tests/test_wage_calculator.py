import unittest
from wage_calculator import Staff


class TestWageCalculator(unittest.TestCase):

    def setUp(self):
        """Set up test data"""
        self.staff = Staff("TEST_ID", 5)  # 5 hours or days depending on version

    def test_base_wage_only(self):
        """Test wage when no hours/days worked"""
        staff = Staff("ID1", 0)
        self.assertEqual(staff.calculate_wage(), 50)

    def test_wage_calculation(self):
        """Test correct wage calculation"""
        staff = Staff("ID2", 5)
        expected = 50 + (5 * 10)  # Adjust if using daily rate
        self.assertEqual(staff.calculate_wage(), expected)

    def test_negative_hours(self):
        """Test handling of negative input"""
        staff = Staff("ID3", -5)
        self.assertGreaterEqual(staff.calculate_wage(), 50)

    def test_staff_id_assignment(self):
        """Ensure staff ID is assigned correctly"""
        self.assertEqual(self.staff.staff_id, "TEST_ID")

    def test_hours_assignment(self):
        """Ensure hours/days worked is assigned correctly"""
        self.assertEqual(self.staff.hours_worked, 5)

    def test_wage_type(self):
        """Ensure returned wage is numeric"""
        result = self.staff.calculate_wage()
        self.assertIsInstance(result, (int, float))


if __name__ == "__main__":
    unittest.main()
