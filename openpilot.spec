%define major	1
%define libAggregation		%mklibname Aggregation %{major}
%define libExtensionSystem	%mklibname ExtensionSystem %{major}
%define libGLC_lib		%mklibname GLC_lib %{major}
%define libQScienceSpinBox	%mklibname QScienceSpinBox %{major}
%define libQtConcurrent		%mklibname QtConcurrent %{major}
%define libQwt			%mklibname Qwt %{major}
%define libUtils		%mklibname Utils %{major}
%define libVersionInfo		%mklibname VersionInfo %{major}
%define libopmapwidget		%mklibname opmapwidget %{major}
%define libsdlgamepad		%mklibname sdlgamepad %{major}
%define devname	%mklibname -d	openpilot

Summary:        Ground Control Station
Name:           OpenPilot
Version:        15.02.01
Release:        1
License:        GPLv2+
Group:          Monitoring
Url:            https://www.openpilot.org/
# git archive --format=tar --prefix OpenPilot-15.02.01/ HEAD | xz -vf > ../OpenPilot-15.02.01.tar.xz
Source0:	https://github.com/openpilot/OpenPilot/archive/OpenPilot-15.02.01.tar.xz
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5SerialPort)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	qt5-linguist-tools

%description
OpenPilot is a next-generation Open Source UAV
autopilot created by the OpenPilot Community.
It is a highly capable platform for multirotors, helicopters,
fixed wing aircraft, and other vehicles.

#=================================
%package -n	%{libAggregation}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libAggregation}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libAggregation}
%{_libdir}/openpilotgcs/libAggregation.so.%{major}*
#=================================

%package -n	%{libExtensionSystem}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libExtensionSystem}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libExtensionSystem}
%{_libdir}/openpilotgcs/libExtensionSystem.so.%{major}*
#=================================

%package -n	%{libGLC_lib}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libGLC_lib}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libGLC_lib}
%{_libdir}/openpilotgcs/libGLC_lib.so.%{major}*
#===============================

%package -n	%{libQScienceSpinBox}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libQScienceSpinBox}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libQScienceSpinBox}
%{_libdir}/openpilotgcs/libQScienceSpinBox.so.%{major}*
#=============================
%package -n	%{libQtConcurrent}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libQtConcurrent}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libQtConcurrent}
%{_libdir}/openpilotgcs/libQtConcurrent.so.%{major}*
#=============================
%package -n	%{libQwt}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libQwt}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libQwt}
%{_libdir}/openpilotgcs/libQwt.so.%{major}*
#============================
%package -n	%{libUtils}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libUtils}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libUtils}
%{_libdir}/openpilotgcs/libUtils.so.%{major}*
#=============================
%package -n	%{libVersionInfo}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libVersionInfo}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libVersionInfo}
%{_libdir}/openpilotgcs/libVersionInfo.so.%{major}*
#=============================
%package -n	%{libopmapwidget}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libopmapwidget}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libopmapwidget}
%{_libdir}/openpilotgcs/libopmapwidget.so.%{major}*
#=============================
%package -n	%{libsdlgamepad}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libsdlgamepad}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{libsdlgamepad}
%{_libdir}/openpilotgcs/libsdlgamepad.so.%{major}*
#=============================
%package -n	%{devname}
Summary:	Library for GCS
Group:		System/Libraries
Requires:	%{libVersionInfo} = %{EVRD}
Requires:	%{libUtils} = %{EVRD}
Requires:	%{libopmapwidget} = %{EVRD}
Requires:	%{libsdlgamepad} = %{EVRD}
Requires:	%{libAggregation} = %{EVRD}
Requires:	%{libExtensionSystem} = %{EVRD}
Requires:	%{libGLC_lib} = %{EVRD}

%description -n	%{devname}
OpenPilot is a next-generation Open Source UAV autopilot
created by the OpenPilot Community.

%files -n	%{devname}
%{_libdir}/openpilotgcs/lib*.so
#=============================

%prep
%setup -q
%apply_patches

%build
%make gcs QMAKE=qmake-qt5 libdir=%{_libdir} CC=%{__cc} CXX=%{__cxx}

%install
%make install DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir}

%files
%{_bindir}/openpilotgcs
%{_bindir}/udp_test
%{_libdir}/openpilotgcs/plugins/%{name}/*.so
%{_libdir}/openpilotgcs/plugins/%{name}/*.pluginspec
%{_datadir}/openpilotgcs/*
%{_datadir}/pixmaps/openpilot.png
%{_datadir}/applications/openpilot.desktop
