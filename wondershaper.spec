Summary:	The Wonder Shaper
Name:		wondershaper
Version:	1.1a
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://lartc.org/wondershaper/%{name}-%{version}.tar.gz
# Source0-md5:	bbc5a3a4485ab286e337ce8550e7b990
Patch0:		%{name}-conf.patch
URL:		http://lartc.org/wondershaper/
Requires:	iproute2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Many cablemodem and ADSL users experience horrifying latency while
uploading or downloading. They also notice that uploading hampers
downloading greatly. The wondershaper neatly addresses these issues,
allowing users of a router with a wondershaper to continue using SSH
over a loaded link happily.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -D wshaper.conf  $RPM_BUILD_ROOT%{_sysconfdir}/wshaper.conf
install -D wshaper  $RPM_BUILD_ROOT%{_bindir}/wshaper
install wshaper.htb $RPM_BUILD_ROOT%{_bindir}/wshaper.htb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/wshaper.conf
%attr(755,root,root) %{_bindir}/*
%doc README ChangeLog
