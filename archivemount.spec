Summary:	FUSE based filesystem for mounting compressed archives
Name:		archivemount
Version:	0.9.1
Release:	6
Group:		System/Base
License:	LGPLv2+
URL:		http://www.cybernoia.de/software/archivemount.html
# See also https://github.com/cybernoid/archivemount
Source0:	http://www.cybernoia.de/software/archivemount/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(libarchive)
Requires:	fuse2

%description
Archivemount is a piece of glue code between libarchive and FUSE. It can be
used to mount a (possibly compressed) archive (as in .tar.gz or .tar.bz2)
and use it like an ordinary filesystem.

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%files
%doc CHANGELOG COPYING README
%{_bindir}/archivemount
%doc %{_mandir}/*/*
