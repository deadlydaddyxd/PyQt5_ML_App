# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[], datas=[('accuracy.png','.'),('c.png','.'),('cc.jpg','.'),('cc.png','.'),('chloride1.png','.'),('cl.png','.'),('close.png','.'),('concrete.png','.'),('concrete256x256.png','.'),('data_model.png','.'),('design.ui','.'),('email.png','.'),('graph.png','.'),('histogram.png','.'),('info.png','.'),('MaterialDark.qss','.'),('matrix.png','.'),('maximize.png','.'),('minimize.png','.'),('NAC Strength Prediction.pkl','.'),('phone.png','.'),('question.png','.'),('RAC Carbonization Prediction.pkl','.'),('RAC Chloride Ion Prediction.pkl','.'),('RAC Strength Prediction.pkl','.'),('RAC Sulfate Corrosion Prediction.pkl','.'),('sf_pic.png','.'),('splashscreen.ui','.'),('SplashScreen_actual.png','.'),('transform_X_carbonization.pkl','.'),('transform_X_chloride.pkl','.'),('transform_X_cs.pkl','.'),('transform_X_detailed.joblib','.'),('transform_X_detailed.pkl','.'),('transform_X_sulfate.pkl','.'),('graphs_data','graphs_data')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Concrete SureCast',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='concrete256x256.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SureCast',
)
