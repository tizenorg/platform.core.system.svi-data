Name:       svi-data-sdk
Summary:    svi library audio data package (SDK)
Version:    0.1.1
Release:    6
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

%post
mkdir -p /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key0.wav            /opt/share/svi/sound/touch/key0.wav
ln -s %{_datadir}/svi/sound/touch/key1.wav            /opt/share/svi/sound/touch/key1.wav
ln -s %{_datadir}/svi/sound/touch/key2.wav            /opt/share/svi/sound/touch/key2.wav
ln -s %{_datadir}/svi/sound/touch/key3.wav            /opt/share/svi/sound/touch/key3.wav
ln -s %{_datadir}/svi/sound/touch/key4.wav            /opt/share/svi/sound/touch/key4.wav
ln -s %{_datadir}/svi/sound/touch/key5.wav            /opt/share/svi/sound/touch/key5.wav
ln -s %{_datadir}/svi/sound/touch/key6.wav            /opt/share/svi/sound/touch/key6.wav
ln -s %{_datadir}/svi/sound/touch/key7.wav            /opt/share/svi/sound/touch/key7.wav
ln -s %{_datadir}/svi/sound/touch/key8.wav            /opt/share/svi/sound/touch/key8.wav
ln -s %{_datadir}/svi/sound/touch/key9.wav            /opt/share/svi/sound/touch/key9.wav
ln -s %{_datadir}/svi/sound/touch/keyasterisk.wav     /opt/share/svi/sound/touch/keyasterisk.wav
ln -s %{_datadir}/svi/sound/touch/keysharp.wav        /opt/share/svi/sound/touch/keysharp.wav
ln -s %{_datadir}/svi/sound/touch/sip.wav             /opt/share/svi/sound/touch/sip.wav
ln -s %{_datadir}/svi/sound/touch/sip_backspace.wav   /opt/share/svi/sound/touch/sip_backspace.wav
ln -s %{_datadir}/svi/sound/touch/touch.wav           /opt/share/svi/sound/touch/touch.wav

mkdir -p /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/call_connect.wav         /opt/share/svi/sound/operation/call_connect.wav
ln -s %{_datadir}/svi/sound/operation/call_disconnect.wav      /opt/share/svi/sound/operation/call_disconnect.wav
ln -s %{_datadir}/svi/sound/operation/charger_connection.wav   /opt/share/svi/sound/operation/charger_connection.wav
ln -s %{_datadir}/svi/sound/operation/fully_charged.wav        /opt/share/svi/sound/operation/fully_charged.wav
ln -s %{_datadir}/svi/sound/operation/list_reorder.wav         /opt/share/svi/sound/operation/list_reorder.wav
ln -s %{_datadir}/svi/sound/operation/lock.wav                 /opt/share/svi/sound/operation/lock.wav
ln -s %{_datadir}/svi/sound/operation/low_battery.wav          /opt/share/svi/sound/operation/low_battery.wav
ln -s %{_datadir}/svi/sound/operation/minute_minder.wav        /opt/share/svi/sound/operation/minute_minder.wav
ln -s %{_datadir}/svi/sound/operation/power_on.wav             /opt/share/svi/sound/operation/power_on.wav
ln -s %{_datadir}/svi/sound/operation/shutter.wav              /opt/share/svi/sound/operation/shutter.wav
ln -s %{_datadir}/svi/sound/operation/slider_sweep.wav         /opt/share/svi/sound/operation/slider_sweep.wav
ln -s %{_datadir}/svi/sound/operation/unlock.wav               /opt/share/svi/sound/operation/unlock.wav
ln -s %{_datadir}/svi/sound/operation/volume_control.wav       /opt/share/svi/sound/operation/volume_control.wav

mkdir -p /opt/share/svi/haptic/default
ln -s %{_datadir}/svi/haptic/default/Basic_call.tht			/opt/share/svi/haptic/default/Basic_call.tht

mkdir -p /opt/share/svi/haptic/touch
ln -s %{_datadir}/svi/haptic/touch/touch.tht					/opt/share/svi/haptic/touch/touch.tht

%files
%manifest svi-data-sdk.manifest
%defattr(644,root,root,-)
%{_datadir}/svi/sound/operation/*
%{_datadir}/svi/sound/touch/*
%{_datadir}/svi/haptic/default/*
%{_datadir}/svi/haptic/touch/*
