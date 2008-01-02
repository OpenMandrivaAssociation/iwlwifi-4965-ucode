%define name iwlwifi-4965-ucode
%define version 4.44.15
%define release %mkrel 2

Summary: Intel Wireless WiFi Link 4965AGN microcode
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tar.bz2
# This additional firmware is for development iwlwifi drivers, no clean
# way to do this now, they have an extra "-1.ucode" suffix so it's ok
# (no conflicts)
Source1: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-4965-ucode-4.44.1.18.tgz
License: Proprietary
Group: System/Kernel and hardware
Url: http://intellinuxwireless.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
The file iwlwifi-4965.ucode provided in this package is required to be 
present on your system in order for the Intel Wireless WiFi Link
4965AGN driver for Linux (iwlwifi-4965) to be able to operate on your system.

%prep
%setup -q -b 1
chmod -x *

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/
install -m644 ../iwlwifi-4965-ucode-4.44.1.18/*.ucode \
              %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.* README.*
/lib/firmware/*.ucode
