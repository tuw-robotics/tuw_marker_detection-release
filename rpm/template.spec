Name:           ros-kinetic-tuw-marker-pose-estimation
Version:        0.0.6
Release:        0%{?dist}
Summary:        ROS tuw_marker_pose_estimation package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-geometry
Requires:       ros-kinetic-marker-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-geometry
BuildRequires:  ros-kinetic-marker-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf

%description
This node does pose estimation for detected fiducials
(marker_msgs/FiducialDetection.msg)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Nov 12 2016 Lukas Pfeifhofer <lukas.pfeifhofer@devlabs.pro> - 0.0.6-0
- Autogenerated by Bloom

* Sat Nov 12 2016 Lukas Pfeifhofer <lukas.pfeifhofer@devlabs.pro> - 0.0.5-1
- Autogenerated by Bloom

* Sat Nov 12 2016 Lukas Pfeifhofer <lukas.pfeifhofer@devlabs.pro> - 0.0.5-0
- Autogenerated by Bloom

* Fri Nov 11 2016 Lukas Pfeifhofer <lukas.pfeifhofer@devlabs.pro> - 0.0.4-0
- Autogenerated by Bloom

* Mon Nov 07 2016 Lukas Pfeifhofer <lukas.pfeifhofer@devlabs.pro> - 0.0.2-0
- Autogenerated by Bloom

