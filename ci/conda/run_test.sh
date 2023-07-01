echo 'Test start!!!'
pwd
tree
mypy test/test_mypy_classic_occ_bottle.py
if [[ "$OSTYPE" != "darwin"* ]]; then
    python test/core_display_pyqt5_unittest.py
    python test/core_display_pyside2_unittest.py
    python test/core_display_wx_unittest.py
fi