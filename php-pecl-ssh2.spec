%define		_modname	ssh2
%define		_status		beta

Summary:	%{_modname} - bindings for the libssh2 library
Summary(pl):	%{_modname} - dowi±zania do biblioteki libssh2
Name:		php-pecl-%{_modname}
Version:	0.5
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	1f147612d193af45c163614e24e716b5
URL:		http://pecl.php.net/package/ssh2/
BuildRequires:	libssh2-devel >= 0.5
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
Provides bindings to the functions of libssh2 which implements the
SSH2 protocol.

In PECL status of this extension is: %{_status}.

%description -l pl
Dostarcza dowi±zañ do ró¿nych funkcji biblioteki libssh2
implementuj±cej protokó³ SSH2.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
