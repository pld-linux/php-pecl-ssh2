%define		modname	ssh2
%define		status	beta
Summary:	%{modname} - bindings for the libssh2 library
Summary(pl.UTF-8):	%{modname} - dowiązania do biblioteki libssh2
Name:		php-pecl-%{modname}
Version:	0.11.0
Release:	5
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	9f5dcd5b92299458389038f7318cbc46
Patch0:		php-pecl-ssh2-libssh2.patch
Patch1:		branch.diff
URL:		http://pecl.php.net/package/ssh2/
BuildRequires:	libssh2-devel >= 0.16
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	php-devel >= 4:5.0.4
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides bindings to the functions of libssh2 which implements the
SSH2 protocol.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Dostarcza dowiązań do różnych funkcji biblioteki libssh2
implementującej protokół SSH2.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .
%patch0 -p0
%patch1 -p0

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
