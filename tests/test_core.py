"""Tests for Type Contract Enforcer."""
import unittest
from runtime_type_contract_enforcer.core import enforce_contracts, TypeContractError

class TestRuntimeTypeContractEnforcer(unittest.TestCase):
    def test_enforces_parameter_types(self):
        @enforce_contracts
        def add(x: int, y: int) -> int:
            return x + y

        self.assertEqual(add(2, 3), 5)
        with self.assertRaises(TypeContractError):
            add("2", 3)
