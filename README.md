# vrecord-rpm
 - RPM spec file for [Vrecord](https://github.com/amiaopensource/vrecord)
 - You can find RPM builds on [COPR](https://copr.fedorainfracloud.org/coprs/lsde/vrecord/)
 - Assumes that available RPM repositories contain a build of FFmpeg with `--enable-decklink`.
 - Repositories with tested FFmpeg build:
   - [epel-multimedia](https://negativo17.org/repos/epel-multimedia.repo) for RHEL/CentOS
   - [fedora-multimedia](https://negativo17.org/repos/fedora-multimedia.repo) for recent Fedora releases
 - Contains following patches:
   - replace hardcoded paths for AMIA's Homebrew [FFmpeg build](https://github.com/amiaopensource/homebrew-amiaos), with standard POSIX binary path.
   - add .desktop file entry to have a nice menu shortcut, which opens GUI mode on top of terminal emulator.
