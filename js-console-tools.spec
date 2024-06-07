%define realname linuxconsoletools

Name:    js-console-tools
Version: 1.8.1
Release: 1
License: GPLv2
Summary: Joystick calibration/test console utilities
URL:     https://linuxconsole.sourceforge.net
Group:   Development/Other
Source0: https://downloads.sourceforge.net/linuxconsole/%{realname}-%{version}.tar.bz2

%description
The following utilities are provided to calibrate and test joysticks:
* evdev-joystick - calibrate joystick devices (including dead zones
  and fuzz)
* ffcfstress, ffmvforce, fftest - test force-feedback devices
* ffset - set force-feedback device parameters
* jscal - calibrate joystick devices, reconfigure the axes and buttons
* jscal-store, jscal-restore - store and retrieve joystick device
  settings as configured using jscal
* jstest - test joystick devices

%prep
%autosetup -n %{realname}-%{version}

%build
%make_build

%install
%make_install PREFIX=/usr
mv %{buildroot}/lib %{buildroot}/usr/

%files
%doc README
%license COPYING
%{_bindir}/evdev-joystick
%{_bindir}/ffcfstress
%{_bindir}/ffmvforce
%{_bindir}/ffset
%{_bindir}/fftest
%{_bindir}/inputattach
%{_bindir}/jscal
%{_bindir}/jscal-restore
%{_bindir}/jscal-store
%{_bindir}/jstest
%{_datadir}/joystick
%{_mandir}/man1/evdev-joystick*
%{_mandir}/man1/ffcfstress*
%{_mandir}/man1/ffmvforce*
%{_mandir}/man1/ffset*
%{_mandir}/man1/fftest*
%{_mandir}/man1/inputattach*
%{_mandir}/man1/jscal*
%{_mandir}/man1/jstest*
%{_udevrulesdir}/80-stelladaptor-joystick.rules
%{_udevrulesdir}/../js-set-enum-leds
