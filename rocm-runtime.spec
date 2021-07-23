Name:		rocm-runtime
Version:	3.9.0
Release:	2%{?dist}
Summary:	ROCm Runtime Library

License:	NCSA
URL:		https://github.com/RadeonOpenCompute/ROCm
Source0:	https://github.com/RadeonOpenCompute/ROCR-Runtime/archive/rocm-%{version}.tar.gz

Patch0:		0001-fix-CMake-target-paths.patch
Patch1:		0002-fix-link-time-ordering-condition.patch

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
Requires: hsakmt(rocm) = %{version}

%description devel
ROCm Runtime development files


%prep
%autosetup -n  ROCR-Runtime-rocm-%{version} -p1

# Remove the executable bit from a header
chmod a-x src/inc/hsa_ext_amd.h

%build
mkdir build
cd build

# TODO: Image support needs the ROCM-device-libs as dependencies
%cmake ../src -DIMAGE_SUPPORT=OFF -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build


%install
cd build
%cmake_install

rm -rf %{buildroot}/usr/hsa

mv %{buildroot}{/usr/lib/cmake,%{_libdir}}

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/libhsa-runtime64.so.1
%{_libdir}/libhsa-runtime64.so.1.2.0

%files devel
%{_includedir}/hsa/
%{_libdir}/libhsa-runtime64.so
%{_libdir}/cmake/hsa-runtime64/

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Philipp Knechtges <philipp-dev@knechtges.com> - 3.9.0-0
- Version 3.9.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Tom Stellard <tstellar@redhat.com> - 3.5.0-1
- ROCm 3.5.0 Release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Tom Stellard <tstellar@redhat.com> - 2.0.0-3
- Add endian detection for AArch64

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Tom Stellard <tstellar@redhat.com> - 2.0.0-1
- ROCm 2.0.0 Release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
