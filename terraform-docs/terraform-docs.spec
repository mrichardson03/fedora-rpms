%global debug_package %{nil}

Name:           terraform-docs
Version:        0.20.0
Release:        1%{?dist}
Summary:        Generate documentation from Terraform modules

License:        MIT
URL:            https://github.com/terraform-docs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git-core >= 2.0
BuildRequires:  golang >= 1.24
BuildRequires:  make

%description
Generate documentation from Terraform modules in various output formats


%prep
%autosetup


%build
go build -o bin/%{name}


%install
install -Dpm 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE
%doc README.md docs/
%{_bindir}/%{name}



%changelog
* Sat Sep 27 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- Initial spec file 
