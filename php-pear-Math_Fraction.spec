%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Fraction
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Classes that represent and manipulate fractions
Summary(pl):	%{_pearname} - Klasy do przedstawiania i manipulowania u³amkami
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9c84e6f4ae9427ab0824907bc6c9c2ff
URL:		http://pear.php.net/package/Math_Fraction/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

%description -l pl
Klasy do przedstawiania i manipulowania u³amkami (x = a/b).

Statyczna klasa Math_FractionOp zawiera definicje dla:
- podstawowych operacji arytmetycznych,
- porównywania u³amków,
- najwiêkszego wspólnego dzielnika (NWD) i najmniejszej wspólnej
  wielokrotno¶ci (NWM) dwóch liczb,
- upraszczanie (skracanie) i obliczanie odwrotno¶ci u³amka,
- konwersja liczby na u³amek.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/examples/*.php
%{php_pear_dir}/%{_class}/*.php
