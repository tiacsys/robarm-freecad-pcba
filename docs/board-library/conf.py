# Sphinx configuration of the document "Board Library" (board-library).
# The shared XDMOD setup (xdmod/sphinx/xdmod_conf.py) wraps zdocs' configure().
# The table of board versions is made at build time from the files in boards/ (their name and
# the Trace properties in Document.xml), so it cannot drift from the files; nothing is written
# into the repo.
import html
import os
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(os.environ["ZDOCS_WEST_TOPDIR"]) / "xdmod" / "sphinx"))
from xdmod_conf import configure, repo_root  # noqa: E402

REPO = repo_root(__file__)
configure(globals(), __file__, "Board Library")

MARKER = ".. board-versions::"
PROP = re.compile(r'<Property name="(TraceID|Version|Variant|Commit)"[^>]*>\s*<String value="([^"]*)"')


def _props(fc: Path) -> dict:
    try:
        with zipfile.ZipFile(fc) as z:
            xml = z.read("Document.xml").decode("utf-8", "replace")
    except (OSError, KeyError, zipfile.BadZipFile):
        return {}
    out = {}
    for k, v in PROP.findall(xml):
        out.setdefault(k, html.unescape(v))
    return out


def board_table() -> str:
    files = sorted((REPO / "boards").glob("*/*.FCStd"))
    if not files:
        return "The library holds no board version yet.\n"
    rows = [".. list-table::", "   :header-rows: 1", "",
            "   * - Board", "     - Version", "     - Variant", "     - EE-PCBA", "     - File", "     - Size"]
    for fc in files:
        p = _props(fc)
        rows += [f"   * - {fc.parent.name}", f"     - {p.get('Version') or '?'}", f"     - {p.get('Variant') or '-'}",
                 f"     - {p.get('TraceID') or '?'}", f"     - ``boards/{fc.parent.name}/{fc.name}``",
                 f"     - {fc.stat().st_size / 1e6:.2f} MB"]
    return "\n".join(rows) + "\n"


def _source_read(app, docname, source):
    if MARKER in source[0]:
        source[0] = source[0].replace(MARKER, board_table())


def setup(app):
    app.connect("source-read", _source_read)
