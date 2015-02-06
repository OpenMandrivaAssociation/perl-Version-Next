%define upstream_name    Version-Next
%define upstream_version 0.002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Increment module version numbers simply and correctly
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Version/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.2.0-2mdv2011.0
+ Revision: 656977
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.2.0-1mdv2011.0
+ Revision: 596697
- update to 0.002

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.1.0-2mdv2011.0
+ Revision: 528121
- rebuild
- import perl-Version-Next


* Sat Mar 27 2010 cpan2dist 0.001-1mdv
- initial mdv release, generated with cpan2dist
