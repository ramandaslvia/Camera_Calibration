#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from kalibrasi_utils import (
    calibrate_images,
    print_calibration,
    validate_calibration,
)


# Folder tempat file program berada
PROJECT_DIR = Path(__file__).resolve().parent

# Semua foto checkerboard
DEFAULT_IMAGE_PATTERN = str(
    PROJECT_DIR / "folder_papan_baru" / "*.jpg"
)


def parse_args(
    arguments: Sequence[str] | None = None,
) -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description="Calibrate a camera from checkerboard images."
    )

    parser.add_argument(
        "--images",
        default=DEFAULT_IMAGE_PATTERN,
        help="Calibration image glob",
    )

    parser.add_argument(
        "--no-display",
        action="store_true",
        help="Skip the interactive checkerboard preview",
    )

    parser.add_argument(
        "--validate",
        action="store_true",
        help="Check calibration invariants",
    )

    return parser.parse_args(arguments)


def run(options: argparse.Namespace) -> None:

    # Melakukan kalibrasi
    calibration = calibrate_images(
        options.images,
        display=not options.no_display,
    )

    # Menampilkan hasil kalibrasi
    print_calibration(calibration)

    # Validasi jika diminta
    if options.validate:

        validate_calibration(calibration)

        print("Validation passed")


def main(
    arguments: Sequence[str] | None = None,
) -> int:

    try:

        options = parse_args(arguments)

        run(options)

    except Exception as error:

        print(
            f"Error: {error}",
            file=sys.stderr,
        )

        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())