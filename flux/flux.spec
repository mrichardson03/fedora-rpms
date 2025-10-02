%global debug_package %{nil}

Name:           flux
# renovate: datasource=github-releases depName=flux packageName=fluxcd/flux2
Version:        2.6.4
Release:        1%{?dist}
Summary:        Continuous delivery solution for Kubernetes

License:        Apache-2.0
URL:            https://github.com/fluxcd/flux2
Source0:        %{url}/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz
ExclusiveArch:  x86_64

%description
Continuous delivery solution for Kubernetes

%prep
%setup -q -c


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}



%changelog
* Sat Sep 27 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- Initial spec file
