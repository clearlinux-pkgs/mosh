#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : mosh
Version  : 1.4.0
Release  : 35
URL      : https://github.com/mobile-shell/mosh/releases/download/mosh-1.4.0/mosh-1.4.0.tar.gz
Source0  : https://github.com/mobile-shell/mosh/releases/download/mosh-1.4.0/mosh-1.4.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: mosh-bin = %{version}-%{release}
Requires: mosh-license = %{version}-%{release}
Requires: mosh-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : openssl-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(nettle)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(protobuf)
BuildRequires : pkgconfig(tinfo)
BuildRequires : zlib
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![ci](https://github.com/mobile-shell/mosh/actions/workflows/ci.yml/badge.svg)](https://github.com/mobile-shell/mosh/actions/workflows/ci.yml)

%package bin
Summary: bin components for the mosh package.
Group: Binaries
Requires: mosh-license = %{version}-%{release}

%description bin
bin components for the mosh package.


%package license
Summary: license components for the mosh package.
Group: Default

%description license
license components for the mosh package.


%package man
Summary: man components for the mosh package.
Group: Default

%description man
man components for the mosh package.


%prep
%setup -q -n mosh-1.4.0
cd %{_builddir}/mosh-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689805174
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1689805174
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mosh
cp %{_builddir}/mosh-%{version}/COPYING %{buildroot}/usr/share/package-licenses/mosh/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/mosh-%{version}/COPYING.iOS %{buildroot}/usr/share/package-licenses/mosh/23bf40f764b6aabac3b6492b6e1306d46190b2d5 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mosh
/usr/bin/mosh-client
/usr/bin/mosh-server

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mosh/23bf40f764b6aabac3b6492b6e1306d46190b2d5
/usr/share/package-licenses/mosh/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mosh-client.1
/usr/share/man/man1/mosh-server.1
/usr/share/man/man1/mosh.1
