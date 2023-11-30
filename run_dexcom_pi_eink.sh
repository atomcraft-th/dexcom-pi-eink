#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
export PYTHON_PATH=${PYTHON_PATH}:${SCRIPT_DIR}
while true
do
	python3 ${SCRIPT_DIR}/dexcom_pi_eink.py
	sleep 30
done