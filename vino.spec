%define name vino
%define version 2.32.2
%define release %mkrel 2

Summary: GNOME VNC server and client
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/vino/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Networking/Remote access
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libice-devel
BuildRequires: libsm-devel
BuildRequires: libx11-devel
BuildRequires: libxdamage-devel
BuildRequires: libxext-devel
BuildRequires: libxfixes-devel
BuildRequires: libxtst-devel
BuildRequires: gnutls-devel
BuildRequires: avahi-glib-devel
BuildRequires: avahi-client-devel
BuildRequires: libgcrypt-devel
BuildRequires: libsoup-devel
BuildRequires: libnotify-devel
BuildRequires: unique-devel
BuildRequires: gtk+2-devel
BuildRequires: jpeg-devel
BuildRequires: intltool
BuildRequires: dbus-glib-devel
BuildRequires: libtelepathy-glib-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libGConf2-devel GConf2

%description
The package contains an integrated GNOME VNC server.

%prep
%setup -q

%build
%configure2_5x \
  --disable-schemas-install \
  --enable-avahi \
  --enable-telepathy \
  --enable-gnome-keyring \
  --disable-http-server		\
  --enable-libnotify 		\
  --disable-network-manager

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name --with-gnome

%clean
rm -rf %{buildroot}

%preun
%preun_uninstall_gconf_schemas vino-server

%files -f %name.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog docs/remote-desktop.txt docs/TODO
%_sysconfdir/gconf/schemas/vino-server.schemas
%_sysconfdir/xdg/autostart/vino-server.desktop
%_bindir/vino-passwd
%_bindir/vino-preferences
%_libexecdir/vino-server
%_datadir/vino
%_datadir/applications/vino-preferences.desktop
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Vino.service
%_datadir/telepathy/clients/Vino.client
