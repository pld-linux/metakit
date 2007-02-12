Summary:	Embeddable database
Summary(pl.UTF-8):   Baza danych
Name:		metakit
Version:	2.4.9.5
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://www.equi4.com/pub/mk/%{name}-%{version}.tar.gz
# Source0-md5:	37ba351462dad0d7f01394e04c173ce3
URL:		http://www.equi4.com/metakit.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	python-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MetaKit is an embeddable database which runs on Unix, Windows,
Macintosh, and other platforms. It lets you build applications which
store their data efficiently, in a portable way, and which will not
need a complex runtime installation. In terms of the data model,
MetaKit takes the middle ground between RDBMS, OODBMS, and flat-file
databases - yet it is quite different from each of them.

%description -l pl.UTF-8
MetaKit to baza danych pracująca na platformach Unix, Windows,
Macintosh oraz innych. Pozwala ona na tworzenie aplikacji, które
zapisują dane efektywnie w sposób łatwy do przenoszenia między
platformami i które nie wymagają skomplikowanej instalacji. MetaKit
używając określeń z dziedziny baz danych znajduje się pomiędzy RDBMS,
OODBMS i bazami opartymi na płaskich-plikach.

%package devel
Summary:	Header files and development documentation for %{name}
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	metakit-static

%description devel
Header files and development documentation for %{name}.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do %{name}.

%package -n python-metakit
Summary:	Python modules for metakit
Summary(pl.UTF-8):   Moduły Pythona dla pakietu metakit
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-metakit
Python modules for metakit.

%description -n python-metakit -l pl.UTF-8
Moduły Pythona dla pakietu metakit.

%package -n tcl-metakit
Summary:	Tcl modules for metakit
Summary(pl.UTF-8):   Moduły Tcl-a dla pakietu metakit
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description -n tcl-metakit
Tcl modules for metakit.

%description -n tcl-metakit -l pl.UTF-8
Moduły Tcl-a dla pakietu metakit.

%prep
%setup -q

# remove CVS control files
find -name CVS -print0 | xargs -0 rm -rf

%build
cd unix
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-tcl \
	--with-python \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{py_sitedir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	-C unix \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc CHANGES Metakit.html doc
%{_includedir}/*.h
%{_includedir}/*.inl
%{_examplesdir}/%{name}-%{version}

%files -n python-metakit
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/Mk4py.so
%{py_sitedir}/metakit.py

%files -n tcl-metakit
%defattr(644,root,root,755)
%dir %{_libdir}/tcl8.4/Mk4tcl
%attr(755,root,root) %{_libdir}/tcl8.4/Mk4tcl/Mk4tcl.so
%{_libdir}/tcl8.4/Mk4tcl/pkgIndex.tcl
