Summary:	A remote-control DockApp for xmms
Summary(pl):	"Pilot" do xmms dla Doku WindowMakera
Name:		wmusic
Version:	1.2.2
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://idoru.current.nu/pub/idoru/%{name}-%{version}.tar.gz
Source1:	wmusic.desktop
BuildRequires:	xmms-devel >= 1.0.0
BuildRequires:	libdockapp-devel >= 0.3.0
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
Obsoletes:	wmplay
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_applnkdir	%{_datadir}/applnk

%description
wmusic is a dockapp that remote-controls xmms.
Here is a list of the features:
	- VCR style controls including fast rewind and fast forward 
	- Time and Playlist position display 
	- Super stylee rotating arrow 
	- Hiding of the xmms windows (on startup and through middle-click) 
	- Multi-threaded

%description -l pl
wmusic jest dokowalnym apletem umo¿liwiaj±cym zdalne sterowanie aplikacj±
xmms. Oto lista niektórych cech programu:
	- funkcje kontrolne w stylu VCR, m.in. szybkie przewijanie i cofanie
	- wy¶wietlacz czasu i pozycji z listy odgrywanych utworów
	- ukrywanie okna xmms
	- wielow±tkowo¶æ

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"
LDFLAGS="-s -L/usr/X11R6/lib"
export CFLAGS LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(0755,root,root) %{_bindir}/%{name}

%{_applnkdir}/DockApplets/%{name}.desktop
