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

mkdir -p %{buildroot}/opt/share/svi/sound/touch
mkdir -p %{buildroot}/opt/share/svi/sound/operation
mkdir -p %{buildroot}/opt/share/svi/haptic/default
mkdir -p %{buildroot}/opt/share/svi/haptic/touch

%post
ln -s %{_datadir}/svi/sound/touch/key0.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key1.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key2.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key3.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key4.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key5.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key6.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key7.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key8.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key9.wav            /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/keyasterisk.wav     /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/keysharp.wav        /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/sip.wav             /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/sip_backspace.wav   /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/touch.wav           /opt/share/svi/sound/touch
ln -s %{_datadir}/svi/sound/operation/call_connect.wav         /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/call_disconnect.wav      /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/charger_connection.wav   /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/fully_charged.wav        /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/list_reorder.wav         /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/lock.wav                 /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/low_battery.wav          /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/minute_minder.wav        /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/power_on.wav             /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/shutter.wav              /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/slider_sweep.wav         /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/unlock.wav               /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/volume_control.wav       /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/haptic/default/Basic_call.tht				/opt/share/svi/haptic/default
ln -s %{_datadir}/svi/haptic/touch/touch.tht					/opt/share/svi/haptic/touch

%files
%defattr(644,root,root,-)
%{_datadir}/svi/*
%defattr(666,app,app,-)
%dir /opt/share/svi/sound/touch
%dir /opt/share/svi/sound/operation
%dir /opt/share/svi/haptic/default
%dir /opt/share/svi/haptic/touch
%manifest svi-data-sdk.manifest
