import subprocess

# The below command gives the list of USB devices
command = 'pnputil /enum-devices /class "USB" '
output = subprocess.check_output(command, shell=True, encoding='utf-8')


# Finding the device IDs of only USB Root Hubs
device_id = None
count = 0

for line in output.splitlines():
    if "USB\ROOT_HUB" in line:
        device_id = line.split(":")[-1].strip()
        print("USB Root Hub Device Detected!! : " + device_id)
        
# Disabling the detected USB Root Hub devices   
        command = f'pnputil /disable-device "{device_id}"'
        subprocess.run(command, shell=True)
        print("USB Root Hub disabled successfully.")
        print("\n")
        count += 1

if count < 1:
    print("USB Root Hub not found")