
Name: app-samba-extension
Epoch: 1
Version: 2.1.6
Release: 1%{dist}
Summary: Samba Extension - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-samba-extension-%{version}.tar.gz
Buildarch: noarch

%description
The Samba Extension extends the directory with attributes required for Windows Networking.

%package core
Summary: Samba Extension - Core
Requires: app-base-core
Requires: app-openldap-directory-core
Requires: app-samba-core
Requires: app-users

%description core
The Samba Extension extends the directory with attributes required for Windows Networking.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/samba_extension
cp -r * %{buildroot}/usr/clearos/apps/samba_extension/

install -D -m 0644 packaging/samba.php %{buildroot}/var/clearos/openldap_directory/extensions/20_samba.php

%post core
logger -p local6.notice -t installer 'app-samba-extension-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/samba_extension/deploy/install ] && /usr/clearos/apps/samba_extension/deploy/install
fi

[ -x /usr/clearos/apps/samba_extension/deploy/upgrade ] && /usr/clearos/apps/samba_extension/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-samba-extension-core - uninstalling'
    [ -x /usr/clearos/apps/samba_extension/deploy/uninstall ] && /usr/clearos/apps/samba_extension/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/samba_extension/packaging
%dir /usr/clearos/apps/samba_extension
/usr/clearos/apps/samba_extension/deploy
/usr/clearos/apps/samba_extension/language
/usr/clearos/apps/samba_extension/libraries
/var/clearos/openldap_directory/extensions/20_samba.php
