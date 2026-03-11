# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

python_root = Path(sys.base_prefix)
dll_dir = python_root / "DLLs"

tk_binaries = []
for dll_name in ("_tkinter.pyd", "tcl86t.dll", "tk86t.dll"):
    dll_path = dll_dir / dll_name
    if dll_path.exists():
        tk_binaries.append((str(dll_path), "."))

tk_datas = []
for source_rel, target_rel in (
    ("tcl/tcl8.6", "_tcl_data"),
    ("tcl/tk8.6", "_tk_data"),
):
    source_path = python_root / source_rel
    if source_path.exists():
        tk_datas.append((str(source_path), target_rel))

project_datas = [
    ("README.md", "."),
    ("docs/QUICKSTART_ONE_PAGE.md", "docs"),
    ("assets/logo.png", "assets"),
    ("assets/sbs_dsw_icon.ico", "assets"),
]

a = Analysis(
    ['sbs_dsw.py'],
    pathex=[],
    binaries=tk_binaries,
    datas=project_datas + tk_datas,
    hiddenimports=[],
    hookspath=['tools/pyi_hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='sbs_dsw',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
