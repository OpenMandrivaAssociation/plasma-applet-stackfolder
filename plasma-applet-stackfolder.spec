Name:		plasma-applet-stackfolder
Summary:	Browse the stack of folders
Version:	0.2.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://www.rosalab.ru
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel

%description
Browse the stack of folders

%files
%{_kde_libdir}/kde4/plasma_applet_stackfolder.so
%{_kde_datadir}/kde4/services/plasma-applet-stackfolder.desktop

%prep
%setup -q

%build
%cmake_kde4

%make

%install
%makeinstall_std -C build
