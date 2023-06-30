#!/bin/bash
pwd
cd ~/pythonocc-core/test
python run_tests.py
mypy test_mypy_classic_occ_bottle.py
