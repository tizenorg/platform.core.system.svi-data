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

%files
%manifest %{name}.manifest
%defattr(644,root,root,-)
%{_datadir}/svi/*
%defattr(444,%{TZ_USER_NAME},%{TZ_SYS_USER_GROUP},-)
%manifest svi-data-sdk.manifest
