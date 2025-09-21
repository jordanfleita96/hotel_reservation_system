import sys
from pathlib import Path

# Make sure Python can find the src/ folder without installing as a package
root = Path(__file__).resolve().parents[1]
src = root / "src"
if str(src) not in sys.path:
    sys.path.insert(0, str(src))
