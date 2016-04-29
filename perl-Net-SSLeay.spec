#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-SSLeay
Version  : 1.74
Release  : 18
URL      : http://search.cpan.org/CPAN/authors/id/M/MI/MIKEM/Net-SSLeay-1.74.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/M/MI/MIKEM/Net-SSLeay-1.74.tar.gz
Summary  : 'Perl extension for using OpenSSL'
Group    : Development/Tools
License  : Artistic-1.0-Perl Artistic-2.0
Requires: perl-Net-SSLeay-lib
Requires: perl-Net-SSLeay-doc
BuildRequires : openssl-dev
BuildRequires : zlib-dev

%description
By popular demand...
--------------------
perl -MNet::SSLeay -e '($p)=Net::SSLeay::get_https("www.openssl.org", 443, "/"); print $p'

%package doc
Summary: doc components for the perl-Net-SSLeay package.
Group: Documentation

%description doc
doc components for the perl-Net-SSLeay package.


%package lib
Summary: lib components for the perl-Net-SSLeay package.
Group: Libraries

%description lib
lib components for the perl-Net-SSLeay package.


%prep
cd ..
%setup -q -n Net-SSLeay-1.74

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/Net/SSLeay.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/Net/SSLeay.pod
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/Net/SSLeay/Handle.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/autosplit.ix
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/debug_read.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/do_https.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/do_https2.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/do_https3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/do_https4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/do_httpx2.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/do_httpx3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/do_httpx4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/dump_peer_certificate.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/get_http.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/get_http3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/get_http4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/get_https.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/get_https3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/get_https4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/get_httpx.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/get_httpx3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/get_httpx4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/head_http.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/head_http3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/head_http4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/head_https.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/head_https3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/head_https4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/head_httpx.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/head_httpx3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/head_httpx4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/http_cat.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/https_cat.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/httpx_cat.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/initialize.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/make_form.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/make_headers.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/new_x_ctx.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/open_proxy_tcp_connection.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/open_tcp_connection.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/post_http.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/post_http3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/post_http4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/post_https.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/post_https3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/post_https4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/post_httpx.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/post_httpx3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/post_httpx4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/put_http.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/put_http3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/put_http4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/put_https.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/put_https3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/put_https4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/put_httpx.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/put_httpx3.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/put_httpx4.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/randomize.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/set_cert_and_key.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/set_proxy.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/set_server_cert_and_key.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/ssl_read_CRLF.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/ssl_read_all.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/ssl_read_until.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/ssl_write_CRLF.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/ssl_write_all.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/sslcat.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/tcp_read_CRLF.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/tcp_read_all.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/tcp_read_until.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/tcp_write_CRLF.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/tcp_write_all.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/tcpcat.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/tcpxcat.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/want_X509_lookup.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/want_nothing.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/want_read.al
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/want_write.al

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Net/SSLeay/SSLeay.so
