#
# TODO:
# - descriptions and summaries
# - requires/provides/obsoletes
#
%define		snap 20040709
#
Summary:	debrix
Summary(pl):	debrix
Name:		debrix
Version:	6.7.1
Release:	0.%{snap}.3
Epoch:		0
License:	??
Group:		X11/Xorg
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	ae50d56757530012db8b5e3d394c6a1f
Patch0:		%{name}-fbPictureInit.patch
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
BuildRequires:	renderext
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

%package devel
Summary:	debrix headers
Summary(pl):	Pliki nagłowkowe debrix
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel

%description devel -l pl

%prep
%setup -q -n %{name}
%patch0 -p1

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
%{_includedir}/X11/extensions/*
%{_pkgconfigdir}/debrix.pc
