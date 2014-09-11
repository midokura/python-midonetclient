#!/bin/bash
#
# This script generates RPM and debian packages.
#
# Usage: ./package.sh [VERSION_STRING]
#
#   VERSION_STRING: version string for deb and RPM packaes.
#                   If ommited (recommended), it defaults to
#                   `git describe --tag | sed 's/^v//'`
#
# Build ependencies:
#   In short, do the following on Ubuntu based distribution to install
#   build dependencies.
#
#   $ sudo apt-get install -y rubygems rpm ruby-ronn && sudo gem install fpm
#
#   Here's list of dependencies:
#
#   * fpm (https://github.com/jordansissel/fpm):
#       This enables us to produce both RPM and debian packages easily
#       withough requiring details about their packaging systems
#
#   * rpm: of course rpmbuild is needed to produce RPM packages
#
#   * ronn: a tool to produce man pages from markdown

set -e

# Get version number from command line or defaults to use git describe
pkgver=$1
if [ "$pkgver" == "" ]; then
    pkgver=$(git describe --tag | sed 's/^v//')
fi
echo "Packaging with version number $pkgver"

## Common args for rpm and deb
FPM_BASE_ARGS=$(cat <<EOF
--name 'python-midonetclient' \
--architecture 'noarch' \
--license '2014, Midokura' \
--vendor 'Midokura' \
--maintainer "Midokura" \
--url 'http://midokura.com' \
--description 'Python client library for MidoNet API' \
-d 'python-webob' -d 'python-eventlet' -d 'python-httplib2' \
-s dir \
--version $pkgver
EOF
)

function clean() {
    find . -name "*.pyc" -exec rm {} \;
    rm -f doc/*.{gz,.1}
    rm -rf build
}

function build_man_pages() {
    ronn --roff doc/*.ronn 2> /dev/null
    gzip -f doc/*.1
}

function package_rpm() {
    RPM_BUILD_DIR=build/rpm/
    mkdir -p  $RPM_BUILD_DIR/usr/lib/python2.6/site-packages/
    mkdir -p  $RPM_BUILD_DIR/usr/bin/
    mkdir -p  $RPM_BUILD_DIR/usr/share/man/man1

    cp -r  src/midonetclient $RPM_BUILD_DIR/usr/lib/python2.6/site-packages/
    cp src/bin/midonet-cli $RPM_BUILD_DIR/usr/bin/
    cp doc/*.gz $RPM_BUILD_DIR/usr/share/man/man1/
    RPM_ARGS="$RPM_ARGS -C build/rpm"
    RPM_ARGS="$RPM_ARGS --provides python2.6-midonetclient"
    RPM_ARGS="$RPM_ARGS -d 'python >= 2.6'"
    RPM_ARGS="$RPM_ARGS --epoch 1"
    eval fpm $FPM_BASE_ARGS $RPM_ARGS -t rpm .
}

function package_deb() {
    DEB_BUILD_DIR=build/deb
    mkdir -p  $DEB_BUILD_DIR/usr/lib/python2.7/dist-packages
    mkdir -p  $DEB_BUILD_DIR/usr/bin/
    mkdir -p  $DEB_BUILD_DIR/usr/share/man/man1/

    cp -r  src/midonetclient $DEB_BUILD_DIR/usr/lib/python2.7/dist-packages
    cp src/bin/midonet-cli $DEB_BUILD_DIR/usr/bin/
    cp doc/*.gz $DEB_BUILD_DIR/usr/share/man/man1/

    DEB_ARGS="$DEB_ARGS -C build/deb"
    DEB_ARGS="$DEB_ARGS --provides python2.7-midonetclient"
    DEB_ARGS="$DEB_ARGS --deb-priority optional"
    eval fpm $FPM_BASE_ARGS $DEB_ARGS -t deb .
}

# Main
clean
build_man_pages
package_rpm
package_deb
