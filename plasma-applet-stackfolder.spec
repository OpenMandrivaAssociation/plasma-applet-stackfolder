Name: plasma-applet-stackfolder
Summary: Browse the stack of folders
Version: 0.1.9
Release: %mkrel 8
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.rosalab.ru
Source: %name-%version.tar.bz2
BuildRequires: kdelibs4-devel
BuildRequires: libjpeg-devel

BuildRoot: %_tmppath/%name-%version-%release-root

%description
Browse the stack of folders

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_stackfolder.so
%_kde_datadir/kde4/services/plasma-applet-stackfolder.desktop

%prep
%setup -q

%build
%cmake_kde4

%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

