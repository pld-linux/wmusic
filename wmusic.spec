Summary:	A remote-control DockApp for XMMS
Summary(pl):	"Pilot" do XMMS-a dla Doku WindowMakera
Name:		wmusic
Version:	1.5.0
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://home.jtan.com/~john/wmusic/%{name}-%{version}.tar.gz
# Source0-md5:	20b39e0528089161998e2b0c77b1e4ea
Source1:	%{name}.desktop
Patch0:		%{name}-ac.patch
URL:		http://home.jtan.com/~john/wmusic/
BuildRequires:	xmms-devel >= 1.0.0
BuildRequires:	libdockapp-devel >= 0.3.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuilDrequires:	xmms-devel
Obsoletes:	wmplay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmusic is a dockapp that remote-controls XMMS.
Here is a list of the features:
 - VCR style controls including fast rewind and fast forward
 - Time and Playlist position display
 - Super stylee rotating arrow
 - Hiding of the XMMS windows (on startup and through middle-click)
 - Multi-threaded

%description -l pl
wmusic jest dokowalnym apletem umo�liwiaj�cym zdalne sterowanie
XMMS-em. Oto lista niekt�rych cech programu:
 - funkcje kontrolne w stylu VCR, m.in. szybkie przewijanie i cofanie
 - wy�wietlacz czasu i pozycji z listy odgrywanych utwor�w
 - ukrywanie okna XMMS-a
 - wielow�tkowo��

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -I/usr/X11R6/include"
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(0755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/%{name}.desktop
