Summary:	Virtual sticky pad system
Summary(pl):	Program do umieszczania na pulpicie "karteczek z notatkami"
Name:		xpad
Version:	0.1.9.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/xpad/%{name}-%{version}.tar.gz
URL:		http://xpad.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Virtual sticky pad system. Can be used as tiny font browser:)

%description -l pl
Program do umieszczania na pulpicie "karteczek z notatkami". Mo�e by�
u�ywany jako zgrabna przegl�darka font�w.

%prep
%setup -q

%build
%{__make} clean
%{__make} CC="%{__cc} %{rpmcflags}"

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
