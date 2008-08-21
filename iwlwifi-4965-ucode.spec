%define name iwlwifi-4965-ucode
# Don't use last numbers for the version, we provide both -1 and -2 ucode apis
%define version 228.57
%define ucode_rel 21
%define release %mkrel 1.%{ucode_rel}.1

Summary: Intel Wireless WiFi Link 4965AGN microcode
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.1.%{ucode_rel}.tgz
Source1: http://intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.2.%{ucode_rel}.tgz
License: Proprietary
Group: System/Kernel and hardware
Url: http://intellinuxwireless.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
The files iwlwifi-4965-*.ucode provided in this package are required to be
present on your system in order for the Intel Wireless WiFi Link 4965AGN
driver for Linux (iwl4965/iwlagn) to be able to operate on your system.

%prep
%setup -q -c -b 1

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
find -name \*.ucode -exec install -m644 {} %{buildroot}/lib/firmware \;
for d in `find -mindepth 1 -maxdepth 1 -type d`; do
	ucode=`echo $d | cut -d . -f 4`
	install -m644 $d/README.iwlwifi-4965-ucode \
	              README.iwlwifi-4965-ucode-$ucode
done
install -m644 $d/LICENSE.iwlwifi-4965-ucode .

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.* README.*
/lib/firmware/*.ucode
