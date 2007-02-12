Summary:	The Wonder Shaper
Summary(pl.UTF-8):   Wonder Shaper - narzędzie do kształtowania wykorzystania łącza
Name:		wondershaper
Version:	1.1a
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://lartc.org/wondershaper/%{name}-%{version}.tar.gz
# Source0-md5:	bbc5a3a4485ab286e337ce8550e7b990
Patch0:		%{name}-conf.patch
URL:		http://lartc.org/wondershaper/
Requires:	iproute2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Many cablemodem and ADSL users experience horrifying latency while
uploading or downloading. They also notice that uploading hampers
downloading greatly. The wondershaper neatly addresses these issues,
allowing users of a router with a wondershaper to continue using SSH
over a loaded link happily.

%description -l pl.UTF-8
Wielu użytkowników modemów kablowych i ADSL zauważa przerażające
opóźnienia w czasie ściągania lub wysyłania danych, a jednocześnie
widzi, że wysyłanie danych bardzo przeszkadza w ściąganiu.
wondershaper niesie pomoc w takich przypadkach, pozwalając
użytkownikom routera z wondershaperem na wygodne używanie SSH po
obciążonym łączu.

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
%doc ChangeLog README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wshaper.conf
%attr(755,root,root) %{_bindir}/*
