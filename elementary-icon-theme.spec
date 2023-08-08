Summary:	An original set of vector icons designed specifically for elementary OS and its desktop environment: Pantheon
Summary(pl.UTF-8):	Oryginalny zestaw ikon wektorowych zaprojektowany specjalnie dla elementary OS i jego środowiska graficznego: Pantheon.
Name:		elementary-icon-theme
Version:	7.3.1
Release:	1
License:	GPL v3
Group:		X11/Applications
URL:		https://github.com/elementary/icons
Source0:	https://github.com/elementary/icons/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	748124a7a1973818d81c7de20977c215
BuildRequires:	gettext-tools
BuildRequires:	librsvg
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	xorg-app-xcursorgen
Requires(post,postun):	gtk-update-icon-cache
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An original set of vector icons designed specifically for elementary
OS and its desktop environment: Pantheon.

%description -l pl.UTF-8
Oryginalny zestaw ikon wektorowych zaprojektowany specjalnie dla
elementary OS i jego środowiska graficznego: Pantheon.

%prep
%setup -q -n icons-%{version}

%build
%meson build --prefix=%{_prefix}
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/icons
%ninja_install -C build
%{__rm} -r $RPM_BUILD_ROOT/.VolumeIcon.*
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/{gimp,inkscape}
touch $RPM_BUILD_ROOT%{_iconsdir}/elementary/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache elementary

%postun
%update_icon_cache elementary

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md COPYING README.md
%dir %{_iconsdir}/elementary
%ghost %{_iconsdir}/elementary/icon-theme.cache
%{_datadir}/metainfo/io.elementary.icons.metainfo.xml
%{_iconsdir}/elementary/{actions,apps,categories,cursors,devices,emblems,emotes,mimes,places,status}
%{_iconsdir}/elementary/*@2x
%{_iconsdir}/elementary/*@3x
%{_iconsdir}/elementary/*.theme
