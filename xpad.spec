Summary:	Virtual sticky pad system
Summary(pl):	Program do umieszczania na pulpicie "karteczek z notatkami"
Name:		xpad
Version:	1.10.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xpad/%{name}-%{version}.tar.gz
# Source0-md5:	56d9c05c4bf0184922e380ae1353a4a3
Source1:	%{name}.desktop
URL:		http://xpad.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	freetype-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual sticky pad system.

%description -l pl
Program do umieszczania na pulpicie "karteczek z notatkami".

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_pixmapsdir},%{_applnkdir}/Office/Misc}

#%%{__make} install DESTDIR=$RPM_BUILD_ROOT
install src/xpad $RPM_BUILD_ROOT%{_bindir}
install images/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/Misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/README doc/ChangeLog doc/TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/Office/Misc/*
%{_pixmapsdir}/*
