%define name vino
%define version 2.19.90
%define release %mkrel 1

Summary: GNOME VNC server and client
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/vino/%{name}-%{version}.tar.bz2
License: GPL
Group: Networking/Remote access
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libgnutls-devel
BuildRequires: perl-XML-Parser
BuildRequires: libxtst-devel
BuildRequires: libxdamage-devel
BuildRequires: desktop-file-utils

%description
The package contains an integrated GNOME VNC server.

%prep
%setup -q

%build
#gw remove session support once we move to gnome-session 2.8
%configure2_5x --enable-session-support --enable-avahi
%make

%install
rm -rf $RPM_BUILD_ROOT
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
%find_lang %name --with-gnome
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%clean
rm -rf $RPM_BUILD_ROOT

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/vino-server.schemas > /dev/null

%preun
if [ "$1" = "0" ] ; then
 export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
 gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/vino-server.schemas > /dev/null
fi

%files -f %name.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog docs/remote-desktop.txt docs/TODO
%_sysconfdir/gconf/schemas/vino-server.schemas
%_bindir/vino-preferences
%_bindir/vino-session
%_libdir/bonobo/servers/GNOME_RemoteDesktop.server
%_libexecdir/vino-server
%_datadir/vino
%_datadir/applications/vino-preferences.desktop
%_datadir/icons/hicolor/48x48/apps/*
