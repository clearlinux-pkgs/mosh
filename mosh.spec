#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mosh
Version  : 1.3.2
Release  : 20
URL      : https://mosh.mit.edu/mosh-1.3.2.tar.gz
Source0  : https://mosh.mit.edu/mosh-1.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: mosh-bin
Requires: mosh-doc
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(nettle)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(protobuf)
BuildRequires : pkgconfig(tinfo)
BuildRequires : zlib
BuildRequires : zlib-dev

%description
[![Build Status](https://travis-ci.org/mobile-shell/mosh.svg?branch=master)](https://travis-ci.org/mobile-shell/mosh)

%package bin
Summary: bin components for the mosh package.
Group: Binaries

%description bin
bin components for the mosh package.


%package doc
Summary: doc components for the mosh package.
Group: Documentation

%description doc
doc components for the mosh package.


%prep
%setup -q -n mosh-1.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1501111302
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1501111302
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mosh
/usr/bin/mosh-client
/usr/bin/mosh-server

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
