%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _userunitdir /usr/lib/systemd/user/

Summary:	GNOME VNC server and client
Name:		vino
Version:	3.22.0
Release:	3
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vino/%{url_ver}/%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Networking/Remote access
Url:		http://www.gnome.org

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gnutls) >= 3.0
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(zlib)
BuildRequires:  pkgconfig(systemd)

%description
The package contains an integrated GNOME VNC server.

%prep
%setup -q

%build
%configure

%make_build

%install
%make_install
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS AUTHORS ChangeLog docs/remote-desktop.txt docs/TODO
%{_libexecdir}/vino-server
%{_datadir}/applications/vino-server.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vino.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/telepathy/clients/Vino.client
%{_userunitdir}/%{name}-server.service

