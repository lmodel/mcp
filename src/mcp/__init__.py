"""mcp.

Model Context Protocol (MCP) 2026-07-28 (LinkML)
"""

try:
    from mcp._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
