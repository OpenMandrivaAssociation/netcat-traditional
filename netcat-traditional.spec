%define real_name nc

Summary:	Reads and writes data across network connections using TCP or UDP
Name:		netcat-traditional
Version:	1.12
Release:	2
License:	Public Domain
Group:		Networking/Other
Url:		https://nc110.sourceforge.net/
Source0:	http://sourceforge.net/projects/nc110/files/unix%20netcat%201.10%20by%20_Hobbit_/%5BUnnamed%20release%5D/nc110.tgz
Source1:	%{real_name}.1
Patch0:		unstripped.patch
Patch1:		glibc-resolv-h.patch
Patch2:		arm-timer.patch
Patch3:		posix-setjmp.patch
Patch4:		no-sleep-punt.patch
Patch5:		single-verbose.patch
Patch6:		use-getservbyport.patch
Patch7:		read-overflow.patch
Patch8:		inet-aton.patch     
Patch9:		udp-broadcast.patch
Patch10:	quit.patch
Patch11:	dash-port.patch
Patch12:	sh-c.patch
Patch13:	tos.patch
Patch14:	rservice-buf.patch      
Patch15:	so-keepalive.patch
Patch16:	nodup-stderr.patch
Patch17:	help-exit-failure.patch
Patch18:	darwin-ipproto.patch
Patch19:	select-nfds.patch
Patch20:	proxy-doc.patch
Patch30:	nc-1.10-format_not_a_string_literal_and_no_format_arguments.diff
Patch31:	nc-1.10-LDFLAGS.patch
Provides:	netcat = 1.0
Conflicts:	netcat-openbsd
Conflicts:	netcat-gnu

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
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

%patch30 -p0
%patch31 -p0

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

