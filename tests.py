import unittest
import main

class TestResourceAllocation(unittest.TestCase):
    
    def test_case_1(self):
        output = main.ResourceAllocator().start_process(total_units=1150, hours=1)
        self.assertEqual(output, {'Output': [{'region': 'New York', 'total_cost': '$10150', 'machines': [('Large', 1), ('XLarge', 1), ('8XLarge', 7)]}, {'region': 'India', 'total_cost': '$9520', 'machines': [('Large', 3), ('8XLarge', 7)]}, {'region': 'China', 'total_cost': '$8570', 'machines': [('Large', 1), ('XLarge', 1), ('8XLarge', 7)]}]})

    def test_case_2(self):
        output = main.ResourceAllocator().start_process(total_units=230, hours=5)
        self.assertEqual(output, {'Output': [{'region': 'New York', 'total_cost': '$11000', 'machines': [('Large', 1), ('XLarge', 1), ('2XLarge', 1), ('8XLarge', 1)]}, {'region': 'India', 'total_cost': '$10665', 'machines': [('Large', 3), ('2XLarge', 1), ('8XLarge', 1)]}, {'region': 'China', 'total_cost': '$9450', 'machines': [('Large', 1), ('XLarge', 3), ('8XLarge', 1)]}]})

    def test_case_3(self):
        output = main.ResourceAllocator().start_process(total_units=100, hours=24)
        self.assertEqual(output, 
        {'Output': [{'region': 'New York', 'total_cost': '$24096', 'machines': [('XLarge', 1), ('4XLarge', 1)]}, {'region': 'India', 'total_cost': '$26544', 'machines': [('Large', 2), ('2XLarge', 2)]}, {'region': 'China', 'total_cost': '$20880', 'machines': [('XLarge', 1), ('4XLarge', 1)]}]})

    def test_case_4(self):
        output = main.ResourceAllocator().start_process(total_units=1100, hours=12)
        self.assertEqual(output, 
        {'Output': [{'region': 'New York', 'total_cost': '$118248', 'machines': [('XLarge', 1), ('2XLarge', 1), ('4XLarge', 1), ('8XLarge', 6)]}, {'region': 'India', 'total_cost': '$111828', 'machines': [('Large', 2), ('2XLarge', 3), ('8XLarge', 6)]}, {'region': 'China', 'total_cost': '$100200', 'machines': [('XLarge', 3), ('4XLarge', 1), ('8XLarge', 6)]}]})

    def test_case_zero(self):
        output = main.ResourceAllocator().start_process(total_units=0, hours=0)
        self.assertEqual(output, {'Output': [{'region': 'New York', 'total_cost': '$0', 'machines': []}, {'region': 'India', 'total_cost': '$0', 'machines': []}, {'region': 'China', 'total_cost': '$0', 'machines': []}]})

if __name__ == "__main__":
    unittest.main()