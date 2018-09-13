Name:           ros-melodic-pr2-power-board
Version:        1.1.6
Release:        0%{?dist}
Summary:        ROS pr2_power_board package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/pr2_power_board
Source0:        %{name}-%{version}.tar.gz

Requires:       log4cxx-devel
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-pr2-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
BuildRequires:  log4cxx-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-pr2-msgs
BuildRequires:  ros-melodic-roscpp

%description
This provides a ROS node for the PR2 Power Board.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Sep 13 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.1.6-0
- Autogenerated by Bloom

