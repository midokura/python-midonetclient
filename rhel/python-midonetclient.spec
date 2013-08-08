Name:       python-midonetclient
Epoch:      1
Version:    1.1.0
Release:    1.0
Summary:    Python client for MidoNet REST API.
Group:      Development/Languages
License:    Test
URL:        https://github.com/midokura/midonet-client
Source0:    https://github.com/midokura/midonet-client/python-midonet-client-%{version}.tar.gz
BuildArch:  noarch
BuildRoot:  /var/tmp/%{name}-buildroot

%description
Python client for MidoNet REST API.

%prep
%setup -q 

%install
mkdir -p $RPM_BUILD_ROOT/%{python_sitelib}
cp -r src/midonetclient/ $RPM_BUILD_ROOT/%{python_sitelib}/ 

%files
%defattr(-,root,root)
%{python_sitelib}/midonetclient

%changelog
* Thu Aug 8 2013 Guillermo Ontanon <guillermo@midokura.com> - 1.1.0-1.0
* Mon Aug 5 2013 Guillermo Ontanon <guillermo@midokura.com> - 1.0.99-rc5
* Thu Jul 18 2013 Takaaki Suzuki <suzuki@midokura.com> - 1.0.99-rc3
- Initial package
