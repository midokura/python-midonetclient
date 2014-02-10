#!/bin/bash
#
# python-midonetclient packaging script for RHEL and DEBIAN.
#
# The build is self-sufficient and able to build from a fresh checkout,
# independently from source control. The script will not perform any validation
# on the correctness of the versions, so the user is responsible to ensure that
# the contents of the package match the correct release version.

BUILD_DIR=build
NOW=`date -u +"%a, %d %b %Y %T %z"` # RFC 5322
YEAR=`date +%Y`
USER="Midokura"
USER_E="info@midokura.com"

usage() {
    echo ""
    echo "Python-midonetclient packaging script"
    echo "Usage: package.sh [deb|rhel] version (rpm_release_number)"
    echo "Where:"
    echo " - version: in format X.Y.Z for final, X.Y.Z-rcW for rc or -hfW for hotfix"
    echo " - rpm_release_number: optional, allows overriding the release number
   in RPM, if unsure, leave empty"
    echo ""
}

# generates files for deb packaging, creating a changelog file in the
# build directory.
gen_deb() {
    echo "Generating version-dependent files"
    VERSION="$1"
    DEB_DISTRIBUTION="precise"
    echo "Generating debian changelog for $VERSION"
    echo "python-midonetclient ($VERSION) $DEB_DISTRIBUTION; urgency=low

  * $VERSION

 -- $USER <$USER_E>  $NOW" > debian/changelog
}

# generates files for rhel packaging, creating the copyright file in the
# build directory.
gen_rhel() {
    echo "Generating version-dependent files $@"
    echo "This work was packaged for RPM by:

    $USER <$USER_E> on $NOW

It was downloaded from:

    https://github.com/midokura/python-midonetclient

Upstream Author(s):

    $USER <$USER_E>

Copyright:

    Copyright (C) $YEAR Midokura KK

License:

    This work is proprietary software. All rights reserved.

The RPM packaging is:

    Copyright (C) $YEAR Midokura KK
" > $BUILD_DIR/rhel/copyright
}

# packages DEBs, leaving all build-generated files and packages in
# $BUILD_DIR/debian
# usage: package_deb <version> 
package_deb() {

    version=`echo $1 | sed -e "s/-/~/"` # X.Y.Z-rc5 -> X.Y.Z~rc5
    stage "Creating DEBIAN package for version: $version"

    if [ "$1" == "" ]
    then
        echo "DEBIAN build requires a release number"
        exit -1
    fi

    gen_deb $version
 
    echo "Generating DEBIAN packages"
     
    dpkg-buildpackage -rfakeroot -b -us -uc
    destdir="$BUILD_DIR/debian/"
    mv ../*_${version}_*.deb $destdir
    mv ../*_${version}_*.changes $destdir

    echo "DEBIAN packages ready at $destdir"
}

# packages RPMs, leaves all generated files in # $BUILD_DIR/rhel/
# usage: package_rhel <version> (sub_version)
# where:
# - version: X.Y.Z for a final, X.Y.Z-rcW for a pre-release
# - release: typically 0.1 for prerelease, 1.0 for release, optional and
#   will be inferred from the version if not present
package_rhel() {

    stage "Creating RHEL packages, version: $1, release: $2"

    version=$1
    release=$2

    if [ "$version" == "" ]
    then
        echo "ERROR: Missing version parameter"
        exit -1
    fi

    # suffix is the -rcX or -hfX
    suffix=`echo $version | sed -e 's/^.*-//'`
    if [ "$release" == "" ]
    then
	if [ "$suffix" == "" ]
	then
	    release="1.0" # a final
   	else
	    release="0.1.$suffix" # a pre release
	fi
    fi

    # remove pre release tag
    rpm_ver=`echo $version | sed -e 's/-.*$//'` 
    gen_rhel $rpm_ver $release

    # prerelease: X.Y.Z-0.1.prerelease-tag (e.g.: 1.2.3-0.1.rc4)
    # final: X.Y.Z-1.0
    if [ "$suffix" -ne "" ]
    then
    	rpm_ver="$rpm_ver.$suffix"
    fi

    echo "Generating RHEL packages for version: $rpm_ver"

    rpm_ver=$rpm_ver.$suffix

    DATE=`date -u +"%a %b %d %Y"`
    TAR=~/rpmbuild/SOURCES/python-midonetclient-$rpm_ver.tar
    mkdir -p $BUILD_DIR/rhel/python-midonetclient-$rpm_ver
    cp -r LICENSE* NEWS README rhel doc src setup.* $BUILD_DIR/rhel/python-midonetclient-$rpm_ver
    mv $BUILD_DIR/rhel/copyright $BUILD_DIR/rhel/python-midonetclient-$rpm_ver/rhel
    pushd $BUILD_DIR/rhel > /dev/null
    tar -cf $TAR python-midonetclient-$rpm_ver
    popd
    gzip -f $TAR
    rpmbuild --quiet --define "version $rpm_ver" --define "release $release" --define "now $DATE" -ba rhel/python-midonetclient.spec
    find ~/rpmbuild/RPMS/ | grep python-midonetclient-$rpm_ver | grep rpm$ | while read pkg ; do
        cp $pkg $BUILD_DIR/rhel
    done

    echo "RHEL packages are ready at $BUILD_DIR/rhel"
}

# Prepares build directories
prepare() {
    echo "Creating build directories"
    mkdir -p $BUILD_DIR/rhel
    mkdir -p $BUILD_DIR/debian
}

echo "Welcome to Midokura's python-midonetclient packaging experience"

if [ "$#" -lt 2 ]
then
    echo "ERROR: Insufficient parameters"
    usage
    exit -1
fi

prepare

COMMAND=$1
shift

set -e
case $COMMAND in
  deb) package_deb $@ ;;
  rhel) package_rhel $@ ;;
  *) usage ;;
esac
