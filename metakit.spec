Summary:	Embeddable database
Summary(pl):	Baza danych
Name:		metakit
Version:	2.01
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.equi4.com/pub/mk/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-debian.patch
URL:		http://www.equi4.com/metakit/
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
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
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for %{name}.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do %{name}.

%package static
Summary:	%{name} static library
Summary(pl):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
%{name} static library.

%description -l pl static
Biblioteka statyczna %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd unix
libtoolize --copy --force
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}
cd unix

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd .. && gzip -9nf README CHAN*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc READ*.gz
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc CHA*.gz
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*.h
%{_includedir}/*.inl

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
