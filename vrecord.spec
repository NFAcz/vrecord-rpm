Name:           vrecord
Version:        master
Release:        1%{?dist}
Summary:        Vrecord is open-source software for capturing a video signal and turning it into a digital file.

License:        CC-BY 4.0
URL:            https://github.com/NFAcz/vrecord
Source0:        https://github.com/NFAcz/vrecord/archive/master.zip
Patch0:         vrecord-bypass-homebrew.patch
Patch1:         vrecord-xdg-open.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       ffmpeg mpv qcli gtkdialog

%description
Vrecord is open-source software for capturing a video signal and turning it into a digital file. Its purpose is to make videotape digitization or transfer easier. Vrecord can capture analog and digital signals through a variety of inputs and can create digital video files in a variety of formats and codecs. Vrecord has been designed with needs of audiovisual archivists in mind.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -m 0755 vtest %{buildroot}/%{_bindir}/vtest
mv Resources/Documentation .
cp -p Resources/* %{buildroot}/%{_datadir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.md
%doc Documentation/*
%{_bindir}/%{name}
%{_bindir}/vtest
%{_datadir}/%{name}



%changelog


