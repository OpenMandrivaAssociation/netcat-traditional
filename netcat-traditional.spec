%global optflags %{optflags} -std=gnu89 -Wno-int-conversion
%define real_name nc

Summary:	Reads and writes data across network connections using TCP or UDP
Name:		netcat-traditional
Version:	20180111
Release:	1
License:	Public Domain
Group:		Networking/Other
Url:		https://nc110.sourceforge.net/
Source0:	http://sourceforge.net/projects/nc110/files/community%20releases/nc110.%{version}.tar.xz
Source1:	%{real_name}.1
Provides:	netcat = 1.0
Conflicts:	netcat-openbsd
Conflicts:	netcat-gnu

%patchlist
posix-setjmp.patch
single-verbose.patch
tos.patch
rservice-buf.patch      
so-keepalive.patch
select-nfds.patch
proxy-doc.patch

%description
The nc package contains Netcat (the program is now netcat), a simple utility
for reading and writing data across network connections, using the TCP or UDP
protocols. Netcat is intended to be a reliable back-end tool which can be used
directly or easily driven by other programs and scripts. Netcat is also a
feature-rich network debugging and exploration tool, since it can create many
different connections and has many built-in capabilities.

You may want to install the netcat package if you are administering a network
and you'd like to use its debugging and network exploration capabilities.

netcat has been compiled with -DGAPING_SECURITY_HOLE turned on. I do not
believe this is as much of a security hole as the author makes it out to be,
*if* you know what you're doing (but then, if you didn't, you'd still be using
telnet ;-)). Since the spawned program will run as whatever user started
netcat, don't use -e as root. You have been warned, so if some cracker breaks
into your system due to your own stupidity, don't blame me.

A symlink to the netcat binary called 'netcat' has been installed. However, the
canonical name is still 'nc'. If you use netcat on other systems, it will
probably only be installed as 'nc', so keep this in mind when writing scripts.

%prep
%autosetup -p1 -n nc110

%build
# Make linux ids supported, but it makes a static binary. 
make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" \
          DFLAGS='-DLINUX -DTELNET -DGAPING_SECURITY_HOLE' generic

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 nc %{buildroot}%{_bindir}
(cd %{buildroot}%{_bindir} && %{__ln_s} nc netcat)

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1
(cd %{buildroot}%{_mandir}/man1 && %{__ln_s} nc.1 netcat.1)

%files
%doc README Changelog scripts
%{_bindir}/nc
%{_bindir}/netcat
%{_mandir}/man1/nc.1*
%{_mandir}/man1/netcat.1*
