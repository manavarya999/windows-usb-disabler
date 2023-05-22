# Windows-USB-Disabler
A python script for disabling USB ports in your Windows machine. This tool uses Microsoft's `Pnputil` which is a command line utility that you can use to manage the driver store.

## NOTE: 
Disconnect all your devices physically connected to your USB ports before running this script.

## Usage

- Run the `Command prompt` or `Powershell` as an administrator in your Windows machine.

- Clone the repository: 

  ```bash
    git clone https://github.com/manavarya999/win-usb-disabler.git
  ```

- Head over to the directory: 

  ```bash
  cd win-usb-disabler
  ``` 
- Run the python script:

  ```bash
  python win-usb-disabler.py
  ```
- Restart your system incase you didn't see the changes.
