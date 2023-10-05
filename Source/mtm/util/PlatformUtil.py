from mtm.util.Assert import *

from mtm.util.Platforms import Platforms

def toPlatformFolderName(platform):
    # We can just directly use the full platform name for folder names
    return platform

def fromPlatformFolderName(platformDirName):
    platformDirName = platformDirName.lower()

    for curPlatform in Platforms.All:
        if curPlatform.lower() == platformDirName:
            return curPlatform

    assertThat(False)

def fromPlatformArgName(platformArgStr):

    if platformArgStr in ['win', 'w']:
        return Platforms.Windows

    if platformArgStr in ['webgl', 'g']:
        return Platforms.WebGl

    if platformArgStr in ['and', 'a']:
        return Platforms.Android

    if platformArgStr in ['osx', 'o']:
        return Platforms.OsX

    if platformArgStr in ['ios', 'i']:
        return Platforms.Ios

    if platformArgStr in ['lin', 'l']:
        return Platforms.Linux

    if platformArgStr == 'uwp':
        return Platforms.UWP

    if platformArgStr == 'lumin':
        return Platforms.Lumin

    assertThat(False)
    return ''
