# boards/

One folder per board of robarm-ee (the KiCad project name), with one FreeCAD model per tagged
board version and variant:

```
boards/<board>/<board>-<version>[-<variant>].FCStd
```

The files are written by `curatrix cam robarm-ee <board> --library`, never by hand, and never
changed afterwards: a new board version is a new file. See `docs/board-library/` and XD-ADR-0139.
