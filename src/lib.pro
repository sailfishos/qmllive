include(../qmllive.pri)

TEMPLATE = lib
TARGET = qmllive

DESTDIR = $${BUILD_DIR}/lib
DEFINES += QMLLIVE_LIBRARY

macx*: QMAKE_SONAME_PREFIX = @rpath

SOURCES += \
    qmllive.cpp

public_headers += \
    qmllive_global.h \
    qmllive.h

include(src.pri)

win32: target.path = $${PREFIX}/bin
else: target.path = $$[QT_INSTALL_LIBS]
INSTALLS += target

headers.files = $$public_headers
headers.path = $${PREFIX}/include/qmllive
INSTALLS += headers

# This should be passed on qmake command line
isEmpty(PKGCONFIG_LIB) {
    PKGCONFIG_LIB = lib
    message("PKGCONFIG_LIB is unset, assuming $$PKGCONFIG_LIB")
}

!win32 {
    CONFIG += create_pc create_prl no_install_prl
    QMAKE_PKGCONFIG_NAME = qmllive
    QMAKE_PKGCONFIG_DESCRIPTION = Qt QmlLive Library
    QMAKE_PKGCONFIG_PREFIX = $$PREFIX
    QMAKE_PKGCONFIG_LIBDIR = ${prefix}/$$PKGCONFIG_LIB
    QMAKE_PKGCONFIG_INCDIR = ${prefix}/include/qmllive
    QMAKE_PKGCONFIG_DESTDIR = pkgconfig
}
