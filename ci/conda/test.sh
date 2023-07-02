echo 'Test start!!!'
pwd
tree
mypy test/test_mypy_classic_occ_bottle.py

# Ubuntu: Unable to access the X Display, is $DISPLAY set properly?
# Mac: RuntimeError: Aspect_GraphicDeviceDefinitionErrorOpenGl_Window::CreateWindow: NSOpenGLContext creation failed raised from method Init of class Display3d
if [[ "$OSTYPE" != "darwin"* ] && [ "$OSTYPE" != "linux-gnu"* ]]; then
    python test/core_display_pyqt5_unittest.py
    python test/core_display_pyside2_unittest.py
    python test/core_display_wx_unittest.py
fi