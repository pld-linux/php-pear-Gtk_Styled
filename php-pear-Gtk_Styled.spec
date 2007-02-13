%include	/usr/lib/rpm/macros.php
%define		_class		Gtk
%define		_subclass	Styled
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - PHP-GTK pseudo-widgets that mimic GtkData based objects
Summary(pl.UTF-8):	%{_pearname} - pseudo widgety naśladujące oparte na GtkData obiekty
Name:		php-pear-%{_pearname}
Version:	0.9.0
%define	_beta beta1
%define	_rel 0.2
Release:	0.%{_beta}.%{_rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_beta}.tgz
# Source0-md5:	5c5d4364259b066c187aabb78d48903a
URL:		http://pear.php.net/package/Gtk_Styled/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in data/
%define		_noautoreq 'pear(data/Gtk_Styled/Buttons.php)'

%description
While it is possible to control some style elements of a GtkScrollBar,
other elements cannot be controlled so easily. Items such as the
images at the begining and end (usually arrows) and the scroll bar
that is dragged to scroll the element cannot be changed. This leads to
applications that either must conform to the windowing systems look
and feel or appear incomplete. The goal of this family of PHP-GTK
classes is to provide all the same functionality as a normal scroll
bar but allow the user to have better control over the look and feel.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
O ile można kontrolować niektóre elementy styli GtkScrollBara, innych
elementów nie da się kontrolować tak łatwo. Rzeczy takie jak obrazki
na początku i końcu (zwykle strzałki) i pasek przesuwania przeciągany
w celu przewinięcia elementów nie mogą być zmienione. Prowadzi to do
aplikacji, które muszą być zgodne z wyglądem systemów okienkowych albo
wyglądają niekompletnie. Celem tej rodziny klas PHP-GTK jest
dostarczenie takiej samej funkcjonalności jak normalny pasek
przesuwania, ale dającej lepszą kontrolę nad wyglądem i zachowaniem.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/data/Gtk_Styled
