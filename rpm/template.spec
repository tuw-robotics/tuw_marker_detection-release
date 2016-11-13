Name:           ros-kinetic-tuw-ellipses
Version:        0.0.7
Release:        0%{?dist}
Summary:        ROS tuw_ellipses package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-geometry
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-marker-msgs
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-geometry
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-marker-msgs
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-tf

%description
The tuw_ellipses package contains a computer vision library which is able to
detect ellipses within images. The package is able to estimate the pose of the
circle related to the ellipse the circle diameter as well as the camera
parameter are known. A dynamic reconfigure interface allows the user to tune the
parameter of the system to ones needs. But be aware that the pose of a projected
circle within a image (ellipse) has two solutions and only one is published as
TF.

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
* Sun Nov 13 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.0.7-0
- Autogenerated by Bloom

* Sat Nov 12 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.0.6-0
- Autogenerated by Bloom

* Sat Nov 12 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.0.5-1
- Autogenerated by Bloom

* Sat Nov 12 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.0.5-0
- Autogenerated by Bloom

* Fri Nov 11 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.0.4-0
- Autogenerated by Bloom

* Mon Nov 07 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.0.2-0
- Autogenerated by Bloom

