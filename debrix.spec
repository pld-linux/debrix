#
%define		snap 20040627
#
Summary:	debrix
Summary(pl):	debrix
Name:		debrix
Version:	6.7.1
Release:	0.1
Epoch:		0
License:	??
Group:		X11/Xorg
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	-
# not really debrix URL, but there is no other...
URL:		http://xserver.freedesktop.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	compositeext
BuildRequires:	damageext
BuildRequires:	fixesext
BuildRequires:	libtool
BuildRequires:	libXau-devel
BuildRequires:	libXdmcp-devel
BuildRequires:	libXfont-devel
BuildRequires:	libXtrans-devel
BuildRequires:	panoramixext
BuildRequires:	randrext
BuildRequires:	render
BuildRequires:	resourceext
BuildRequires:	xextensions
BuildRequires:	xkbfile-devel
BuildRequires:	xproto
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--enable-dri \
	--enable-xtrap

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/xorg

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/xorg
%{_pkgconfigdir}/debrix.pc
