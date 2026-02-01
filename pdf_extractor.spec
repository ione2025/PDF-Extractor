# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for PDF Extractor Pro
Builds a standalone Windows executable with all dependencies.
"""

import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Collect all Flask templates and static files
datas = [
    ('templates', 'templates'),
    ('static', 'static'),
]

# Collect data files for dependencies
datas += collect_data_files('google.generativeai')
datas += collect_data_files('google.ai')

# Collect all submodules that might be imported dynamically
hiddenimports = [
    'flask',
    'werkzeug',
    'jinja2',
    'PyPDF2',
    'pdfplumber',
    'fitz',
    'PIL',
    'google.generativeai',
    'openpyxl',
    'pytesseract',
    'pdf2image',
    'reportlab',
    'pypdf',
    'img2pdf',
    'docx',
    'xlsxwriter',
    'cairosvg',
    'flask.json',
    'flask.json.provider',
]

# Analysis - find all the imports
a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# PYZ - archive of Python modules
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# EXE - executable file
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PDF_Extractor_Pro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Show console for server logs
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon='icon.ico' if you have an icon file
)

# COLLECT - collect all files into a folder
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PDF_Extractor_Pro',
)
