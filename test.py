from typing import Callable

def test(func: Callable, tests: dict) -> None:
    for test_name, values in tests.items():
        assert func(*values["args"], **values["kwargs"]) == values["answer"], f"[!] ERROR - {test_name}"
    else:
        print("[i] ALL TESTS PASSED")