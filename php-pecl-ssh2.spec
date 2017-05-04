%define		php_name	php%{?php_suffix}
%define		modname	ssh2
Summary:	%{modname} - bindings for the libssh2 library
Summary(pl.UTF-8):	%{modname} - dowiązania do biblioteki libssh2
Name:		%{php_name}-pecl-%{modname}
Version:	0.13
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	e35f8438b3f6177066166c8c1916f44e
Patch0:		bug-73524.patch
URL:		https://pecl.php.net/package/ssh2
BuildRequires:	%{php_name}-devel >= 4:5.0.4
BuildRequires:	libssh2-devel >= 1.2.9
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Provides:	php(%{modname}) = %{version}
Obsoletes:	php-pecl-ssh2 < 0.12-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides bindings to the functions of libssh2 which implements the
SSH2 protocol.

%description -l pl.UTF-8
Dostarcza dowiązań do różnych funkcji biblioteki libssh2
implementującej protokół SSH2.

%prep
%setup -qc
mv %{modname}-%{version}/* .
%patch0 -p1

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
