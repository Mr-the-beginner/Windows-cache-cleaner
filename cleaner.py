import os
import shutil
import glob
import time

def get_disk_space(path):
    """Returns the free space on the given path in bytes"""
    total, used, free = shutil.disk_usage(path)
    return free

def delete_files(pattern):
    """Deletes files matching the given pattern"""
    expanded_pattern = os.path.expandvars(pattern)
    print(f"Deleting files matching pattern: {expanded_pattern}")
    files = glob.glob(expanded_pattern, recursive=True)
    for file in files:
        try:
            if os.path.isdir(file):
                shutil.rmtree(file)
            else:
                os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

def bytes_to_mb(n):
    return round(n / 1024 / 1024, 2)

def main():
    before = get_disk_space("C:/")
    print(f"Disk space before cleanup: {bytes_to_mb(before)} MB")

    patterns_to_delete = [

         # --- Windows Temp and Logs ---
        "C:/Windows/Temp/*",
        "%TEMP%/*",
        "%SystemRoot%/Prefetch/*",
        "%SystemRoot%/Memory.dmp",
        "%SystemRoot%/Minidump/*.dmp",
        "%SystemRoot%/SoftwareDistribution/Download/*",
        "%SystemRoot%/SoftwareDistribution/*",
        "%SystemRoot%/Installer/$PatchCache$/*",
        "%SystemRoot%/Installer/*",

        # --- Error Reports and Crash Dumps ---
        "%ALLUSERSPROFILE%/Microsoft/Windows/WER/ReportQueue/*",
        "%LOCALAPPDATA%/Microsoft/Windows/WER/ReportQueue/*",
        "%LOCALAPPDATA%/CrashDumps/*.dmp",

        # --- Windows Old (after update) ---
        "C:/Windows.old/*",
        
        # --- Explorer and Recent Items ---
        "%APPDATA%/Microsoft/Windows/Recent/*.lnk",
        "%LOCALAPPDATA%/Microsoft/Windows/Explorer/thumbcache_*.db",
        "%LOCALAPPDATA%/Microsoft/Windows/Explorer/*",

        # --- Browser Cache ---
        "%LOCALAPPDATA%/Google/Chrome/User Data/*Cache/*",
        "%LOCALAPPDATA%/Google/Chrome/User Data/Default/Code Cache/js/*",
        "%LOCALAPPDATA%/Google/Chrome/User Data/Crashpad/*",
        "%LOCALAPPDATA%/Microsoft/Edge/User Data/*Cache/*",
        "%LOCALAPPDATA%/BraveSoftware/Brave-Browser/User Data/*Cache/*",
        "%APPDATA%/Mozilla/Firefox/Profiles/*/cache2/entries/*",

        # --- App-specific Caches ---
        "%LOCALAPPDATA%/discord/Cache/*",
        "%LOCALAPPDATA%/discord/GPUCache/*",
        "%LOCALAPPDATA%/discord/Code Cache/js/*",
        "%APPDATA%/Microsoft/Teams/*",
        "%USERPROFILE%/AppData/Local/Packages/Microsoft.MSTeams_8wekyb3d8bbwe/LocalCache/Microsoft/MSTeams/*",
        "%PROGRAMFILES(X86)%/Steam/appcache/*",
        "%PROGRAMFILES(X86)%/Steam/steamapps/common/*",
        "%LOCALAPPDATA%/Steam/*",

        # --- Shader Cache (GPU) ---
        "%LOCALAPPDATA%/NVIDIA/DXCache/*",
        "%LOCALAPPDATA%/NVIDIA/GLCache/*",
        "%LOCALAPPDATA%/AMD/DxCache/*",
        "%LOCALAPPDATA%/AMD/GLCache/*",
        "%LOCALAPPDATA%/AMD/DxcCache/*",
        "%PROGRAMDATA%/Intel/ShaderCache/*",
        "%LOCALAPPDATA%/LocalLow/Intel/ShaderCache/*",

        # --- Visual Studio Dev Tools ---
        "%LOCALAPPDATA%/Microsoft/VisualStudio/*/ComponentModelCache/*",
        "%LOCALAPPDATA%/Microsoft/VisualStudio/Roslyn/*",

        # --- Office Logs ---
        "%LOCALAPPDATA%/Microsoft/Office/*",

        # --- Misc System/User Cache Files ---
        "%USERPROFILE%/CHKDSK.CHK",
        "%USERPROFILE%/AppData/Local/Microsoft/DirectX/*",
        "%USERPROFILE%/AppData/Local/Microsoft/Windows/UsrClass.dat",
        "%USERPROFILE%/AppData/Local/Intel/*",
        "%USERPROFILE%/AppData/Local/NVIDIA Corporation/*",
        "%USERPROFILE%/AppData/Local/AMD/*",
        "%USERPROFILE%/AppData/Local/Packages/Microsoft.Store_8wekyb3d8bbwe/LocalState/*",

        # --- Manifest Caches ---
        "%USERPROFILE%/AppData/Local/Microsoft/Windows/ManifestCache/*_blobs.bin",

        # --- Misc Logs ---
        "%USERPROFILE%/AppData/Local/Microsoft/*.log",
    ]

    for pattern in patterns_to_delete:
        delete_files(pattern)

    after = get_disk_space("C:/")
    print(f"Disk space after cleanup: {bytes_to_mb(after)} MB")

    delta = after - before
    if delta > 0:
        print(f"Space increased by: {bytes_to_mb(delta)} MB")
    elif delta < 0:
        print(f"Space decreased by: {bytes_to_mb(-delta)} MB")
    else:
        print("No change in disk space")

if __name__ == "__main__":
    main()

