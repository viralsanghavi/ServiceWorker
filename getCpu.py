import wmi
import os
import win32serviceutil


list = ["AvastSecureBrowserElevationService"]


def main():
    c = wmi.WMI()

    for name in list:
        stop = c.Win32_Service(Name=name, State="Stopped")
        if stop != []:
            for service in c.Win32_Service(Name=name):
                service.ChangeStartMode(StartMode="Automatic")
                win32serviceutil.StartService(name)
                print(name + ' Started')
        else:
            print(name + "  Already Running")


main()
