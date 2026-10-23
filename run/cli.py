import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(
        description="Запуск Kedro pipeline для обучения модели."
    )

    parser.add_argument(
        "--pipeline",
        default="modeling",
        help="Название pipeline. По умолчанию: modeling.",
    )
    parser.add_argument("--alpha", type=float, default=None)
    parser.add_argument("--l1-ratio", type=float, default=None)
    parser.add_argument("--max-iter", type=int, default=None)

    args = parser.parse_args()

    if args.alpha is not None and args.alpha < 0:
        parser.error("--alpha должен быть >= 0")

    if args.l1_ratio is not None and not 0 <= args.l1_ratio <= 1:
        parser.error("--l1-ratio должен быть от 0 до 1")

    if args.max_iter is not None and args.max_iter <= 0:
        parser.error("--max-iter должен быть > 0")

    overrides = {
        "model_options.alpha": args.alpha,
        "model_options.l1_ratio": args.l1_ratio,
        "model_options.max_iter": args.max_iter,
    }

    params = [
        f"{name}={value}"
        for name, value in overrides.items()
        if value is not None
    ]

    command = [
        sys.executable,
        "-m",
        "kedro",
        "run",
        "--pipeline",
        args.pipeline,
    ]

    if params:
        command.extend(["--params", ",".join(params)])

    result = subprocess.run( # noqa: S603
        command,
        cwd=PROJECT_ROOT,
        check=False,
    )

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
