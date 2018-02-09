# Copyright 2011, Red Hat

%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

%global oname configshell-fb

Name:           python-configshell
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        A framework to implement simple but nice CLIs
Epoch:          1
Version:        1.1.fb24
Release:        3%{?dist}
URL:            https://github.com/agrover/configshell-fb
Source:         https://fedorahosted.org/released/targetcli-fb/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel python2-setuptools

%if 0%{?with_python3}
BuildRequires:  python3-devel python3-setuptools
%endif

%global _description\
A framework to implement simple but nice configuration-oriented\
command-line interfaces.

%description %_description

%package -n python2-configshell
Summary: %summary
Requires: python2-pyparsing python2-urwid python2-six
%{?python_provide:%python_provide python2-configshell}

%description -n python2-configshell %_description

%if 0%{?with_python3}
%package -n python3-configshell
Summary:        A framework to implement simple but nice CLIs
Group:          System Environment/Libraries
Requires:       python3-pyparsing python3-urwid

%description -n python3-configshell
A framework to implement simple but nice configuration-oriented
command-line interfaces.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%files -n python2-configshell
%{python_sitelib}/*
%doc COPYING README.md

%if 0%{?with_python3}
%files -n python3-configshell
%{python3_sitelib}/*
%doc COPYING README.md
%endif

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.fb24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:1.1.fb24-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Jan 26 2018 Andy Grover <agrover@redhat.com> - 1:1.1.fb24-1
- New upstream release
- Remove patch configshell-fix-term.patch

* Fri Dec 01 2017 Troy Dawson <tdawson@redhat.com> - 1:1.1.fb23-5
- Update spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:1.1.fb23-4
- Python 2 binary package renamed to python2-configshell
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.fb23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Andy Grover <agrover@redhat.com> - 1:1.1.fb23-2
- Add patch configshell-fix-term.patch

* Wed Mar 1 2017 Andy Grover <agrover@redhat.com> - 1:1.1.fb23-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.fb20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1:1.1.fb20-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb20-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 7 2016 Andy Grover <agrover@redhat.com> - 1:1.1.fb20-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.fb19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 1 2015 Andy Grover <agrover@redhat.com> - 1:1.1.fb19-1
- New upstream release

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb18-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 27 2015 Andy Grover <agrover@redhat.com> - 1:1.1.fb18-2
- Rebuild

* Tue Jun 23 2015 Andy Grover <agrover@redhat.com> - 1:1.1.fb18-1
- New upstream release
- Add dependency on python-six instead of 2to3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 13 2015 Andy Grover <agrover@redhat.com> - 1:1.1.fb17-1
- New upstream release

* Tue Dec 2 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb16-1
- New upstream release

* Fri Nov 14 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb14-3
- Add python 3 dependencies to Python 3 package

* Thu Nov 13 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb14-2
- Add Python 3 subpackage

* Thu Aug 28 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb14-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb13-1
- New upstream release

* Fri Mar 14 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb12-1
- New upstream release

* Mon Jan 6 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb11-1
- New upstream release

* Fri Nov 1 2013 Andy Grover <agrover@redhat.com> - 1:1.1.fb10-1
- New upstream release

* Thu Sep 12 2013 Andy Grover <agrover@redhat.com> - 1:1.1.fb9-1
- New upstream release
- Remove dependency on python-simpleparse in favor of pyparsing
- Remove BuildRequires

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Andy Grover <agrover@redhat.com> - 1:1.1.fb8-1
- New upstream release
- License now Apache 2.0
- README.md instead of README

* Tue Feb 26 2013 Andy Grover <agrover@redhat.com> - 1:1.1.fb7-1
- New upstream release

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

* Wed Dec 14 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb3-1
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
