Summary:	A remote-control DockApp for xmms
Summary(pl):	"Pilot" do xmms dla Doku WindowMakera
Name:		wmusic
Version:	1.4.7
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.hadess.net/files/attic/wmusic/%{name}-%{version}.tar.gz
# Source0-md5:	accd0711d89e4049174a2554e1c61958
#Source0:	http://home.jtan.com/~john/wmusic/downloads/%{name}-%{version}-old.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-ac.patch
URL:		http://home.jtan.com/~john/wmusic/
BuildRequires:	xmms-devel >= 1.0.0
BuildRequires:	libdockapp-devel >= 0.3.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuilDrequires:  xmms-devel
Obsoletes:	wmplay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
wmusic is a dockapp that remote-controls xmms.
Here is a list of the features:
	- VCR style controls including fast rewind and fast forward 
	- Time and Playlist position display 
	- Super stylee rotating arrow 
	- Hiding of the xmms windows (on startup and through middle-click) 
	- Multi-threaded

%description -l pl
wmusic jest dokowalnym apletem umożliwiającym zdalne sterowanie aplikacją
xmms. Oto lista niektórych cech programu:
	- funkcje kontrolne w stylu VCR, m.in. szybkie przewijanie i cofanie
	- wyświetlacz czasu i pozycji z listy odgrywanych utworów
	- ukrywanie okna xmms
	- wielowątkowość

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
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(0755,root,root) %{_bindir}/%{name}

#%%{_applnkdir}/DockApplets/%{name}.desktop
