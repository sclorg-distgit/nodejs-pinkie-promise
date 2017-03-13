%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name pinkie-promise

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        2.0.0
Release:        5%{?dist}
Summary:        Promise ponyfill with pinkie

License:        MIT
URL:            https://github.com/floatdrop/pinkie-promise
Source0:        https://github.com/floatdrop/%{module_name}/archive/v%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
BuildRequires:  %{?scl_prefix}npm(pinkie)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md 
%doc license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-5
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-4
- Rebuilt with updated metapackage

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-3
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-2
- Enable scl macros, fix license macro for el6

* Mon Nov 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-1
- update to 2.0.0

* Wed Jul 15 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging
