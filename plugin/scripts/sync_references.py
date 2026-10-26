#!/usr/bin/env python3
"""ルートの原本をプラグインに同梱する。--check は変更せず同期状態を確認する。"""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="差分があれば終了コード1")
    args = parser.parse_args()

    plugin = Path(__file__).resolve().parents[1]
    repository = plugin.parent
    references = plugin / "skills" / "mountaineering-plan" / "references"
    names = ("project-instructions.md", "mountaineering-plan.md")

    # 全原本を先に読む。インストール済みコピーなどで原本がない場合は書き込まない。
    try:
        originals = {name: (repository / name).read_bytes() for name in names}
    except OSError as error:
        parser.exit(2, f"原本を読み込めません。リポジトリ内で実行してください: {error}\n")

    stale = []
    for name, content in originals.items():
        destination = references / name
        if destination.is_file() and destination.read_bytes() == content:
            continue
        if args.check:
            stale.append(name)
        else:
            references.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
            print(f"同期: {name}")

    if stale:
        parser.exit(1, "未同期: " + ", ".join(stale) + "\n")
    print("同梱資料は原本と一致しています。")


if __name__ == "__main__":
    main()
