Summary: GNOME VNC server and client
Name: vino
Version: 3.2.2
Release: 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/vino/%{name}-%{version}.tar.xz
License: GPLv2+
Group: Networking/Remote access
Url: http://www.gnome.org

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(NetworkManager)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(zlib)

%description
The package contains an integrated GNOME VNC server.

%prep
%setup -q

%build
%configure2_5x \
  --disable-http-server

%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS AUTHORS ChangeLog docs/remote-desktop.txt docs/TODO
#{_sysconfdir}/gconf/schemas/vino-server.schemas
%{_sysconfdir}/xdg/autostart/vino-server.desktop
%{_bindir}/vino-passwd
%{_bindir}/vino-preferences
%{_libexecdir}/vino-server
%{_datadir}/vino
%{_datadir}/applications/vino-preferences.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vino.service
%{_datadir}/GConf/gsettings/org.gnome.Vino.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/telepathy/clients/Vino.client

