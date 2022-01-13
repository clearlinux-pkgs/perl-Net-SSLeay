#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-SSLeay
Version  : 1.92
Release  : 60
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
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Net/SSLeay.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Net/SSLeay.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Net/SSLeay/Handle.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/SSLeay.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/autosplit.ix
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/debug_read.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/do_https.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/do_https2.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/do_https3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/do_https4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/do_httpx2.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/do_httpx3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/do_httpx4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/dump_peer_certificate.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/get_http.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/get_http3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/get_http4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/get_https.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/get_https3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/get_https4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/get_httpx.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/get_httpx3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/get_httpx4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/head_http.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/head_http3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/head_http4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/head_https.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/head_https3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/head_https4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/head_httpx.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/head_httpx3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/head_httpx4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/http_cat.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/https_cat.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/httpx_cat.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/initialize.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/make_form.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/make_headers.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/new_x_ctx.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/open_proxy_tcp_connection.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/open_tcp_connection.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/post_http.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/post_http3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/post_http4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/post_https.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/post_https3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/post_https4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/post_httpx.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/post_httpx3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/post_httpx4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/put_http.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/put_http3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/put_http4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/put_https.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/put_https3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/put_https4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/put_httpx.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/put_httpx3.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/put_httpx4.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/randomize.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/set_cert_and_key.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/set_proxy.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/set_server_cert_and_key.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/ssl_read_CRLF.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/ssl_read_all.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/ssl_read_until.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/ssl_write_CRLF.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/ssl_write_all.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/sslcat.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/tcp_read_CRLF.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/tcp_read_all.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/tcp_read_until.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/tcp_write_CRLF.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/tcp_write_all.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/tcpcat.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/tcpxcat.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/want_X509_lookup.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/want_nothing.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/want_read.al
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/SSLeay/want_write.al
