%global debug_package %{nil}

Name:           lazygit
# renovate: datasource=github-releases depName=lazygit packageName=jesseduffield/lazygit
Version:        0.58.0
Release:        1%{?dist}
Summary:        Simple terminal UI for git commands

License:        MIT
URL:            https://github.com/jesseduffield/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}_%{version}_linux_x86_64.tar.gz
ExclusiveArch:  x86_64

%description
A simple terminal UI for git commands


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
