import contextlib
import sys

# Python 2 support.
if sys.version_info < (3,):
    from StringIO import StringIO
else:
    from io import StringIO


@contextlib.contextmanager
def capture_stdout(target=None):
    original = sys.stdout
    if target is None:
        target = StringIO()
    sys.stdout = target
    yield target
    target.seek(0)
    sys.stdout = original


@contextlib.contextmanager
def capture_stderr(target=None):
    original = sys.stderr
    if target is None:
        target = StringIO()
    sys.stderr = target
    yield target
    target.seek(0)
    sys.stderr = original
