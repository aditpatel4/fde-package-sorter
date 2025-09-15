"""
FDE Technical Screen – Package sorter
Language: Python 3.11+

Implements `sort(width, height, length, mass)` per spec:
- Bulky if volume >= 1_000_000 cm^3 OR any dimension >= 150 cm
- Heavy if mass >= 20 kg
Dispatch:
- "REJECTED" if both heavy and bulky
- "SPECIAL"  if exactly one of heavy or bulky
- "STANDARD" if neither
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Decision = Literal["STANDARD", "SPECIAL", "REJECTED"]


def sort(width: float, height: float, length: float, mass: float) -> Decision:
    """
    Decide the dispatch stack for a package.

    Args:
        width:  width in cm
        height: height in cm
        length: length in cm
        mass:   mass in kg

    Returns:
        One of "STANDARD", "SPECIAL", or "REJECTED".

    Raises:
        ValueError: if any input is negative or NaN.
    """
    for name, v in (("width", width), ("height", height), ("length", length), ("mass", mass)):
        if v is None or (isinstance(v, (int, float)) and v != v) or v < 0:
            raise ValueError(f"Invalid {name}: {v!r}")

    volume = width * height * length
    bulky = (width >= 150) or (height >= 150) or (length >= 150) or (volume >= 1_000_000)
    heavy = mass >= 20

    # At least one required ternary operator per instructions:
    return "REJECTED" if (bulky and heavy) else ("SPECIAL" if (bulky or heavy) else "STANDARD")


def _cli() -> None:
    import argparse, sys, json

    p = argparse.ArgumentParser(description="Package sorter per FDE spec")
    p.add_argument("--width", type=float, required=True, help="cm")
    p.add_argument("--height", type=float, required=True, help="cm")
    p.add_argument("--length", type=float, required=True, help="cm")
    p.add_argument("--mass", type=float, required=True, help="kg")
    args = p.parse_args()

    decision = sort(args.width, args.height, args.length, args.mass)
    print(decision)


if __name__ == "__main__":
    _cli()
