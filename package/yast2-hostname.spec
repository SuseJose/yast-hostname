#
# spec file for package yast2-caasp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-hostname
Version:        4.1.0
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

# SystemRoleHandlersRunner
Requires:       yast2
BuildRequires:  yast2
# Overview widget
Requires:       yast2-installation >= 3.2.38
BuildRequires:  yast2-installation >= 3.2.38
# chrony support
Requires:       yast2-ntp-client   >= 4.0.3
BuildRequires:  yast2-ntp-client   >= 4.0.3
# parsing dhcp leases (ntp)

Requires:       yast2-network   >= 4.1.11
BuildRequires:  yast2-network   >= 4.1.11

BuildRequires:  yast2-devtools     >= 3.1.39
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(yast-rake) >= 0.2.13

BuildArch:      noarch

Summary:        YaST2 - Hostname  Module
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/JoseSuse/yast-hostname

%description
A model for change your hostname 

%prep
%setup -n %{name}-%{version}

%build

%check
%yast_check

%install
%yast_install

%files
%defattr(-,root,root)
%{yast_clientdir}/*.rb
%dir %{yast_libdir}/y2hostname
%{yast_libdir}/y2hostname/*.rb
%dir %{yast_libdir}/y2hostname/cfa
%{yast_libdir}/y2hostname/cfa/*.rb
%dir %{yast_libdir}/y2hostname/widgets
%{yast_libdir}/y2hostname/widgets/*.rb
%dir %{yast_libdir}/y2hostname/clients
%{yast_libdir}/y2hostname/clients/*.rb
%dir %{yast_libdir}/y2system_role_handlers
%{yast_libdir}/y2system_role_handlers/*.rb
%doc %{yast_docdir}

%changelog
