# Copyright 2011, Red Hat

%global oname configshell-fb

Name:           python-configshell
License:        AGPLv3
Group:          System Environment/Libraries
Summary:        A framework to implement simple but nice CLIs
Epoch:          1
Version:        1.1.fb6
Release:        2%{?dist}
URL:            https://github.com/agrover/configshell-fb
# Acquire with
# wget --content-disposition https://github.com/agrover/%{oname}/archive/v%{version}.tar.gz
# and it will save with the name below. Not cool, github.
Source:         https://github.com/agrover/%{oname}/archive/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel epydoc python-simpleparse python-urwid
Requires: python-simpleparse python-urwid

%description
A framework to implement simple but nice configuration-oriented
command-line interfaces.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%{python_sitelib}/*
%doc COPYING README

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 4 2013 Andy Grover <agrover@redhat.com> - 1:1.1.fb6-1
- New upstream release
- Update source URL

* Tue Jul 31 2012 Andy Grover <agrover@redhat.com> - 1:1.1.fb5-1
- New upstream release
- Update Source URL to proper tarball

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Andy Grover <agrover@redhat.com> - 1:1.1.fb4-1
- New upstream release

* Tue Dec 14 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb3-1
- New upstream release

* Tue Dec 13 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb2-1
- New upstream release

* Tue Dec 6 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb1-1
- New upstream source and release
- Remove patches:
  * python-configshell-remove-epydoc-dep.patch
  * python-configshell-git-version.patch

* Mon Nov 21 2011 Andy Grover <agrover@redhat.com> - 1:1.1-2
- Properly update changelog
- Sync version with upstream, Epoch used
- Change Source URL to intermediate github repo

* Fri Sep 23 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-5
* Rebuild

* Thu Aug 25 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-4
- Add patch
  - python-configshell-remove-epydoc-dep.patch

* Wed Aug 17 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-3
- Address comments from spec review
  - drop examples/myshell from doc, it hasn't been updated for API change
  - Fully document procedure to generate source .tar.gz
  - Remove "." from summary
  - Remove commented-out spec todos and other cruft

* Mon Aug 1 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-2
- Update to latest git version
- Add urwid builddep

* Tue May 10 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-1
- Initial packaging
