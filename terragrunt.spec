Name:           terragrunt
Version:        0.85.1
Release:        1%{?dist}
Summary:        Terraform/OpenTofu IaC orchestration tool 

License:        MIT
URL:            https://github.com/gruntwork-io/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git-core >= 2.0
BuildRequires:  golang >= 1.24

%description
Terraform/OpenTofu IaC orchestration tool

%global debug_package %{nil}

%prep
%autosetup


%build
go get
go build -o %{name} -ldflags "-s -w -X github.com/gruntwork-io/go-commons/version.Version=%{version} -extldflags '-static'" .


%install
mkdir -p %{buildroot}/%{_bindir}

install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE.txt
%{_bindir}/%{name}
%doc README.md SECURITY.md



%changelog
* Sat Sep 27 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- Initial spec file 
