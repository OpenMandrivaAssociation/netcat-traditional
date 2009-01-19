%define real_name nc

Name:           netcat-traditional
Version:        1.10
Release:        %mkrel 30
Summary:        Reads and writes data across network connections using TCP or UDP
License:        Public Domain
Group:          Networking/Other
URL:            http://www.vulnwatch.org/netcat/
Source0:        http://www.vulnwatch.org/netcat/nc110.tgz
Source1:        %{real_name}.1
Patch0:         %{real_name}-%{version}-arm.patch
Patch1:         %{real_name}-%{version}-resolv.patch
Patch2:         %{real_name}-%{version}-posix_setjmp.patch
Patch3:         %{real_name}-%{version}-nopunt.patch
Patch4:         %{real_name}-%{version}-nosleep.patch
Patch5:         %{real_name}-%{version}-single_verbose.patch
Patch6:         %{real_name}-%{version}-use_getservbyport.patch
Patch7:         %{real_name}-%{version}-read_overflow.patch
Patch8:         %{real_name}-%{version}-inet_aton.patch
Patch9:         %{real_name}-%{version}-udp_broadcast.patch
Patch10:        %{real_name}-%{version}-quit.patch
Patch11:        nc-1.10-format_not_a_string_literal_and_no_format_arguments.diff
Patch12:        nc-1.10-LDFLAGS.diff
Obsoletes:      nc
Provides:       netcat
Conflicts:      netcat-openbsd
Conflicts:      netcat-gnu
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%patch0 -p1 -b .arm
%patch1 -p1 -b .resolv
%patch2 -p1 -b .posix_setjmp
%patch3 -p1 -b .nopunt
%patch4 -p1 -b .nosleep
%patch5 -p1 -b .single_verbose
%patch6 -p1 -b .use_getservbyport
%patch7 -p1 -b .read_overflow
%patch8 -p1 -b .inet_aton
%patch9 -p1 -b .udp_broadcast
%patch10 -p1 -b .quit
%patch11 -p0 -b .format_not_a_string_literal_and_no_format_arguments
%patch12 -p0 -b .LDFLAGS

%build
# Make linux ids supported, but it makes a static binary. 
%{__make} CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" \
          DFLAGS='-DLINUX -DTELNET -DGAPING_SECURITY_HOLE' generic

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a %{real_name} %{buildroot}%{_bindir}
(cd %{buildroot}%{_bindir} && %{__ln_s} %{real_name} netcat)
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__cp} -a %{SOURCE1} %{buildroot}%{_mandir}/man1/nc.1
(cd %{buildroot}%{_mandir}/man1 && %{__ln_s} %{real_name}.1 netcat.1)

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog scripts
%{_bindir}/nc
%{_bindir}/netcat
%{_mandir}/man1/nc.1*
%{_mandir}/man1/netcat.1*
