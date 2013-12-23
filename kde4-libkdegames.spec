%define		_state		stable
%define		orgname		libkdegames
%define		qtver		4.8.0

Summary:	K Desktop Environment - games
Summary(es.UTF-8):	K Desktop Environment - Juegos
Summary(ja.UTF-8):	KDEデスクトップ環境 - ゲーム
Summary(ko.UTF-8):	K 데스크탑 환경 - 놀이(게임)
Summary(pl.UTF-8):	K Desktop Environment - gry
Summary(pt_BR.UTF-8):	K Desktop Environment - Jogos
Summary(zh_CN.UTF-8):	KDE游戏
Name:		kde4-libkdegames
Version:	4.12.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	24bbf5989dc9cead8dbeef309486fc4e
BuildRequires:	OpenAL-devel
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libsndfile-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries for kdegames which contain highscore support functions.

%description -l pl.UTF-8
Biblioteki dla gier KDE zawierające wsparcie dla tabel wyników.

%package devel
Summary:	Development files for KDE games
Summary(pl.UTF-8):	Pliki przydatne twórcom gier dla KDE
Summary(pt_BR.UTF-8):	Arquivos de inclusão do kdegames
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdegame-devel

%description devel
Development files for KDE games.

%description devel -l pl.UTF-8
Pliki dla programistów KDE games.

%description devel -l pt_BR.UTF-8
Este pacote detém os arquivos de inclusão necessários para compilar
aplicativos que usam bibliotecas do kdegames.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
touch $RPM_BUILD_ROOT/var/games/kbounce.scores
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog README README.highscore
%attr(755,root,root) %{_libdir}/libkdegames.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdegames.so.?
%attr(755,root,root) %{_libdir}/libkdegamesprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdegamesprivate.so.?
#%attr(755,root,root) %{_libdir}/kde4/imports/org/kde/games/core/libcorebindingsplugin.so
%{_libdir}/kde4/imports/org/kde/games
%{_datadir}/apps/carddecks
%{_datadir}/apps/kconf_update/kgthemeprovider-migration.upd
#/var/games/kbounce.scores

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdegames.so
%attr(755,root,root) %{_libdir}/libkdegamesprivate.so
%{_includedir}/KDE/KExtHighscore
%{_includedir}/KDE/KGameClock
%{_includedir}/KDE/KGamePopupItem
%{_includedir}/KDE/KGameRenderedItem
%{_includedir}/KDE/KGameRenderedObjectItem
%{_includedir}/KDE/KGameRenderer
%{_includedir}/KDE/KGameRendererClient
%{_includedir}/KDE/KHighscore
%{_includedir}/KDE/KScoreDialog
%{_includedir}/KDE/KStandardGameAction
%{_includedir}/KDE/KgAudioScene
%{_includedir}/KDE/KgDeclarativeView
%{_includedir}/KDE/KgDifficulty
%{_includedir}/KDE/KgSound
%{_includedir}/KDE/KgTheme
%{_includedir}/KDE/KgThemeProvider
%{_includedir}/KDE/KgThemeSelector
%{_includedir}/highscore
%{_includedir}/kgameclock.h
%{_includedir}/kgamepopupitem.h
%{_includedir}/kgamerendereditem.h
%{_includedir}/kgamerenderedobjectitem.h
%{_includedir}/kgamerenderer.h
%{_includedir}/kgamerendererclient.h
%{_includedir}/kgaudioscene.h
%{_includedir}/kgdeclarativeview.h
%{_includedir}/kgdifficulty.h
%{_includedir}/kgsound.h
%{_includedir}/kgtheme.h
%{_includedir}/kgthemeprovider.h
%{_includedir}/kgthemeselector.h
%{_includedir}/kstandardgameaction.h
%{_includedir}/libkdegames_capabilities.h
%{_includedir}/libkdegames_export.h
%{_includedir}/libkdegamesprivate
%{_libdir}/cmake/KDEGames
