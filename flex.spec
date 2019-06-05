#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flex
Version  : 2.6.4
Release  : 25
URL      : https://github.com/westes/flex/archive/v2.6.4.tar.gz
Source0  : https://github.com/westes/flex/archive/v2.6.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: flex-bin
Requires: flex-lib
Requires: flex-doc
Requires: flex-locales
BuildRequires : bison
BuildRequires : flex
BuildRequires : help2man
BuildRequires : texinfo
Patch1: define-gnu-source.patch

%description
This file describes the flex test suite.
* WHO SHOULD USE THE TEST SUITE?
The test suite is intended to be used by flex developers, i.e., anyone hacking
the flex distribution. If you are simply installing flex, then you can ignore
this directory and its contents.

%package bin
Summary: bin components for the flex package.
Group: Binaries

%description bin
bin components for the flex package.


%package dev
Summary: dev components for the flex package.
Group: Development
Requires: flex-lib
Requires: flex-bin
Provides: flex-devel

%description dev
dev components for the flex package.


%package doc
Summary: doc components for the flex package.
Group: Documentation

%description doc
doc components for the flex package.


%package lib
Summary: lib components for the flex package.
Group: Libraries

%description lib
lib components for the flex package.


%package locales
Summary: locales components for the flex package.
Group: Default

%description locales
locales components for the flex package.


%prep
%setup -q -n flex-2.6.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526411446
%autogen --disable-static
make

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1526411446
rm -rf %{buildroot}
%make_install
%find_lang flex

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flex
/usr/bin/flex++

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libfl.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/flex/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfl.so.2
/usr/lib64/libfl.so.2.0.0

%files locales -f flex.lang
%defattr(-,root,root,-)

