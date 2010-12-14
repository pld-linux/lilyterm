%define		_rc	rc8
Summary:	LilyTerm - a terminal emulator
Summary(hu.UTF-8):	LilyTerm egy terminál emulátor
Summary(pl.UTF-8):	LilyTerm - emulator terminala
Name:		lilyterm
Version:	0.9.9
Release:	0.%{_rc}.1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://lilyterm.luna.com.tw/file/%{name}-%{version}~%{_rc}.tar.gz
# Source0-md5:	1f239e7623d8b2c03c6dd7be84f5df3d
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

%description -l pl.UTF-8
Lekki, prosty w użyciu, oparty o libvte emulator terminala.

%prep
%setup -q -n %{name}-%{version}~%{_rc}

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
%doc AUTHORS ChangeLog COPYING TODO
%attr(755,root,root) %{_bindir}/*
## %{_docdir}/lilyterm/examples/lilyterm.rc is equal with %{_sysconfdir}/xdg/lilyterm.rc
## so we skip the %{_prefix}/.../lilyterm.rc
%{_sysconfdir}/xdg/lilyterm.conf
%{_desktopdir}/lilyterm.desktop
%{_pixmapsdir}/lilyterm.*
%{_mandir}/man1/lilyterm.1*
