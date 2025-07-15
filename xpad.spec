Summary:	Virtual sticky pad system
Summary(pl.UTF-8):	Program do umieszczania na pulpicie "karteczek z notatkami"
Name:		xpad
Version:	2.14
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/xpad/%{name}-%{version}.tar.bz2
# Source0-md5:	1e12e6aec8f03a656eb6427ba22c38d3
Patch0:		%{name}-desktop.patch
URL:		http://xpad.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.11.5
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual sticky pad system.

%description -l pl.UTF-8
Program do umieszczania na pulpicie "karteczek z notatkami".

%prep
%setup -q
%patch -P0 -p1

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

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/*
