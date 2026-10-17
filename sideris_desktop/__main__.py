"""Entry point for ``python -m sideris_desktop`` and the packaged app.

No arguments opens the desktop window.  Anything else is treated as a
CLI command, so ``Sideris.exe chat`` and ``python -m sideris_desktop
status`` behave the same way.
"""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    # Make pip-installed extras (llama.cpp / training wheels) importable
    # before anything tries to use them.
    try:
        from .installer import activate_runtime

        activate_runtime()
    except Exception:
        pass

    if args == ["--smoke"]:
        from .app import run_gui

        return run_gui(smoke=True)

    if not args:
        from .app import run_gui

        return run_gui()

    from .cli import main as cli_main

    return cli_main(args)


if __name__ == "__main__":
    raise SystemExit(main())
