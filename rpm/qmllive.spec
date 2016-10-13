Name: qmllive
Version: 0
Release: 1
Summary: Qt QmlLive - live reloader environment for rapid UI development
Group: Development/Tools
License: GPLv3
URL: http://code.qt.io/cgit/qt-apps/qmllive.git
Source: %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Qml)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Qt QmlLive is a system to automatically reload a Qt Quick user interface on every
document save.

%package devel
Summary: Development library for Qt QmlLive
Requires: %{name} = %{version}

%description devel
This package contains the development library for %{name}.

%package example-app
Summary: Example application for demonstration of Qt QmlLive
Requires: %{name} = %{version}

%description example-app
This package contains an example application for demonstration of %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
# Auto-update pkg-config / library version from RPM .spec version
sed -i -e 's#^VERSION = .*$#VERSION = %{version}#' qmllive.pri

# We know we can build certain parts with Qt 5.2
sed -i -e '/^!minQtVersion/s/^/#/' qmllive.pro

%qmake5 'CONFIG+= skip-bench skip-tests' -after QMAKE_RPATHDIR=
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/qmlliveruntime
%{_libdir}/libqmllive.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libqmllive.so
%{_libdir}/pkgconfig/qmllive.pc
%{_includedir}/qmllive/*.h

%files example-app
%defattr(-,root,root,-)
%{_libdir}/qmllive/examples/app
