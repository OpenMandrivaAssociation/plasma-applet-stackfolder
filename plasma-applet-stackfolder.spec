%define doc_version 1.3

Name: plasma-applet-stackfolder
Summary: Browse the stack of folders
Version: 2.4
Release: 8
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.rosalab.ru
Source0: %name-%version.tar.gz
Source1: %name-doc-%{doc_version}.tar.gz
Patch0: %name-configChanged.patch
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-devel

%description
Browse the stack of folders

%files
%_kde_libdir/kde4/plasma_applet_stackfolder.so
%_kde_datadir/kde4/services/plasma-applet-stackfolder.desktop
%_kde_datadir/apps/plasma/packages/org.kde.stackfolder/contents/ui/main.qml
%_kde_datadir/apps/plasma/packages/org.kde.stackfolder/contents/ui/Button.qml
%_kde_datadir/apps/plasma/packages/org.kde.stackfolder/contents/ui/Delegate.qml
%_kde_datadir/apps/plasma/packages/org.kde.stackfolder/contents/ui/ScrollBar.qml
%doc welcome-en.pdf welcome-ru.pdf

%prep
%setup -q
%apply_patches
tar xvf %{SOURCE1}

%build
%cmake_kde4

%make

%install
%makeinstall_std -C build


%changelog
* Thu Dec 06 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:2.4-3
- Fixed plasma core module importing

* Mon Dec 03 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.4-2
- Fixed focus losses after KDE updating to 4.9.4 version

* Sun Dec 02 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.4-1
- Fixed focus losing after klook hiding

* Tue Nov 29 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.3-7
- Updated help documents

* Tue Nov 29 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.3-6
- Added help documents

* Fri Nov 23 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.3-5
- Fixed losing preview
- Fixed memory leaks
- Fixed hiding Klook
- Implemented switching items highlight by mouse

* Fri Oct 26 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.3-3
- Set text color from theme

* Wed Oct 24 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.3-2
- Added shadows for text

* Fri Oct 19 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.3-1
- Fixed plasma resetting after changing folder name
- Fixed escape button parsing for correct closing embedded klook application
- Moved qml contents to the plasma/packages and renamed package to org.kde.stackfolder

* Fri Oct 05 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.2-2
- Fixed icon resizing on the panel

* Fri Aug 31 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.2-1
- Reworked to PopupApplet

* Tue May 29 2012 Dmitry Ashkadov <dmitry.ashkadov@rosalab.ru> 1:0.2.1-23
- Drag and Drop was implemented

* Wed May 02 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-20
- Added folder name to the tooltip

* Sat Apr 28 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-19
- Added sorting by date to download folder

* Thu Apr 26 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-18
- Reworked Klook launching behavior for hovered item

* Tue Apr 24 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-17
- Hid scrollbar for empty folders

* Tue Apr 24 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-16
- Fixed loss of focus

* Mon Apr 23 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-15
- Added scrollbar
- Added Klook launching for hovered item

* Wed Apr 18 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-14
- Fixed bug with loss preview after flicking

* Mon Apr 16 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-12
- Added interaction with Klook
- Fixed preview generating bug

* Mon Apr 02 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-3
- Fixed loss of highlight items

* Thu Mar 29 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-2
- Removed debug outputs

* Mon Mar 26 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:0.2.1-1
- Updated to version 2.0

* Fri Jul 22 2011 Ural Mullabaev <mur@mandriva.org> 1:0.1.9-12
+ Revision: 691070
- Add tooltip

* Tue Jun 28 2011 Ural Mullabaev <mur@mandriva.org> 1:0.1.9-11
+ Revision: 687702
- Added returning to the preset root folder after hiding

* Thu Jun 09 2011 Ural Mullabaev <mur@mandriva.org> 1:0.1.9-10
+ Revision: 683514
- Added window hiding after opening folder by file manager

* Wed Jun 08 2011 Ural Mullabaev <mur@mandriva.org> 1:0.1.9-9
+ Revision: 683214
- Change to the stretchable icon on the panel

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Clean spec file

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.9-8
+ Revision: 667780
- mass rebuild

* Mon Mar 14 2011 Alex Burmashev <burmashev@mandriva.org> 1:0.1.9-7
+ Revision: 644608
- Fixed screen title size bug

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - libjpeg-devel is not needed as buildrequires because already required by kdelibs4

* Fri Mar 04 2011 Alex Burmashev <burmashev@mandriva.org> 1:0.1.9-6
+ Revision: 641604
- imported package plasma-applet-stackfolder


* Fri Jan 21 2011 Ural Mullabaev <ural.mullabaev@rosalab.ru> 0.1.0-1
- First package

