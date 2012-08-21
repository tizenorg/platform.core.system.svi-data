Name:       svi-data-sdk
Summary:    svi library audio data package (SDK)
Version:    0.1.1
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
BuildRequires: cmake


%description
Description: svi library audio data package (SDK)

%prep
%setup -q

%build
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
ln -s %{_datadir}/svi/sound/touch/touch1.wav          /opt/share/svi/sound/touch/touch1.wav
ln -s %{_datadir}/svi/sound/touch/touch2.wav          /opt/share/svi/sound/touch/touch2.wav
ln -s %{_datadir}/svi/sound/touch/touch3.wav          /opt/share/svi/sound/touch/touch3.wav

mkdir -p /opt/share/svi/sound/operation
ln -s %{_datadir}/svi/sound/operation/call_connect.wav         /opt/share/svi/sound/operation/call_connect.wav
ln -s %{_datadir}/svi/sound/operation/call_disconnect.wav      /opt/share/svi/sound/operation/call_disconnect.wav
ln -s %{_datadir}/svi/sound/operation/charger_connection.wav   /opt/share/svi/sound/operation/charger_connection.wav
ln -s %{_datadir}/svi/sound/operation/fully_charged.wav        /opt/share/svi/sound/operation/fully_charged.wav
ln -s %{_datadir}/svi/sound/operation/list_reorder.wav         /opt/share/svi/sound/operation/list_reorder.wav
ln -s %{_datadir}/svi/sound/operation/lock.wav                 /opt/share/svi/sound/operation/lock.wav
ln -s %{_datadir}/svi/sound/operation/low_battery.wav          /opt/share/svi/sound/operation/low_battery.wav
ln -s %{_datadir}/svi/sound/operation/minute_minder.wav        /opt/share/svi/sound/operation/minute_minder.wav
ln -s %{_datadir}/svi/sound/operation/new_chat.wav             /opt/share/svi/sound/operation/new_chat.wav
ln -s %{_datadir}/svi/sound/operation/on_off_slider.wav        /opt/share/svi/sound/operation/on_off_slider.wav
ln -s %{_datadir}/svi/sound/operation/power_off.wav            /opt/share/svi/sound/operation/power_off.wav
ln -s %{_datadir}/svi/sound/operation/power_on.wav             /opt/share/svi/sound/operation/power_on.wav
ln -s %{_datadir}/svi/sound/operation/sent_chat.wav            /opt/share/svi/sound/operation/sent_chat.wav
ln -s %{_datadir}/svi/sound/operation/shutter.wav              /opt/share/svi/sound/operation/shutter.wav
ln -s %{_datadir}/svi/sound/operation/slider_sweep.wav         /opt/share/svi/sound/operation/slider_sweep.wav
ln -s %{_datadir}/svi/sound/operation/unlock.wav               /opt/share/svi/sound/operation/unlock.wav

%files
%defattr(644,root,root,-) 
%{_datadir}/svi/sound/operation/*
%{_datadir}/svi/sound/touch/*

%changelog
* Tue Aug 14 2012 - Jiyoung Yun <jy910.yun@samsung.com>
- Apply AUI 1.3 ver.
- Tag : svi-data-sdk-0.1.1-1
