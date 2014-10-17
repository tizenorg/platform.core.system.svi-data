Name:       svi-data-sdk
Summary:    svi library audio data package (SDK)
Version:    0.1.2
Release:    1
Group:      System/Resources
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
Source1:    svi-data-sdk.manifest
Requires(post): coreutils
BuildRequires: cmake

%description
svi library audio data package (SDK)

%prep
%setup -q

%build
cp %{SOURCE1} .
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}/usr/share/svi/sound/touch
mkdir -p %{buildroot}/usr/share/svi/sound/operation
mkdir -p %{buildroot}/usr/share/svi/haptic/default
mkdir -p %{buildroot}/usr/share/svi/haptic/touch

%post
ln -s %{_datadir}/svi/sound/touch/key0.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key1.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key2.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key3.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key4.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key5.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key6.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key7.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key8.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key9.wav            /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/keyasterisk.wav     /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/keysharp.wav        /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/sip.wav             /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/sip_backspace.wav   /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/touch.wav           /usr/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/operation/call_connect.wav         /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/call_disconnect.wav      /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/charger_connection.wav   /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/fully_charged.wav        /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/list_reorder.wav         /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/lock.wav                 /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/low_battery.wav          /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/minute_minder.wav        /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/power_on.wav             /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/shutter.wav              /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/slider_sweep.wav         /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/unlock.wav               /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/volume_control.wav       /usr/share/svi/sound/operation
ln -s %{_datadir}/svi/haptic/default/Basic_call.tht     	/usr/share/svi/haptic/default
ln -s %{_datadir}/svi/haptic/touch/touch.tht	        	/usr/share/svi/haptic/touch

%files
%manifest %{name}.manifest
%defattr(644,root,root,-)
%{_datadir}/svi/*
%defattr(666,$USER,users,-)
%dir /usr/share/svi/sound/touch
%dir /usr/share/svi/sound/operation
%dir /usr/share/svi/haptic/default
%dir /usr/share/svi/haptic/touch
%manifest svi-data-sdk.manifest
