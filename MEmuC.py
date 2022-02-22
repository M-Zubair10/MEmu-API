import os


class Memu:
    def __init__(self, path):
        self.index = None
        self.name = None
        os.chdir(path)

        # VM Management
        self.Create = "memuc create"
        self.Remove = 'memuc remove'
        self.Clone = 'memuc clone'
        self.export = 'memuc export'
        self.Import = 'memuc import'
        self.Start = 'memuc start'
        self.Stop = 'memuc stop'
        self.StopAll = 'memuc stopall'
        self.Info = 'memuc listvms'
        self.IsRunning = 'memuc isvmrunning'
        self.Rename = 'memuc rename'
        self.Sort = 'memuc sortwin'
        self.Reboot = 'memuc reboot'
        self.Status = 'memuc taskstatus'

        # VM Configuration
        self.GetConfig = 'memuc getconfigex'
        self.SetConfig = 'memuc setconfigex'

        # VM Control
        self.Install = 'memuc installapp'
        self.Uninstall = 'memuc uninstallapp'
        self.StartApp = 'memuc startapp'
        self.StopApp = 'memuc stopapp'
        self.Keystrokes = 'memuc sendkey'
        self.Shake = 'memuc shake'
        self.Connect = 'memuc connect'
        self.Disconnect = 'memuc disconnect'
        self.Input = 'memuc input'
        self.IP = 'memuc'
        self.Exec = 'memuc'
        self.ZoomIn = 'memuc zoomin'
        self.ZoomOut = 'memuc zoomout'
        self.AppInfo = 'memuc getappinfolist'
        self.Acceleration = 'memuc accelerometer'
        self.Shortcut = 'memuc createshortcut'
        self.Rotate = 'memuc rotate'
        self.GPS = 'memuc setgps'

        # ADB command
        self.ADB = 'memuc'

    # VM Management
    def create(self, version=71):
        os.system(self.Create + ' ' + str(version))
        return self

    def remove(self, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f"{self.Remove} -i {index}") if index is not None else os.system(f"{self.Remove} -n {name}")
        return self

    def clone(self, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f"{self.Clone} -i {index}") if index is not None else os.system(f"{self.Clone} -n {name}")
        return self

    def backup(self, path, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f"{self.export} -i {index} {path}") if index is not None else os.system(
            f"{self.export} -n {name} {path}")
        return self

    def restore(self, ova):
        os.system(self.Import + ' ' + ova)
        return self

    def start(self, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f"{self.Start} -i {index}") if index is not None else os.system(
            f"{self.Start} -n {name}")
        self.index = index
        self.name = name
        return self

    def stop(self, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f"{self.Stop} -i {index}") if index is not None else os.system(
            f"{self.Stop} -n {name}")
        return self

    def stopAll(self):
        os.system(self.StopAll)
        return self

    def listInfo(self):
        os.system(self.Info)
        return self

    def sort(self):
        os.system(self.Sort)
        return self

    def is_running(self, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f"{self.IsRunning} -i {index}") if index is not None else os.system(
            f"{self.IsRunning} -n {name}")
        return self

    def reboot(self, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f"{self.Reboot} -i {index}") if index is not None else os.system(
            f"{self.Reboot} -n {name}")
        return self

    def status(self, ID):
        os.system(f"{self.Status} {ID}")
        return self

    def rename(self, new_name, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f'{self.Rename} -i {index} "{new_name}"') if index is not None else os.system(
            f'{self.Rename} -n {name} "{new_name}"')
        return self

    # VM Config
    def getConfig(self, key, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f'{self.GetConfig} -i {index} {key}') if index is not None else os.system(
            f'{self.GetConfig} -n {name} {key}')
        return self

    def setConfig(self, key, value, index=None, name=None):
        assert index is not None or name is not None, 'Provide at least name or index'
        os.system(f'{self.SetConfig} -i {index} {key} {value}') if index is not None else os.system(
            f'{self.SetConfig} -n {name} {key} {value}')
        return self

    # VM Start Events
    def install(self, apk):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Install} -i {index} {apk}') if index is not None else os.system(
            f'{self.Install} -n {name} {apk}')
        return self

    def uninstall(self, pkg_name):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Uninstall} -i {index} {pkg_name}') if index is not None else os.system(
            f'{self.Uninstall} -n {name} {pkg_name}')
        return self

    def startApp(self, pkg_activity):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.StartApp} -i {index} {pkg_activity}') if index is not None else os.system(
            f'{self.StartApp} -n {name} {pkg_activity}')
        return self

    def send_keys(self, key):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Keystrokes} -i {index} {key}') if index is not None else os.system(
            f'{self.Keystrokes} -n {name} {key}')
        return self

    def shake(self):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Shake} -i {index}') if index is not None else os.system(
            f'{self.Shake} -n {name}')
        return self

    def connect(self):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Connect} -i {index}') if index is not None else os.system(
            f'{self.Connect} -n {name}')
        return self

    def disconnect(self):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Disconnect} -i {index}') if index is not None else os.system(
            f'{self.Disconnect} -n {name}')
        return self

    def input(self, text):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Input} -i {index} "{text}"') if index is not None else os.system(
            f'{self.Input} -n {name} "{text}"')
        return self

    def rotate(self):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Rotate} -i {index}') if index is not None else os.system(
            f'{self.Rotate} -n {name}')
        return self

    def exec_command(self, command):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Exec} -i {index} execcmd "{command}"') if index is not None else os.system(
            f'{self.Exec} -n {name} execcmd "{command}"')
        return self

    def changeGPS(self, latitude, longitude):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.GPS} -i {index} {latitude}') if index is not None else os.system(
            f'{self.GPS} -n {name} {longitude}')
        return self

    def getIP(self):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.IP} -i {index} execcmd “wget -O- whatismyip.akamai.com”') if index is not None else os.system(
            f'{self.IP} -n {name} execcmd “wget -O- whatismyip.akamai.com”')
        return self

    def zoomIn(self):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.ZoomIn} -i {index}') if index is not None else os.system(
            f'{self.ZoomIn} -n {name}')
        return self

    def zoomOut(self):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.ZoomOut} -i {index}') if index is not None else os.system(
            f'{self.ZoomOut} -n {name}')
        return self

    def appsInfo(self):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.AppInfo} -i {index}') if index is not None else os.system(
            f'{self.AppInfo} -n {name}')
        return self

    def acceleration(self, x_value, y_value, z_value):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(
            f'{self.Acceleration} -i {index} -x {x_value} -y {y_value} -z {z_value}') if index is not None else os.system(
            f'{self.Acceleration} -n {name} -x {x_value} -y {y_value} -z {z_value}')
        return self

    def createShortcut(self, pkg_name):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.Shortcut} -i {index} {pkg_name}') if index is not None else os.system(
            f'{self.Shortcut} -n {name} {pkg_name}')
        return self

    def adb(self, command):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.ADB} -i {index} adb "{command}"') if index is not None else os.system(
            f'{self.ADB} -n {name} adb "{command}"')
        return self

    def stopApp(self, pkg_name):
        index, name = self.index, self.name
        assert index is not None or name is not None, "Looks like you MEmu haven't start yet"
        os.system(f'{self.StopApp} -i {index} {pkg_name}') if index is not None else os.system(
            f'{self.StopApp} -n {name} {pkg_name}')
        return self
