# robarm-freecad-pcba

The board library of the robot arm example of [XDMOD](https://github.com/tiacsys/xdmod): FreeCAD
models of the tagged board versions of [robarm-ee](https://github.com/tiacsys/robarm-ee), for the
assemblies of [robarm-me](https://github.com/tiacsys/robarm-me) (XD-ADR-0139).

Status: **skeleton** (Phase 5, task 5.29). No board version has been tagged yet.

## Layout

| Path | What |
|---|---|
| `boards/<board>/<board>-<version>[-<variant>].FCStd` | one FreeCAD model per tagged board version and variant: board body, components, no tracks; Trace properties `TraceID` (the `EE-PCBA` ID), `Version`, `Variant`, `Commit`; saved uncompressed; at most 5 MB |
| `docs/board-library/` | the document that lists the board versions (made from the files at build time) |
| `checks.yaml` | what `curatrix check robarm-freecad-pcba` runs |
| `claude/` | rules for agents working in this repo |

## Use

This repo is a west project of the [robarm-manifest](https://github.com/tiacsys/robarm-manifest)
workspace (west groups `ee` and `me`). Run every command from the workspace root:

```sh
curatrix cam robarm-ee <board> --library        # EE: write a tagged board version into a worktree of this repo
curatrix check robarm-freecad-pcba --stage local # all checks, as before a push
```

Only the owner tags board versions (`<board>/vX.Y.Z` in robarm-ee, XD-ADR-0140). The EE agent opens
the pull request that adds a version. ME links one fixed version; when a newer one exists, the
robarm-me check reports it, and moving to it is an ME change.

## Licence

Apache-2.0, see `LICENSE`.
