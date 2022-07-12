## Installing CRIU from source code

Once CRIU is built one can easily setup the complete CRIU package
(which includes executable itself, CRIT tool, libraries, manual
and etc) simply typing

    make install

this command accepts the following variables:

 * **DESTDIR**, to specify global root where all components will be placed under (empty by default);
 * **PREFIX**, to specify additional prefix for path of every component installed (`/usr/local` by default);
 * **BINDIR**, to specify where to put CRIT tool (`$(PREFIX)/bin` by default);
 * **SBINDIR**, to specify where to put CRIU executable (`$(PREFIX)/sbin` by default);
 * **MANDIR**, to specify directory for manual pages (`$(PREFIX)/share/man` by default);
 * **LIBDIR**, to specify directory where to put libraries (guess the correct path  by default).

Thus one can type

    make DESTDIR=/some/new/place install

and get everything installed under `/some/new/place`.

It is recommended to use the `DESTDIR` and `PREFIX` variables together, especially since the latter defaults to
`/usr/local`, as in

```
make install DESTDIR=/some/new/place PREFIX=
```

## Uninstalling CRIU

To clean up previously installed CRIU instance one can type

    make uninstall

and everything should be removed. Note though that if some variable (**DESTDIR**, **BINDIR**
and such) has been used during installation procedure, the same *must* be passed with
uninstall action.


## Common requirements

Make sure that all packages are installed be compiling:
gcc libprotobuf-dev libprotobuf-c0-dev protobuf-c-compiler protobuf-compiler python-protobuf
libnl-3-dev libnet-dev pkg-config libcap-dev python-ipaddress libbsd-dev libaio-dev asciidoc

If a package was installed after a failed compilation, use "make mrproper-top" to clean the repos.

Additional packages maybe needed, please refer to: https://criu.org/Installation

Moreover, it might be preferable to actually select which Python version (2 or 3) the installed Python tools (e.g.,
`crit`) are meant to use.
This can be forced by selected the corresponding Python interpreter during building and installing by setting the
`PYTHON` variable, e.g. for choosing Python 3:

```
make install PYTHON=python3
```

This is possible because the Make variable `PYTHON` can be overidden as is currently defined in the included Makefile
`scripts/nmk/scripts/tools.mk`. Make sure you adjust the relevant packages appropriately (e.g., install
`python3-protobuf` instead of `python-protobuf`).

## Install CRIU-HET

criu-het is installed at same time as criu. However, for criu-het to work correctly, additional
packages needs to be installed: python-six and pwntools. Both of which are python scripts.

