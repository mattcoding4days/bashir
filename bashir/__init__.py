"""
Root level package init
"""

import pkg_resources
__version__ = pkg_resources.require("bashir")[0].version
