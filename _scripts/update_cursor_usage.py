#!/usr/bin/env python3
"""CURSOR.md usage: Cursor 채팅창에 `@orchestrator` 으로 요청."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def orchestrator_name(cursor_md: Path) -> str:
    harness = cursor_md.parents[1].name
    m = re.match(r"^\d+-(.+)$", harness)
    return m.group(1) if m else harness


def ko_usage(skill: str) -> str:
    return f"Cursor 채팅창에 `@{skill}`으로 요청한다."


def en_usage(skill: str) -> str:
    return f"In Cursor chat, request with `@{skill}`."


OLD_KO = re.compile(
    r"Cursor 채팅에서 `@\.cursor/skills/[^`]+/skill\.md`를 첨부한 뒤 요청한다\."
)
OLD_EN = re.compile(
    r"Attach `@\.cursor/skills/[^`]+/skill\.md` in Cursor chat, then send your request\."
)
OLD_KO2 = re.compile(r"Cursor 채팅창에 @\S+으로 요청한다\.")
OLD_EN2 = re.compile(r"In Cursor chat, request with @\S+\.")
OLD_MISC_KO = re.compile(
    r"자연어, `/[^`]+`, 또는 `@\.cursor/skills/[^`]+/skill\.md`.*"
)
OLD_MISC_EN = re.compile(
    r"Natural language, `/[^`]+`, or `@\.cursor/skills/[^`]+/skill\.md`.*"
)
OLD_SLASH_EN = re.compile(r"`/[^`]+` skill.*")


def main() -> None:
    n = 0
    for path in sorted(ROOT.glob("**/CURSOR.md")):
        if ".cursor" not in path.parts:
            continue
        is_ko = "ko" in path.parts
        skill = orchestrator_name(path)
        text = path.read_text(encoding="utf-8")
        orig = text

        repl = ko_usage(skill) if is_ko else en_usage(skill)
        for pat in (OLD_KO, OLD_KO2, OLD_MISC_KO) if is_ko else (
            OLD_EN,
            OLD_EN2,
            OLD_MISC_EN,
            OLD_SLASH_EN,
        ):
            text = pat.sub(repl, text)

        # blank line before next ## after usage line
        text = re.sub(
            r"(Cursor 채팅창에 `@[^`]+`으로 요청한다\.|In Cursor chat, request with `@[^`]+`\.)\n(## )",
            r"\1\n\n\2",
            text,
        )

        if text != orig:
            path.write_text(text, encoding="utf-8")
            n += 1
    print(f"Updated {n} files")


if __name__ == "__main__":
    main()
