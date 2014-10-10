%define upstream_name    Module-Extract-Use
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Pull out the modules a module uses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/Module-Extract-Use-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(PPI)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Output)
BuildArch:	noarch

%description
Extract the names of the modules used in a file using a static analysis.
Since this module does not run code, it cannot find dynamic uses of
modules, such as 'eval "require $class"'.

* new

  Makes an object. The object doesn't do anything just yet, but you need it
  to call the methods.

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
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 657448
- rebuild for updated spec-helper

* Mon Apr 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.0-1
+ Revision: 650312
- update to new version 1.01

* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.180.0-1
+ Revision: 648090
- update to new version 0.18

* Sat Jan 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 492117
- import perl-Module-Extract-Use


* Sat Jan 16 2010 cpan2dist 0.17-1mdv
- initial mdv release, generated with cpan2dist


