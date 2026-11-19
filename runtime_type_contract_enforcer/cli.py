"""CLI for Type Contract Enforcer."""
import argparse
from .core import enforce_contracts, TypeContractError

def main():
    parser = argparse.ArgumentParser(description="Runtime Type Contract Enforcer CLI")
    parser.add_argument("--demo", action="store_true", help="Run contract enforcer demo")
    args = parser.parse_args()

    @enforce_contracts
    def calculate_tax(amount: float, rate: float) -> float:
        return amount * rate

    valid = calculate_tax(100.0, 0.05)
    print(f"Valid call returned: {valid}")

    try:
        calculate_tax("invalid_amount", 0.05)
    except TypeContractError as e:
        print(f"Caught expected type error: {e}")

if __name__ == "__main__":
    main()
