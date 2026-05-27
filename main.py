from __future__ import annotations

import argparse
import json

from models import Config
from exporter import export_xlsx


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="AdGrid Generator (Meta Ads)")
    p.add_argument("--config", required=True, help="Path to JSON config")
    p.add_argument("--out", required=True, help="Output .xlsx path")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    with open(args.config, "r", encoding="utf-8") as f:
        raw = json.load(f)
    cfg = Config.model_validate(raw)
    export_xlsx(cfg, args.out)
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
