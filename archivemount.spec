Summary:	FUSE based filesystem for mounting compressed archives
Name:		archivemount
Version:	0.8.3
Release:	1
Group:		System/Base
License:	LGPLv2+
URL:		http://www.cybernoia.de/software/archivemount/
Source0:	http://www.cybernoia.de/software/archivemount/%{name}-%{version}.tar.gz
BuildRequires:	fuse-devel
BuildRequires:	pkgconfig(libarchive)
Requires:	fuse

%description
Archivemount is a piece of glue code between libarchive and FUSE. It can be
used to mount a (possibly compressed) archive (as in .tar.gz or .tar.bz2)
and use it like an ordinary filesystem.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc CHANGELOG COPYING README
%{_bindir}/archivemount
%{_mandir}/*/*
