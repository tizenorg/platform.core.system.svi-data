Name:       svi-data-sdk
Summary:    svi library audio data package (SDK)
Version:    0.1.0
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache License v2.0
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

%files
%defattr(644,root,root,-) 
%{_datadir}/svi/sound/operation/call_connect.wav
%{_datadir}/svi/sound/operation/low_battery.wav
%{_datadir}/svi/sound/operation/shutter.wav
%{_datadir}/svi/sound/operation/lock.wav
%{_datadir}/svi/sound/operation/new_chat.wav
%{_datadir}/svi/sound/operation/charger_connection.wav
%{_datadir}/svi/sound/operation/call_disconnect.wav
%{_datadir}/svi/sound/operation/unlock.wav
%{_datadir}/svi/sound/operation/sent_chat.wav
%{_datadir}/svi/sound/operation/fully_charged.wav
%{_datadir}/svi/sound/operation/vibration.wav
%{_datadir}/svi/sound/operation/minute_minder.wav
%{_datadir}/svi/sound/touch/key5.wav
%{_datadir}/svi/sound/touch/key3.wav
%{_datadir}/svi/sound/touch/key2.wav
%{_datadir}/svi/sound/touch/sip.wav
%{_datadir}/svi/sound/touch/key8.wav
%{_datadir}/svi/sound/touch/key1.wav
%{_datadir}/svi/sound/touch/key4.wav
%{_datadir}/svi/sound/touch/keysharp.wav
%{_datadir}/svi/sound/touch/key0.wav
%{_datadir}/svi/sound/touch/key9.wav
%{_datadir}/svi/sound/touch/keyasterisk.wav
%{_datadir}/svi/sound/touch/key6.wav
%{_datadir}/svi/sound/touch/key7.wav
%{_datadir}/svi/sound/touch/touch1.wav

