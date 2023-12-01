# dexcom-pi-eink
Python to connect dexcom reading to raspberry pi e-ink display

## Running at boot
```
sudo cp systemd/dexcom.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable dexcom.service
sudo systemctl start dexcom.service
```

### to check
`sudo systemctl status dexcom.service`'

