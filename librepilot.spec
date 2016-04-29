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
Name:           LibrePilot
Version:        15.09
Release:        1
License:        GPLv2+
Group:          Monitoring
Url:            http://www.librepilot.org/
Source0:	http://download.librepilot.org/source/%{name}-%{version}.tar.gz
Source1:	http://download.librepilot.org/firmware/%{name}-%{version}_firmware.tar.gz
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5SerialPort)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	qmake5
BuildRequires:	curl
BuildRequires:	openssl
BuildRequires:	qt5-linguist-tools
Provides:	openpilot = %{EVRD}

%description
LibrePilot is a next-generation Open Source UAV
autopilot created by the LibrePilot Community.
It is a highly capable platform for multirotors, helicopters,
fixed wing aircraft, and other vehicles.

#=================================
%package -n	%{libAggregation}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libAggregation}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libAggregation}
%{_libdir}/librepilot-gcs/libAggregation.so.%{major}*
#=================================

%package -n	%{libExtensionSystem}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libExtensionSystem}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libExtensionSystem}
%{_libdir}/librepilot-gcs/libExtensionSystem.so.%{major}*
#=================================

%package -n	%{libGLC_lib}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libGLC_lib}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libGLC_lib}
%{_libdir}/librepilot-gcs/libGLC_lib.so.%{major}*
#===============================

%package -n	%{libQScienceSpinBox}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libQScienceSpinBox}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libQScienceSpinBox}
%{_libdir}/librepilot-gcs/libQScienceSpinBox.so.%{major}*
#=============================
%package -n	%{libQtConcurrent}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libQtConcurrent}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libQtConcurrent}
%{_libdir}/librepilot-gcs/libQtConcurrent.so.%{major}*
#=============================
%package -n	%{libQwt}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libQwt}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libQwt}
%{_libdir}/librepilot-gcs/libQwt.so.%{major}*
#============================
%package -n	%{libUtils}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libUtils}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libUtils}
%{_libdir}/librepilot-gcs/libUtils.so.%{major}*
#=============================
%package -n	%{libVersionInfo}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libVersionInfo}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libVersionInfo}
%{_libdir}/librepilot-gcs/libVersionInfo.so.%{major}*
#=============================
%package -n	%{libopmapwidget}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libopmapwidget}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libopmapwidget}
%{_libdir}/librepilot-gcs/libopmapwidget.so.%{major}*
#=============================
%package -n	%{libsdlgamepad}
Summary:	Library for GCS
Group:		System/Libraries

%description -n	%{libsdlgamepad}
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{libsdlgamepad}
%{_libdir}/librepilot-gcs/libsdlgamepad.so.%{major}*
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
LibrePilot is a next-generation Open Source UAV autopilot
created by the LibrePilot Community.

%files -n	%{devname}
%{_libdir}/librepilot-gcs/lib*.so
#=============================

%prep
%setup -qn %{name} -a 1
#apply_patches
#sed -i -e 's!isnan!std::isnan!g' -e 's!isinf!std::isinf!g' \
# flight/libraries/math/mathmisc.h \
# flight/modules/Attitude/attitude.c \
# flight/modules/Sensors/sensors.c \
# flight/modules/StateEstimation/filtercf.c \
# flight/modules/StateEstimation/filterekf.c \
# flight/modules/StateEstimation/filtermag.c \
# flight/pios/inc/pios_math.h \
# flight/tests/math/unittest.cpp \
# ground/gcs/src/plugins/hitl/il2simulator.cpp

%build

make config_new                             \
    enable-udev-rules=yes                   \
    libbasename=%{_lib}                     \
    prefix=%{_prefix}                       \
    QMAKE=qmake-qt5                         \
    udevrulesdir=%{_udevrulesdir}           \
    WITH_PREBUILT_FW=$(pwd)/firmware

make %_smp_mflags opfw_resource gcs

%install
%makeinstall_std

%files
%{_bindir}/librepilot-gcs
%{_udevrulesdir}/45-librepilot.rules
%{_datadir}/applications/librepilot.desktop
%{_datadir}/librepilot-gcs/*
%{_datadir}/pixmaps/librepilot.png
