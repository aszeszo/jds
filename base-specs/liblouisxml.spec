# Copyright 2009, 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
Summary:	Support for braille transciption services for XML documents.
Name:		liblouisxml
Version:	2.1.0
License:	LGPLv3 for library, GPLv3 for binaries
Group:		Libraries
Source: 	http://liblouisxml.googlecode.com/files/%{name}-%{version}.tar.gz

%define python_version 2.6

%description
Provides a braille transcription service for XML documents.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --infodir=%{_infodir} --mandir=%{_mandir} --enable-ucs4
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%changelog
* Wed Nov 03 2010 - Li Yuan <lee.yuan@oracle.com>
- Update description.
* Wed Oct 06 2010 - Brian Cameron
- Initial spec with version 2.1.0.
