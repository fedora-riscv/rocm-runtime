Name:		rocm-runtime
Version:	1.6.1
Release:	7%{?dist}
Summary:	ROCm Runtime Library

License:	NCSA
URL:		https://github.com/RadeonOpenCompute/ROCm
Source0:	https://github.com/RadeonOpenCompute/ROCR-Runtime/archive/roc-%{version}.tar.gz
Patch0:		0001-Fix-Werror-format-overflow-warning.patch
Patch1:		0001-Prefer-using-memfd_create-for-the-ring-buffer.patch
Patch2:		0001-Fix-build-with-gcc-8.patch

ExclusiveArch: x86_64 aarch64

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	elfutils-libelf-devel
BuildRequires:	hsakmt-devel

%description
ROCm Runtime Library

%package devel
Summary: ROCm Runtime development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: hsakmt-devel

%description devel
ROCm Runtime development files


%prep
%autosetup -n  ROCR-Runtime-roc-%{version} -p1

# Remove the executable bit from a header
chmod a-x src/inc/hsa_ext_amd.h

%build
mkdir build
cd build

%cmake ../src -DCMAKE_BUILD_TYPE=RelWithDebInfo
%make_build


%install
cd build
%make_install

# All files are installed to the prefix /usr/hsa with symlinks back to
# /usr/.  Remove the symlinks and move the files into /usr/

rm %{buildroot}%{_includedir}/hsa
rm %{buildroot}/usr/lib/libhsa-runtime64.so

mv %{buildroot}{/usr/hsa/lib,%{_libdir}}
mv %{buildroot}{/usr/hsa/include/hsa,%{_includedir}}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/libhsa-runtime64.so.1
%{_libdir}/libhsa-runtime64.so.1.0.0

%files devel
%{_includedir}/hsa/
%{_libdir}/libhsa-runtime64.so

%changelog
* Tue Feb 13 2018 Tom Stellard <tstellar@redhat.com> - 1.6.1-7
- Build for aarch64

* Wed Feb 07 2018 Tom Stellard <tstellar@redhat.com> - 1.6.1-6
- Add ExclusiveArch: x86_64

* Tue Feb 06 2018 Tom Stellard <tstellar@redhat.com> - 1.6.1-5
- Take ownership of /usr/include/hsa

* Fri Feb 02 2018 Tom Stellard <tstellar@redhat.com> - 1.6.1-4
- Fix build with gcc 8

* Thu Feb 01 2018 Tom Stellard <tstellar@redhat.com> - 1.6.1-3
- Use version macro in source url

* Mon Jan 29 2018 Tom Stellard <tstellar@redhat.com> - 1.6.1-2
- Fix some rpmlint errors

* Thu Oct 12 2017 Tom Stellard <tstellar@redhat.com> - 1.6.1-1
- Initial Release
