Name:       svi-data-sdk
Summary:    svi library audio data package (SDK)
Version:    0.1.2
Release:    1
Group:      System/Resources
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
Source1:    svi-data-sdk.manifest
Requires(post): coreutils
Requires: libtzplatform-config
BuildRequires: cmake
BuildRequires: pkgconfig(libtzplatform-config)
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

mkdir -p %{buildroot}%{TZ_SYS_SHARE}/svi/sound/touch
mkdir -p %{buildroot}%{TZ_SYS_SHARE}/svi/sound/operation
mkdir -p %{buildroot}%{TZ_SYS_SHARE}/svi/haptic/default
mkdir -p %{buildroot}%{TZ_SYS_SHARE}/svi/haptic/touch

%post
ln -s %{_datadir}/svi/sound/touch/key0.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key1.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key2.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key3.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key4.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key5.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key6.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key7.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key8.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/key9.wav            %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/keyasterisk.wav     %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/keysharp.wav        %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/sip.wav             %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/sip_backspace.wav   %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/touch/touch.wav           %{TZ_SYS_SHARE}/svi/sound/touch
ln -s %{_datadir}/svi/sound/operation/call_connect.wav         %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/call_disconnect.wav      %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/charger_connection.wav   %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/fully_charged.wav        %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/list_reorder.wav         %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/lock.wav                 %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/low_battery.wav          %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/minute_minder.wav        %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/power_on.wav             %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/shutter.wav              %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/slider_sweep.wav         %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/unlock.wav               %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/volume_control.wav       %{TZ_SYS_SHARE}/svi/sound/operation
ln -s %{_datadir}/svi/haptic/default/Basic_call.tht            %{TZ_SYS_SHARE}/svi/haptic/default
ln -s %{_datadir}/svi/haptic/touch/touch.tht                   %{TZ_SYS_SHARE}/svi/haptic/touch

%files
%manifest %{name}.manifest
%defattr(644,root,root,-)
%{_datadir}/svi/*
%defattr(666,%{TZ_USER_NAME},%{TZ_SYS_USER_GROUP},-)
%dir %{TZ_SYS_SHARE}/svi/sound/touch
%dir %{TZ_SYS_SHARE}/svi/sound/operation
%dir %{TZ_SYS_SHARE}/svi/haptic/default
%dir %{TZ_SYS_SHARE}/svi/haptic/touch
%manifest svi-data-sdk.manifest
