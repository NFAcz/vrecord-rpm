# vrecord-rpm
 - RPM spec file for [Vrecord](https://github.com/amiaopensource/vrecord)
 - You can find RPMs as [artifacts](https://git.digilab.nfa.cz/nfa-infra/vrecord-rpm/-/artifacts)
 - Assumes that available RPM repositories contain a build of FFmpeg with `--enable-decklink`.
 - Repositories with tested FFmpeg build:
   - [epel-multimedia](https://negativo17.org/repos/epel-multimedia.repo) for RHEL/CentOS
   - [fedora-multimedia](https://negativo17.org/repos/fedora-multimedia.repo) for recent Fedora releases
 - Contains following additions:
   - add wrapper script to /usr/bin
   - add .desktop file entry which opens Vrecord in GUI mode.
