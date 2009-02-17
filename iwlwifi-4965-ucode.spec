Summary: Intel Wireless WiFi Link 4965AGN microcode
Name: iwlwifi-4965-ucode
Version: 228.57.2.23
Release: %mkrel 1
Source0: http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
Source1: http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-4965-ucode-228.57.1.21.tgz
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
%setup -q -a 1

# provide old firmware with ucode_api=1 for compatibility with older kernels
cp iwlwifi-4965-ucode-228.57.1.21/iwlwifi-4965-1.ucode .
cp iwlwifi-4965-ucode-228.57.1.21/README.iwlwifi-4965-ucode \
   README.iwlwifi-4965-ucode-1
mv README.iwlwifi-4965-ucode README.iwlwifi-4965-ucode-2

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.* README.*
/lib/firmware/*.ucode
