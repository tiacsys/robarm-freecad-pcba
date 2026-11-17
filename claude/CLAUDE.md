# robarm-freecad-pcba: rules for agents

Read the workspace `CLAUDE.md` (copied from `xdmod/launch/CLAUDE.md`) first. This file adds the
rules of this repo. Run every command from the workspace root.

## What this repo is

The board library (XD-ADR-0139): FreeCAD models of tagged board versions of robarm-ee, one file per
version and variant in `boards/<board>/<board>-<version>[-<variant>].FCStd`, and one document,
`docs/board-library/`, that lists them. EE writes into it, ME reads from it.

## Rules

- **Only tagged board versions.** A file comes from a tag `<board>/vX.Y.Z` of robarm-ee on `main`,
  made by the owner (XD-ADR-0140). Never add a preview, a `-dirty` export or an untagged commit;
  never create or push a board tag yourself.
- **Files come from curatrix only:** `curatrix cam robarm-ee <board> --library` in a worktree set
  that has this repo on a branch. It exports the STEP with `kicad-cli pcb export step`, imports it
  headless into FreeCAD, sets the Trace properties and saves uncompressed. Never edit a board model
  by hand or in the FreeCAD GUI, and never run FreeCAD or KiCad outside curatrix.
- **Files are never changed or replaced.** A new board version is a new file; older versions stay,
  because assemblies in robarm-me may link them. Removing a version is the owner's call.
- **At most 5 MB per file** (CK-F20). A larger board needs the owner's decision (simpler 3D
  models, fewer components), not a raised limit.
- The EE agent opens the pull request that adds a board version, and names the tag in it. ME
  never writes here.

## Pitfalls

- PR CI has no FreeCAD (D56): CK-F20 reads the files as zip archives in plain Python.
- `.FCStd` files cannot be merged (`-merge` in `.gitattributes`). Two PRs that add the same file
  name are a mistake: one board version, one file.
