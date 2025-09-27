%global debug_package %{nil}

Name:           flux
Version:        2.6.4
Release:        1%{?dist}
Summary:        Continuous delivery solution for Kubernetes

License:        Apache-2.0
URL:            https://github.com/fluxcd/flux2
Source0:        %{url}/archive/v%{version}/flux2-%{version}.tar.gz

BuildRequires:  git-core >= 2.0
BuildRequires:  golang >= 1.24
BuildRequires:  make kustomize

%description
Continuous delivery solution for Kubernetes

%prep
%setup -qn flux2-%{version}


%build
VERSION=%{version} make build


%install
install -Dpm 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md docs/
%{_bindir}/%{name}



%changelog
* Sat Sep 27 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- Initial spec file
