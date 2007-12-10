Summary: Front-end for making snapshots of a set of directories
Name:    timevault
Version: 0.7.5
Release: %mkrel 1
Source:  %name-%version.tar.bz2
# make it using existing macros:
Patch0:   timevault-init-mdv.patch
# make it chkconfig aware:
Patch1:   timevault-init-chkconfig.patch
URL:     https://wiki.ubuntu.com/TimeVault
License: GPL
Group:   System/Configuration/Other
BuildRoot: %{_tmppath}/gnome-python-root
BuildRequires: python-devel >= 2.2
BuildRequires: gnome-common intltool
BuildRequires: gnome-python-devel nautilus-python pygtk2.0-devel python-gnome-devel python-notify python-dbus dbus-devel
BuildRequires: autoconf automake make
Requires: pygtk2.0
Requires(post,preun): rpm-helper

%description
TimeVault is a simple front-end for making snapshots of a set of directories.
Snapshots are a copy of a directory structure or file at a certain point in
time. Restore functionality is integrated into Nautilus - previous versions of
a file or directory that has a snapshot can be accessed by examining the
properties and selecting the 'Previous Versions' tab. 

Snapshots are protected from accidental deletion or modification since they are
read-only by default. The super-user can delete intermediate snapshots to save
space, but files and directories that existed before or after the deletion will
still be accessible. 

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
[[ -x ./configure ]] || ./autogen.sh
%configure2_5x --libdir=%_libdir
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%post
%_post_service %name

%preun
%_preun_service %name

%files
%defattr(-,root,root,755)
%_bindir/*
%_datadir/applications/timevault.desktop
%_datadir/timevault
%config(noreplace) /etc/dbus-1/system.d/timevault.conf
/etc/init.d/timevault
%config(noreplace) /etc/logrotate.d/timevault.logrotate
%_iconsdir/hicolor/14x14/apps/timevault.png
%_iconsdir/hicolor/22x22/apps/timevault.png
%_iconsdir/hicolor/32x32/apps/timevault.png
%_iconsdir/hicolor/scalable/apps/timevault.svg
%py_platsitedir/TimeVault
/usr/lib/nautilus/extensions-1.0/python/timevault-nautilus.py


