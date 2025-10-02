%global debug_package %{nil}

Name:           resticprofile
# renovate: datasource=github-releases depName=resticprofile packageName=creativeprojects/resticprofile
Version:        0.32.0
Release:        1%{?dist}
Summary:        Configuration profiles manager and scheduler for restic backup

License:        GPLv3
URL:            https://github.com/creativeprojects/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}_no_self_update_%{version}_linux_amd64.tar.gz
ExclusiveArch:  x86_64

%description
Configuration profiles manager and scheduler for restic backup

%prep
%setup -q -c


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}


%files
%{_bindir}/%{name}


%changelog
* Sat Sep 27 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- Initial package
