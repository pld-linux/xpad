Summary:	Virtual sticky pad system
Summary(pl):	Program do umieszczania na pulpicie "karteczek z notatkami"
Name:		xpad
Version:	2.11
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xpad/%{name}-%{version}.tar.bz2
# Source0-md5:	f06f6f2017d2dc944eb187e5232c64c6
Patch0:		%{name}-desktop.patch
URL:		http://xpad.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libSM-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual sticky pad system.

%description -l pl
Program do umieszczania na pulpicie "karteczek z notatkami".

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/*
