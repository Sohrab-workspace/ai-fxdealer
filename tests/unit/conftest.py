"""
Conftest for unit tests.

Handles module isolation between test files that both import `collector`
from different service directories (collector-mt4 and collector-mt5).
"""

import sys
import importlib
import pytest
from pathlib import Path

_REPO = Path(__file__).parent.parent.parent
_MT4_SVC = str(_REPO / "services" / "collector-mt4")
_MT5_SVC = str(_REPO / "services" / "collector-mt5")
_PACKAGES = str(_REPO / "packages")


@pytest.fixture(autouse=True)
def isolate_collector_module(request):
    """
    Before each test, ensure sys.modules["collector"] corresponds to the
    service being tested by clearing the cached module and setting the
    correct service directory first in sys.path.

    This prevents cross-contamination when both test_mt4_collector.py and
    test_mt5_collector.py run in the same pytest session.
    """
    # Determine which service this test belongs to
    test_file = request.fspath.basename
    if "mt4" in test_file:
        target_svc = _MT4_SVC
        other_svc = _MT5_SVC
    elif "mt5" in test_file:
        target_svc = _MT5_SVC
        other_svc = _MT4_SVC
    else:
        yield
        return

    # Remove the cached collector module (and ctypes_wrapper for MT4)
    for mod in ("collector", "ctypes_wrapper"):
        sys.modules.pop(mod, None)

    # Ensure packages dir is in path
    if _PACKAGES not in sys.path:
        sys.path.insert(0, _PACKAGES)

    # Remove other service dir from path to prevent wrong collector loading
    if other_svc in sys.path:
        sys.path.remove(other_svc)

    # Put target service dir first
    if target_svc in sys.path:
        sys.path.remove(target_svc)
    sys.path.insert(0, target_svc)

    yield

    # Cleanup: remove stale cached modules after test
    for mod in ("collector", "ctypes_wrapper"):
        sys.modules.pop(mod, None)
