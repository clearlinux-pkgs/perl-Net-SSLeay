#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-SSLeay
Version  : 1.92
Release  : 64
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-1.92.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-1.92.tar.gz
Summary  : 'Perl bindings for OpenSSL and LibreSSL'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Net-SSLeay-license = %{version}-%{release}
Requires: perl-Net-SSLeay-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : openssl-dev

%description
Net-SSLeay - Perl bindings for OpenSSL and LibreSSL
By popular demand...
--------------------

%package dev
Summary: dev components for the perl-Net-SSLeay package.
Group: Development
Provides: perl-Net-SSLeay-devel = %{version}-%{release}
Requires: perl-Net-SSLeay = %{version}-%{release}

%description dev
dev components for the perl-Net-SSLeay package.


%package license
Summary: license components for the perl-Net-SSLeay package.
Group: Default

%description license
license components for the perl-Net-SSLeay package.


%package perl
Summary: perl components for the perl-Net-SSLeay package.
Group: Default
Requires: perl-Net-SSLeay = %{version}-%{release}

%description perl
perl components for the perl-Net-SSLeay package.


%prep
%setup -q -n Net-SSLeay-1.92
cd %{_builddir}/Net-SSLeay-1.92

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-SSLeay
cp %{_builddir}/Net-SSLeay-1.92/LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-SSLeay/5abee7bc8b5c3cb09631ca37a850924ac26588e4
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
/usr/share/man/man3/Net::SSLeay.3
/usr/share/man/man3/Net::SSLeay::Handle.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-SSLeay/5abee7bc8b5c3cb09631ca37a850924ac26588e4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
