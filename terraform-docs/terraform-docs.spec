%global debug_package %{nil}

Name:           terraform-docs
# renovate: datasource=github-releases depName=terraform-docs packageName=terraform-docs/terraform-docs
Version:        0.20.0
Release:        1%{?dist}
Summary:        Generate documentation from Terraform modules

License:        MIT
URL:            https://github.com/terraform-docs/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}-linux-amd64.tar.gz
ExclusiveArch:  x86_64

%description
Generate documentation from Terraform modules in various output formats


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
