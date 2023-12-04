#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Scope-Guard
Version  : 0.21
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/Scope-Guard-0.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/Scope-Guard-0.21.tar.gz
Summary  : 'lexically-scoped resource management'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Scope-Guard-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Scope-Guard version 0.21
========================
This module provides a convenient way to perform cleanup or other forms of resource
management at the end of a scope. It is particularly useful when dealing with exceptions:
the Scope::Guard constructor takes a reference to a subroutine that is guaranteed to
be called even if the thread of execution is aborted prematurely. This effectively allows
lexically-scoped "promises" to be made that are automatically honoured by perl's garbage
collector.

%package dev
Summary: dev components for the perl-Scope-Guard package.
Group: Development
Provides: perl-Scope-Guard-devel = %{version}-%{release}
Requires: perl-Scope-Guard = %{version}-%{release}

%description dev
dev components for the perl-Scope-Guard package.


%package perl
Summary: perl components for the perl-Scope-Guard package.
Group: Default
Requires: perl-Scope-Guard = %{version}-%{release}

%description perl
perl components for the perl-Scope-Guard package.


%prep
%setup -q -n Scope-Guard-0.21
cd %{_builddir}/Scope-Guard-0.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Scope::Guard.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
