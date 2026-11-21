"""Copy entry.txt to /output/entry.txt, byte for byte.

Reads the poem from this script's own directory so the result does
not depend on the working directory it is run from. Copies raw bytes
so the output is identical to the source, byte for byte.
"""

from pathlib import Path

SOURCE = Path(__file__).parent / "entry.txt"
DESTINATION = Path("/output/entry.txt")


def main() -> None:
    data = SOURCE.read_bytes()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(data)


if __name__ == "__main__":
    main()
