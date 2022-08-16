import os
import sys

# configuring the source path for pytest.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "src")))

from fixtures import *  # noqa