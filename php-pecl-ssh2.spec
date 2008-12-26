%define		_modname	ssh2
%define		_status		beta
Summary:	%{_modname} - bindings for the libssh2 library
Summary(pl.UTF-8):	%{_modname} - dowiązania do biblioteki libssh2
Name:		php-pecl-%{_modname}
Version:	0.11.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	9f5dcd5b92299458389038f7318cbc46
Patch0:		php-pecl-ssh2-libssh2.patch
URL:		http://pecl.php.net/package/ssh2/
BuildRequires:	libssh2-devel >= 0.16
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides bindings to the functions of libssh2 which implements the
SSH2 protocol.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Dostarcza dowiązań do różnych funkcji biblioteki libssh2
implementującej protokół SSH2.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
cd ssh2-%{version}
%patch0 -p0

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
