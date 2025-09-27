%global debug_package %{nil}

Name:           resticprofile
Version:        0.32.0
Release:        1%{?dist}
Summary:        Configuration profiles manager and scheduler for restic backup

License:        GPLv3
URL:            https://github.com/creativeprojects/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git-core >= 2.0
BuildRequires:  golang >= 1.24
BuildRequires:  make
Requires:       restic

%description
Configuration profiles manager and scheduler for restic backup

%prep
%autosetup


%build
go build -o %{name} -v -tags no_self_update -ldflags "-X 'main.builtBy=make'"


%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Sat Sep 27 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- 
