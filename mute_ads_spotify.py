# Script Name: mute_ads_spotify.py
# Description: This script detects Spotify ads and automatically mutes them, then unmutes when actual music plays.
# Author: chetanis
# Dependencies: 
# - winsdk: Used to access Windows Media Transport Controls for detecting current media info. Install with `pip install winsdk`.
# - pycaw: Used to control audio volume of specific applications. Install with `pip install pycaw`.

import asyncio
import time

from winsdk.windows.media.control import (
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
)

from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


SPOTIFY_PROCESS = "Spotify.exe"
muted = False


def mute_spotify(mute: bool):
    global muted
    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:
        if session.Process and session.Process.name() == SPOTIFY_PROCESS:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMute(int(mute), None)
            muted = mute
            print("🔇 Muted Spotify" if mute else "🔊 Unmuted Spotify")
            return


async def get_media():
    print("Starting song detection...")
    while True:
        sessions = await MediaManager.request_async()
        current = sessions.get_current_session()

        if not current:
            print("No media playing")
            time.sleep(2)
            continue

        info = await current.try_get_media_properties_async()
        if info.artist == "Spotify" and not muted:
            mute_spotify(True)
        elif info.artist != "Spotify" and muted:
            mute_spotify(False)
        time.sleep(0.5)
    

asyncio.run(get_media())
