Summary:	LilyTerm - a terminal emulator
Summary(hu.UTF-8):	LilyTerm egy terminál emulátor
Summary(pl.UTF-8):	LilyTerm - emulator terminala
Name:		lilyterm
Version:	0.9.6
Release:	0.1
License:	Other (maybe gpl-like)
Group:		X11/Applications
Source0:	http://lilyterm.luna.com.tw/%{name}-%{version}.tar.gz
# Source0-md5:	d18e93fd679b9b8aea1d25d5cf4fbb70
URL:		http://lilyterm.luna.com.tw/index_en.html
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	perl-libxml
BuildRequires:	vte-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A light and easy to use libvte based X Terminal Emulator.

%description -l hu.UTF-8
Egy gyors és könnyen használható libvte alapú X Terminál Emulátor.

%prep
%setup -q

%build
%{__aclocal}
%{__autoheader}
%{__intltoolize}
%{__automake}
%{__autoconf}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS TODO
%attr(755,root,root) %{_bindir}/*
## /usr/share/doc/lilyterm/examples/lilyterm.rc is equal with /etc/xdg/lilyterm.rc
## so we skip the /usr/.../lilyterm.rc
%{_sysconfdir}/xdg/lilyterm.rc
%{_desktopdir}/lilyterm.desktop
%{_pixmapsdir}/*
