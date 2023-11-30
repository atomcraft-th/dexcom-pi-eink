#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
while true
do
	python3 ${SCRIPT_DIR}/dexcom_pi_eink.py
	sleep 30
done