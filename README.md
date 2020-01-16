# vrecord-rpm
 - RPM spec file for [Vrecord](https://github.com/amiaopensource/vrecord)
 - Assumes repositories contain a build of FFmpeg with `--enable-decklink`
 - Contains following patches:
   - replace hardcoded paths for AMIA's Homebrew [FFmpeg build](https://github.com/amiaopensource/homebrew-amiaos), with standard POSIX binary path.
   - replace `open` (which is nonexistent on Linux) with `xdg-open`
