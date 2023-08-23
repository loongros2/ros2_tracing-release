%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-tracetools-test
Version:        7.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tracetools_test package

License:        Apache 2.0
URL:            https://index.ros.org/p/tracetools_test/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-launch
Requires:       ros-rolling-launch-ros
Requires:       ros-rolling-tracetools-launch
Requires:       ros-rolling-tracetools-read
Requires:       ros-rolling-tracetools-trace
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-mypy
BuildRequires:  ros-rolling-ament-pep257
BuildRequires:  ros-rolling-ament-xmllint
%endif

%description
Utilities for tracing-related tests.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Aug 23 2023 Christophe Bedard <bedard.christophe@gmail.com> - 7.1.0-1
- Autogenerated by Bloom

* Fri Jun 09 2023 Christophe Bedard <bedard.christophe@gmail.com> - 7.0.0-1
- Autogenerated by Bloom

* Thu May 11 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.4.1-1
- Autogenerated by Bloom

* Fri Apr 28 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.4.0-1
- Autogenerated by Bloom

* Tue Apr 18 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.3.0-1
- Autogenerated by Bloom

* Tue Apr 18 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.2.0-1
- Autogenerated by Bloom

* Thu Apr 13 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.1.0-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.0.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Christophe Bedard <bedard.christophe@gmail.com> - 5.1.0-2
- Autogenerated by Bloom

