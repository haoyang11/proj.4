# Fre Jan 11 15:39:33 CET 2002, Silke
%define PACKAGE_NAME PROJ
%define PACKAGE_VERSION 4.4.5
%define PACKAGE_URL http://www.remotesensing.org/proj/
%define _prefix /usr

Summary: Cartographic projection software
Name: %PACKAGE_NAME
Version: %PACKAGE_VERSION
Release: 1
Source0: proj-4.4.5.tar.gz
Copyright: MIT License, Copyright (c) 2000, Frank Warmerdam
Group: Applications/GIS
Vendor: Intevation GmbH <http://intevation.net>
Distribution: FreeGIS CD

BuildRoot: %{_builddir}/%{name}-root
Prefix: %{_prefix}

Conflicts: PROJ.4

%description
This package offers commandline tools and a library for performing respective
forward and inverse transformation of cartographic data to or from cartesian 
data with a wide range of selectable projection functions. 

%prep
%setup -D -n proj-4.4.5
%configure

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf %{_builddir}/proj-4.4.5
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*
%{_bindir}/*
%{_includedir}/*
%{_datadir}/proj/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%doc AUTHORS COPYING ChangeLog NEWS README