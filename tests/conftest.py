"""Lets a test import tests/mcp_parity.py by name."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
