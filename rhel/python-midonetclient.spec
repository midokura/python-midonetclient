# TODO:
# -RONN documentation not built and installed.
# -Man files not built and installed.
# -Changelog.gz not installed.
# -.pyc files not built and installed.
Name:       python-midonetclient
Epoch:      1
Version:    %{version}
Release:    %{release}
Summary:    Python client for MidoNet REST API.
Group:      Development/Languages
License:    Test
URL:        https://github.com/midokura/python-midonetclient
Source0:    https://github.com/midokura/python-midonetclient-%{version}.tar.gz
BuildArch:  noarch
BuildRoot:  /var/tmp/%{name}-buildroot
# I added this line but then had to comment it out to build on Ubuntu,
# since rpm doesn't know about packages installed via dpkg. Leaving it
# commented out until someone can test on an RPM system.
# BuildRequires: python, python-support, python-unittest2, python-all-dev, ruby-ronn
Requires: python >= 2.6, python-webob, python-eventlet, python-httplib2

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
* %{now} Midokura <info@midokura.com> - Package for %{version}-%{release}
- Initial package
