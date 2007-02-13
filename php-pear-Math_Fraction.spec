%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Fraction
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Classes that represent and manipulate fractions
Summary(pl.UTF-8):	%{_pearname} - Klasy do przedstawiania i manipulowania ułamkami
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	3
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2c1f57a50db75f7e489fbd0166cb4cf6
URL:		http://pear.php.net/package/Math_Fraction/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes that represent and manipulate fractions (x = a/b).

The Math_FractionOp static class contains definitions for:
- basic arithmetic operations,
- comparing fractions,
- greatest common divisor (gcd) and least common multiple (lcm) of two
  integers,
- simplifying (reducing) and getting the reciprocal of a fraction,
- converting a float to fraction.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasy do przedstawiania i manipulowania ułamkami (x = a/b).

Statyczna klasa Math_FractionOp zawiera definicje dla:
- podstawowych operacji arytmetycznych,
- porównywania ułamków,
- największego wspólnego dzielnika (NWD) i najmniejszej wspólnej
  wielokrotności (NWM) dwóch liczb,
- upraszczanie (skracanie) i obliczanie odwrotności ułamka,
- konwersja liczby na ułamek.

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
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
