%global debug_package %{nil}

Name:           tflint
# renovate: datasource=github-releases depName=tflint packageName=terraform-linters/tflint
Version:        0.59.1
Release:        1%{?dist}
Summary:        A pluggable Terraform linter

License:        MPL
URL:            https://github.com/terraform-linters/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}_linux_amd64.zip
ExclusiveArch:  x86_64

%description
A pluggable Terraform linter

%prep
%setup -q -c -T


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}


%files
%{_bindir}/%{name}


%changelog
* Sat Sep 27 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- Initial spec file 
