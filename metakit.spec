Summary:	Embeddable database
Summary(pl):	Baza danych
Name:		metakit
Version:	2.4.9.2
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://www.equi4.com/pub/mk/%{name}-%{version}.tar.gz
# Source0-md5:	d436a49baed1a31d1ef01ea537e4ba63
Patch0:		%{name}-no_static.patch
URL:		http://www.equi4.com/metakit/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MetaKit is an embeddable database which runs on Unix, Windows,
Macintosh, and other platforms. It lets you build applications which
store their data efficiently, in a portable way, and which will not
need a complex runtime installation. In terms of the data model,
MetaKit takes the middle ground between RDBMS, OODBMS, and flat-file
databases - yet it is quite different from each of them.

%description -l pl
MetaKit to baza danych pracuj±ca na platformach Unix, Windows,
Macintosh oraz innych. Pozwala ona na tworzenie aplikacji, które
zapisuj± dane efektywnie w sposób ³atwy do przenoszenia miêdzy
platformami i które nie wymagaj± skomplikowanej instalacji. MetaKit
u¿ywaj±c okre¶leñ z dziedziny baz danych znajduje siê pomiêdzy RDBMS,
OODBMS i bazami opartymi na p³askich-plikach.

%package devel
Summary:	Header files and development documentation for %{name}
Summary(pl):	Pliki nag³ówkowe i dokumentacja do %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for %{name}.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do %{name}.

%package static
Summary:	%{name} static library
Summary(pl):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
%{name} static library.

%description static -l pl
Biblioteka statyczna %{name}.

%prep
%setup -q
%patch0 -p1

%build
cd unix
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cd unix

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd ..
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README WHATSNEW
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc CHANGES MetaKit.html doc
%{_libdir}/*.la
%{_includedir}/*.h
%{_includedir}/*.inl
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
