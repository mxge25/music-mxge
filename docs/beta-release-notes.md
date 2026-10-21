# MXGE Player 1.0.0-beta.1

Not yet verified on physical devices. The cutter is experimental.

مشغّل صوت مجاني لأندرويد، يعمل بالكامل دون إنترنت أو إعلانات أو حسابات. عربي وإنجليزي. ملفاتك ومكتبتك ومواضع استماعك محلية.

**نسخة Beta: لم يُتحقق منها على هاتف فعلي بعد. أداة القصّ تجريبية وتُصدّر M4A/AAC.**

- Android 8.0+ · applicationId: io.github.mxge25.player.
- ARM64 is the primary APK (21.52 MiB); ARMv7 is an alternative (18.38 MiB).
- Independent position memory, library/folders/playlists, background controls, bookmarks/notes, A–B and pitch-preserving speed.
- EQ, inherited playback settings, sleep timer, themes/motion, local lyrics and supported chapters.
- Experimental cutter: bounded waveform, range/numeric selection, preview, M4A/AAC export and system-tone assignment where Android permits. Source audio stays unchanged; output/codecs, memory, permissions and audible accuracy still need phone tests. Export is foreground-only.
- Tag editor and home widget are not included. Complex chapter variants remain unsupported.
- Existing 60 logic/widget tests passed. They do not verify hardware audio, Bluetooth, notification behavior, export quality or 60fps.

Before changing from an older development installation, export its local metadata backup. The final applicationId/signing identity installs separately; scan/open local files in the beta, then restore metadata. File access grants do not transfer.

Compare the APK SHA256 with **SHA256SUMS.txt** before installing. Open the APK in Files, allow installation from that source if prompted, install and grant music/audio access. Test per-file resume, local backup/restore/undo and short cutter exports first. Keep backup copies of your media.

Android application source is private. This public repository contains the download page and release distribution metadata only.
