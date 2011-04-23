%define upstream_name    Version-Next
%define upstream_version 0.002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Increment module version numbers simply and correctly
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Version/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a simple, correct way to increment a Perl module
version number. It does not attempt to guess what the original version
number author intended, it simply increments in the smallest possible
fashion. Decimals are incremented like an odometer. Dotted decimals are
incremented piecewise and presented in a standardized way.

If more complex version manipulation is necessary, you may wish to consider
the Perl::Version manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


