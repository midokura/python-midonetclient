#!/bin/bash -e

version=`grep ^Version rhel/*.spec | cut -d ' ' -f 5`
package=python-midonet-client

git archive HEAD --prefix=$package-$version/ -o /home/midokura/rpmbuild/SOURCES/$package-$version.tar
gzip /home/midokura/rpmbuild/SOURCES/$package-$version.tar
rpmbuild -ba rhel/$package.spec
