%global debug_package %{nil}

Name:           terragrunt
# renovate: datasource=github-releases depName=terragrunt packageName=gruntwork-io/terragrunt
Version:        0.93.12
Release:        1%{?dist}
Summary:        Terraform/OpenTofu IaC orchestration tool 

License:        MIT
URL:            https://github.com/gruntwork-io/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}_linux_amd64
ExclusiveArch:  x86_64

BuildRequires:  git-core >= 2.0
BuildRequires:  golang >= 1.24

%description
Terraform/OpenTofu IaC orchestration tool

%global debug_package %{nil}

%prep
%setup -q -T -c


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}


%changelog
* Sat Sep 27 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- Initial spec file 
