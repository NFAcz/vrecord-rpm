Name:           vrecord
Version:        master
Release:        1%{?dist}
Summary:        Vrecord is open-source software for capturing a video signal and turning it into a digital file.

License:        CC-BY 4.0
URL:            https://github.com/NFAcz/vrecord
Source0:        https://github.com/NFAcz/vrecord/archive/master.zip
Patch0:         vrecord-bypass-homebrew.patch
Patch1:         vrecord-add-desktop-file.patch
Patch2:         vrecord-mpv-script-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       ffmpeg mpv qcli gtkdialog curl gnuplot xmlstarlet mkvtoolnix mediaconch desktopvideo

%description
Vrecord is open-source software for capturing a video signal and turning it into a digital file. Its purpose is to make videotape digitization or transfer easier. Vrecord can capture analog and digital signals through a variety of inputs and can create digital video files in a variety of formats and codecs. Vrecord has been designed with needs of audiovisual archivists in mind.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT
mv Resources/Documentation .
gzip vrecord.1
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -m 0755 vtest %{buildroot}/%{_bindir}/vtest
cp %{name}.1.gz %{buildroot}/%{_mandir}/man1/
cp %{name}.desktop %{buildroot}/%{_datadir}/applications/
cp -p Resources/* %{buildroot}/%{_datadir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.md
%doc Documentation/*
%doc %{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%{_bindir}/vtest
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop



%changelog
* Wed Nov 10 2021 - Jonáš Svatoš <jonas.svatos@nfa.cz>
- Add patch 'vrecord-mpv-script-fix.patch' to fix changes in MPV v0.26 

* Fri Jan 17 2020 - Jonáš Svatoš <jonas.svatos@nfa.cz>
- Remove patch 'vrecord-xdg-open.patch' as it was upstreamed

* Thu Jan 16 2020 - Jonáš Svatoš <jonas.svatos@nfa.cz>
- Initial version

