Name:       firefox-disable-ai-ml
Version:    0.4
Release:    %autorelease
Summary:    Disable all AI and ML preferences in Firefox
License:    MIT
URL:        https://github.com/py0xc3/firefox-disable-ai-ml
Source0:    https://github.com/py0xc3/firefox-disable-ai-ml/archive/refs/tags/v%{version}.tar.gz

Requires: firefox

BuildRequires: systemd-rpm-macros

%global mozappdir     %{_libdir}/firefox
%global debug_package %{nil}

%description
By default, Firefox enables certain AI/ML preferences.
The "Block AI" option in the settings does not disable them
but only hides them. This means, users must disable these
preferences manually in about:config and thus know what they
are doing: there are many AI/ML preferences that could
change over time, while existing documentation does not
determine any preference that disables all AI/ML reliably
throughout future versions: this forces users to monitor
their settings themselves if they do not want AI/ML enabled.
This package will disable AI/ML preferences automatically
and if Firefox changes its AI/ML preferences in future, the
package can auto-update the preferences to keep AI/ML
disabled for users who want it that way: if any one user
finds changed or new AI/ML settings, they can report it
against the source repo so that all users can get an update
that keeps AI/ML disabled.

%prep
%autosetup -n %{name}-%{version}

%build
#not applicable

%install
mkdir -p %{buildroot}%{mozappdir}/defaults/pref
install -p -m 0644 -D -T autoconfig.js %{buildroot}%{mozappdir}/defaults/pref/autoconfig.js
install -p -m 0644 -D -T ff_disable_ai_ml.cfg %{buildroot}%{mozappdir}/ff_disable_ai_ml.cfg

%files
%license LICENSE
%{mozappdir}/defaults/pref/autoconfig.js
%{mozappdir}/ff_disable_ai_ml.cfg

%changelog
%autochangelog
