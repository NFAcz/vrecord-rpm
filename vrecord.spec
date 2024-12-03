Name:           vrecord
%define _tag    2024-10-18
Version:        %(echo %{_tag}|sed 's/-/./g')
Release:        1%{?dist}
Summary:        Vrecord is open-source software for capturing a video signal and turning it into a digital file.

License:        CC-BY 4.0
URL:            https://github.com/amiaopensource/vrecord
Source0:        https://github.com/amiaopensource/vrecord/archive/refs/tags/v%{_tag}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       ffmpeg mpv qcli gtkdialog curl gnuplot xmlstarlet mkvtoolnix mediaconch desktopvideo

%description
Vrecord is open-source software for capturing a video signal and turning it into a digital file. Its purpose is to make videotape digitization or transfer easier. Vrecord can capture analog and digital signals through a variety of inputs and can create digital video files in a variety of formats and codecs. Vrecord has been designed with needs of audiovisual archivists in mind.

%prep
%setup -n vrecord-%{_tag}

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_datadir}/%{name}
install -d %{buildroot}/%{_datadir}/applications
install -d %{buildroot}/%{_mandir}/man1
install -m 0755 %{name} %{buildroot}/%{_datadir}/%{name}
install -m 0755 vtest %{buildroot}/%{_datadir}/%{name}
gzip -c vrecord.1 > %{buildroot}/%{_mandir}/man1/%{name}.1.gz
gzip -c vtest.1 > %{buildroot}/%{_mandir}/man1/vtest.1.gz
mv Resources/Documentation .
cp -pr Resources %{buildroot}/%{_datadir}/%{name}

# Create a wrapper script
cat > %{buildroot}/%{_bindir}/%{name} << EOF
#!/bin/bash
cd /usr/share/vrecord
exec ./vrecord "\$@"
EOF
chmod 0755 %{buildroot}/%{_bindir}/%{name}

# Create a .desktop file
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Vrecord
Comment=Vrecord is open-source software for capturing a video signal and turning it into a digital file.
Exec=/usr/bin/vrecord
Terminal=false
Type=Application
Encoding=UTF-8
Icon=/usr/share/vrecord/Resources/vrecord_logo.png
Categories=Multimedia;
EOF


%files
%defattr(-,root,root,-)
%doc README.md
%doc Documentation/*
%doc %{_mandir}/man1/%{name}.1.gz
%doc %{_mandir}/man1/vtest.1.gz
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop



%changelog
* Tue Dec 3 2024 - Jonáš Svatoš <jonas.svatos@nfa.cz>
- Remove patches as they are obsolete by now, track release by git tag, inline handling of wrapper script and .desktop file

* Wed Nov 10 2021 - Jonáš Svatoš <jonas.svatos@nfa.cz>
- Add patch 'vrecord-mpv-script-fix.patch' to fix changes in MPV v0.26 

* Fri Jan 17 2020 - Jonáš Svatoš <jonas.svatos@nfa.cz>
- Remove patch 'vrecord-xdg-open.patch' as it was upstreamed

* Thu Jan 16 2020 - Jonáš Svatoš <jonas.svatos@nfa.cz>
- Initial version

