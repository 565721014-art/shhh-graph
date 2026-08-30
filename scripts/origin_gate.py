"""Verify and, when requested, prepare a live OriginPro automation session."""

from __future__ import annotations

import argparse
import importlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def candidate_executables() -> list[Path]:
    candidates: list[Path] = []
    for drive in ("C:", "D:", "E:"):
        root = Path(drive + os.sep)
        for pattern in (
            "OriginLab/Origin*/Origin64.exe",
            "Program Files/OriginLab/Origin*/Origin64.exe",
            "Program Files/OriginLab/Origin*/Origin.exe",
        ):
            candidates.extend(root.glob(pattern))
    return sorted({path.resolve() for path in candidates if path.is_file()})


def ensure_originpro() -> object:
    try:
        return importlib.import_module("originpro")
    except ModuleNotFoundError:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "originpro>=1.1.15"],
            check=True,
        )
        return importlib.import_module("originpro")


def connect(show: bool, ensure_package: bool) -> dict[str, object]:
    if platform.system() != "Windows":
        raise RuntimeError("OriginPro COM automation requires Windows.")

    executables = candidate_executables()
    try:
        op = importlib.import_module("originpro")
    except ModuleNotFoundError as exc:
        if not ensure_package:
            raise RuntimeError(
                "The originpro package is missing. Re-run with --ensure-package."
            ) from exc
        op = ensure_originpro()

    if show:
        op.set_show(True)
    op.attach()
    version = float(op.lt_float("system.version"))
    # A harmless LabTalk expression proves that the automation channel is live.
    handshake_value = float(op.lt_float("1+1"))
    handshake = handshake_value == 2.0
    if not handshake or version <= 0:
        raise RuntimeError("Origin attached but the LabTalk handshake failed.")

    return {
        "connected": True,
        "origin_version": version,
        "labtalk_handshake": handshake,
        "originpro_package": getattr(op, "__version__", "unknown"),
        "detected_executables": [str(path) for path in executables],
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.executable,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Mandatory Shhh Graph OriginPro connection gate.")
    parser.add_argument("--show", action="store_true", help="Make the attached Origin session visible.")
    parser.add_argument("--ensure-package", action="store_true", help="Install originpro if missing.")
    parser.add_argument("--json-out", type=Path, help="Optional path for a machine-readable gate receipt.")
    args = parser.parse_args()

    try:
        result = connect(args.show, args.ensure_package)
    except Exception as exc:
        result = {"connected": False, "error": str(exc)}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 2

    payload = json.dumps(result, ensure_ascii=False, indent=2)
    print(payload)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(payload + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
