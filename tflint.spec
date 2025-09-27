Name:           tflint
Version:        0.58.1
Release:        1%{?dist}
Summary:        A pluggable Terraform linter

License:        MPL
URL:            https://github.com/terraform-linters/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git-core >= 2.0
BuildRequires:  golang >= 1.24
BuildRequires:  make

%description
A pluggable Terraform linter

%global debug_package %{nil}

%prep
%autosetup


%build
%make_build


%install
install -Dpm 0755 dist/%{name} %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE
%doc docs/
%{_bindir}/%{name}



%changelog
* Sat Sep 27 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- Initial spec file 
