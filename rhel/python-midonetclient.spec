# TODO:
# -RONN documentation not built and installed.
# -Man files not built and installed.
# -Changelog.gz not installed.
# -.pyc files not built and installed.
Name:       python-midonetclient
Epoch:      1
Version:    1.2.0
Release:    0.1.rc3
Summary:    Python client for MidoNet REST API.
Group:      Development/Languages
License:    Test
URL:        https://github.com/midokura/midonet-client
Source0:    https://github.com/midokura/midonet-client/python-midonetclient-%{version}.tar.gz
BuildArch:  noarch
BuildRoot:  /var/tmp/%{name}-buildroot
# I added this line but then had to comment it out to build on Ubuntu,
# since rpm doesn't know about packages installed via dpkg. Leaving it
# commented out until someone can test on an RPM system.
# BuildRequires: python, python-support, python-unittest2, python-all-dev, ruby-ronn
# Commented these out because they work in RHEL but CentOS still hasn't
# got those packages available.
# Requires: python >= 2.6, python-webob, python-eventlet, python-httplib2

%description
Python client for MidoNet REST API.

%prep
%setup -q
for r in doc/*.ronn
do
    ronn --roff $r
    gzip ${r%.ronn}
done


%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/%{python_sitelib}
cp -r doc/*.gz $RPM_BUILD_ROOT/%{_mandir}/man1
cp -r rhel/copyright $RPM_BUILD_ROOT/%{_docdir}/%{name}/
cp -r README $RPM_BUILD_ROOT/%{_docdir}/%{name}/
cp -r src/midonetclient/ $RPM_BUILD_ROOT/%{python_sitelib}/
cp -r src/bin/midonet-cli $RPM_BUILD_ROOT/%{_bindir}/

%files
%defattr(-,root,root)
%{_bindir}/midonet-cli
%{_docdir}/%{name}
%{_mandir}/man1
%{python_sitelib}/midonetclient

%changelog
* Thu Aug 8 2013 Guillermo Ontanon <guillermo@midokura.com> - 1.1.0-1.0
* Mon Aug 5 2013 Guillermo Ontanon <guillermo@midokura.com> - 1.0.99-rc5
* Thu Jul 18 2013 Takaaki Suzuki <suzuki@midokura.com> - 1.0.99-rc3
- Initial package
