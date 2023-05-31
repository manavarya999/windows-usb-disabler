# Windows-USB-Disabler
A python script for disabling USB ports in your Windows machine. This tool uses Microsoft's `Pnputil` which is a command line utility that you can use to manage the driver store.

## NOTE: 
Disconnect all your devices physically connected to your USB ports before running this script.

## Usage

1. Run the `Command prompt` or `Powershell` as an administrator in your Windows machine.

2. Clone the repository: 

    ```bash
      git clone https://github.com/manavarya999/win-usb-disabler.git
    ```

3. Head over to the directory: 

    ```bash
    cd win-usb-disabler
    ``` 
4. Run the python script:

    ```bash
    python win-usb-disabler.py
    ```
5. Restart your system to see the changes in effect.
