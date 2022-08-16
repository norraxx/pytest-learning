import os
import sys

# configuring the source path for pytest.
sys.path.insert(
    0,  # push the library on first position, that python would find it earlier
    os.path.abspath(  # real path to the current file
        os.path.join(
            os.path.dirname(os.path.realpath(__file__))
        )
    )
)  # there is a mistake, can u find it?

