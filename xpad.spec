Summary:	Virtual sticky pad system
Summary(pl):	Program do umieszczania na pulpicie "karteczek z notatkami"
Name:		xpad
Version:	0.1.9.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/xpad/%{name}-%{version}.tar.gz
URL:		http://xpad.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Virtual sticky pad system. Can be used as tiny font browser:)

%description -l pl
Program do umieszczania na pulpicie "karteczek z notatkami". Mo¿e byæ
u¿ywany jako zgrabna przegl±darka fontów.

%prep
%setup -q

%build
%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install xpad $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
