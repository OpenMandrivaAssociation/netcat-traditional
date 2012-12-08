%define real_name nc

Name:           netcat-traditional
Version:        1.10
Release:        %mkrel 37
Summary:        Reads and writes data across network connections using TCP or UDP
License:        Public Domain
Group:          Networking/Other
URL:            http://nc110.sourceforge.net/
Source0:        http://sourceforge.net/projects/nc110/files/unix%20netcat%201.10%20by%20_Hobbit_/%5BUnnamed%20release%5D/nc110.tgz
Source1:        %{real_name}.1
Patch0:         unstripped.patch
Patch1:         glibc-resolv-h.patch
Patch2:         arm-timer.patch
Patch3:         posix-setjmp.patch
Patch4:         no-sleep-punt.patch
Patch5:         single-verbose.patch
Patch6:         use-getservbyport.patch
Patch7:         read-overflow.patch
Patch8:         inet-aton.patch     
Patch9:         udp-broadcast.patch
Patch10:        quit.patch
Patch11:        dash-port.patch
Patch12:        sh-c.patch
Patch13:        tos.patch
Patch14:        rservice-buf.patch      
Patch15:        so-keepalive.patch
Patch16:        nodup-stderr.patch
Patch17:        help-exit-failure.patch
Patch18:        darwin-ipproto.patch
Patch19:        select-nfds.patch
Patch20:        proxy-doc.patch
Patch30:        nc-1.10-format_not_a_string_literal_and_no_format_arguments.diff
Patch31:        nc-1.10-LDFLAGS.patch
Obsoletes:      nc
Conflicts:      netcat < 1.0
Provides:       netcat = 1.0
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
%{__make} CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" \
          DFLAGS='-DLINUX -DTELNET -DGAPING_SECURITY_HOLE' generic

%install
%{__rm} -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 nc %{buildroot}%{_bindir}
(cd %{buildroot}%{_bindir} && %{__ln_s} nc netcat)

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1
(cd %{buildroot}%{_mandir}/man1 && %{__ln_s} nc.1 netcat.1)

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog scripts
%{_bindir}/nc
%{_bindir}/netcat
%{_mandir}/man1/nc.1*
%{_mandir}/man1/netcat.1*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.10-36mdv2011.0
+ Revision: 666609
- mass rebuild

* Sat Jul 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-35mdv2011.0
+ Revision: 554525
- sync with debian patches set
- fix URL (bug #59930)

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10-34mdv2010.1
+ Revision: 520189
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.10-33mdv2010.0
+ Revision: 426251
- rebuild

* Wed Jan 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-32mdv2009.1
+ Revision: 332125
- provides a versionned netcat virtual package

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-31mdv2009.1
+ Revision: 331766
- add a conflict with old netcat package

* Mon Jan 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-30mdv2009.1
+ Revision: 331437
- package renaming
- ship netcat binary
- provides netcat virtual package
- package renaming

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.10-29mdv2009.1
+ Revision: 317477
- fix build with -Werror=format-security (P11)
- use %%ldflags (P12)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.10-28mdv2009.0
+ Revision: 223334
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.10-27mdv2008.1
+ Revision: 153277
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Apr 19 2007 David Walluck <walluck@mandriva.org> 1.10-26mdv2008.0
+ Revision: 15163
- bump release
- license is not GPL (see README)
- don't use %%{make} (jobserver unavailable)

* Thu Apr 19 2007 David Walluck <walluck@mandriva.org> 1.10-24mdv2008.0
+ Revision: 15150
- use only nc, not netcat

* Thu Apr 19 2007 David Walluck <walluck@mandriva.org> 1.10-23mdv2008.0
+ Revision: 15149
- better package compatibility with GNU netcat

