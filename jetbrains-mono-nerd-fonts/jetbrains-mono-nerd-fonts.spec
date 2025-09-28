Name:           jetbrains-mono-nerd-fonts
Version:        3.4.0
Release:        1%{?dist}
Summary:        JetBrainsMono Nerd Fonts

License:        OFL-1.1
URL:            https://github.com/ryanoasis/nerd-fonts
Source0:        %{url}/releases/download/v%{version}/JetBrainsMono.tar.xz

BuildArch:      noarch
Requires:       fontpackages-filesystem

%description
Nerd Fonts is a project that patches developer targeted fonts with a high
number of glyphs (icons).  Specifically to add a high number of extra glyphs
from popular 'iconic fonts' such as Font Awesome, Devicons, Octicons, and others.

This package contains the JetBrains Mono fonts.

%prep
%autosetup -c

%build
# Nothing to do here

%install
install -d %{buildroot}%{_fontbasedir}/%{name}
install -Dm 0644 -p JetBrainsMonoNerdFont*.ttf %{buildroot}%{_fontbasedir}/%{name}

%files
%license OFL.txt
%doc README.md

%{_fontbasedir}/%{name}/JetBrainsMonoNerdFont*.ttf



%changelog
* Sun Sep 28 2025 Michael Richardson <8782+mrichardson03@users.noreply.github.com>
- Initial package 
