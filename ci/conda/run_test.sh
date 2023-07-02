#!/bin/bash
# Ubuntu: Unable to access the X Display, is $DISPLAY set properly?
# Mac: RuntimeError: Aspect_GraphicDeviceDefinitionErrorOpenGl_Window::CreateWindow: NSOpenGLContext creation failed raised from method Init of class Display3d

echo 'Test start!!!'
pwd
tree
# python run_tests.py
mypy test/test_mypy_classic_occ_bottle.py
