"""Core Runtime Type Contract Enforcer."""
import functools
import inspect
from typing import get_type_hints, Any

class TypeContractError(TypeError):
    pass

def enforce_contracts(func):
    hints = get_type_hints(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        for param_name, value in bound.arguments.items():
            if param_name in hints:
                expected = hints[param_name]
                if expected is not Any and not isinstance(value, expected):
                    raise TypeContractError(
                        f"Argument '{param_name}' must be {expected.__name__}, got {type(value).__name__} ({value!r})"
                    )

        result = func(*args, **kwargs)

        if "return" in hints:
            expected_ret = hints["return"]
            if expected_ret is not Any and not isinstance(result, expected_ret):
                raise TypeContractError(
                    f"Return value of {func.__name__} must be {expected_ret.__name__}, got {type(result).__name__} ({result!r})"
                )

        return result

    return wrapper
