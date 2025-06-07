import json
import os
import unittest

class TestMilestoneTotals(unittest.TestCase):
    def test_totals_match(self):
        root = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(root, 'milestones.json')
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for contract in data.get('contracts', []):
            with self.subTest(contract=contract.get('name')):
                total = contract.get('total', 0)
                sum_amounts = sum(m.get('amount', 0) for m in contract.get('milestones', []))
                # Use tolerance for floating point arithmetic
                self.assertAlmostEqual(sum_amounts, total, places=2)

if __name__ == '__main__':
    unittest.main()
