Name:           perl-App-cpanminus
Version:        1.6922
Release:        1%{?dist}
Summary:        Get, unpack, build and install CPAN modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/App-cpanminus/
Source0:        http://www.cpan.org/authors/id/M/MI/MIYAGAWA/App-cpanminus-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Tests:
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# Required by bin/cpanm
Requires:       perl(base)
Requires:       perl(Carp)
Requires:       perl(constant)
# CPAN::DistnameInfo bundled
# CPAN::Meta not used
# CPAN::Meta::Check bundled
# CPAN::Meta::Converter bundled
# CPAN::Meta::Feature bundled
# CPAN::Meta::History bundled
# CPAN::Meta::Prereqs bundled
# CPAN::Meta::Requirements bundled
# CPAN::Meta::Spec bundled
# CPAN::Meta::Validator bundled
# CPAN::Meta::YAML bundled
Requires:       perl(Cwd)
Requires:       perl(Digest::SHA)
Requires:       perl(Encode)
# Exporter bundled
# Exporter::Heavy bundled
Requires:       perl(ExtUtils::Install) >= 1.46
Requires:       perl(ExtUtils::MakeMaker) >= 6.31
Requires:       perl(File::Path)
# File::pushd bundled
Requires:       perl(File::Spec)
Requires:       perl(Getopt::Long)
# HTTP getter by LWP::UserAgent or wget or curl or HTTP::Tiny
# HTTP::Tiny bundled
Requires:       perl(IO::File)
Requires:       perl(IO::Socket)
# JSON::PP bundled
# lib::core::only not used
# local::lib bundled
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::BigInt)
Requires:       perl(Module::Build)
Requires:       perl(Module::CoreList)
# Module::CPANfile bundled
# Module::Metadata bundled
Requires:       perl(Module::Signature)
# Parse::CPAN::Meta bundled
Requires:       perl(Safe)
Requires:       perl(Scalar::Util)
Requires:       perl(Time::Local)
# version bundled
# version::vpp bundled
Requires:       perl(YAML)
# XXX: Keep Provides: cpanminus to allow `yum install cpanminus' instead of
# longer `yum install perl-App-cpanminus'.
Provides:       cpanminus = %{version}-%{release}
Obsoletes:      cpanminus <= 1.2002

# Do not require/export in-place modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(App::cpanminus::script\\)$

%description
Why? It's dependency free, requires zero configuration, and stands alone 
but it's maintainable and extensible with plug-ins and friendly to shell 
scripting. When running, it requires only 10 MB of RAM.

%prep
%setup -q -n App-cpanminus-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/cpanm

%changelog
* Fri Jun 21 2013 Petr Pisar <ppisar@redhat.com> - 1.6922-1
- 1.6922 bump

* Thu Jun 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.6921-1
- 1.6921 bump

* Thu Jun 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.6918-1
- 1.6918 bump

* Thu May 16 2013 Petr Pisar <ppisar@redhat.com> - 1.6915-1
- 1.6915 bump

* Mon May 13 2013 Petr Pisar <ppisar@redhat.com> - 1.6914-1
- 1.6914 bump

* Mon May 13 2013 Petr Pisar <ppisar@redhat.com> - 1.6913-1
- 1.6913 bump

* Tue May 07 2013 Petr Pisar <ppisar@redhat.com> - 1.6912-1
- 1.6912 bump

* Mon May 06 2013 Petr Pisar <ppisar@redhat.com> - 1.6911-1
- 1.6911 bump

* Thu May 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.6909-1
- 1.6909 bump

* Mon Apr 29 2013 Petr Pisar <ppisar@redhat.com> - 1.6907-1
- 1.6907 bump

* Mon Apr 22 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.6902-1
- 1.6902 bump

* Mon Apr 15 2013 Petr Pisar <ppisar@redhat.com> - 1.6108-1
- 1.6108 bump

* Mon Apr 08 2013 Petr Pisar <ppisar@redhat.com> - 1.6107-1
- 1.6107 bump

* Mon Apr 08 2013 Petr Pisar <ppisar@redhat.com> - 1.6105-1
- 1.6105 bump

* Wed Apr 03 2013 Petr Pisar <ppisar@redhat.com> - 1.6104-1
- 1.6104 bump

* Thu Mar 28 2013 Petr Pisar <ppisar@redhat.com> - 1.6102-1
- 1.6102 bump

* Tue Mar 26 2013 Petr Pisar <ppisar@redhat.com> - 1.6101-1
- 1.6101 bump

* Wed Mar 20 2013 Petr Pisar <ppisar@redhat.com> - 1.6008-1
- 1.6008 bump

* Thu Mar 14 2013 Petr Pisar <ppisar@redhat.com> - 1.6006-1
- 1.6006 bump

* Mon Mar 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.6005-1
- 1.6005 bump

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 1.6002-1
- 1.6002 bump

* Mon Feb  4 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.5021-1
- 1.5021 bump

* Wed Jan 02 2013 Petr Pisar <ppisar@redhat.com> - 1.5019-1
- 1.5019 bump

* Wed Sep 19 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.5018-1
- 1.5018 bump

* Fri Jul 20 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.5017-1
- 1.5017 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.5015-2
- Perl 5.16 rebuild

* Mon Jun 25 2012 Petr Šabata <contyk@redhat.com> - 1.5015-1
- 1.5015 bump

* Wed Jun 13 2012 Petr Šabata <contyk@redhat.com> - 1.5014-1
- 1.5014 bump
- Drop command macros

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.5013-2
- Perl 5.16 rebuild

* Mon May 14 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.5013-1
- 1.5013 bump

* Fri Apr 13 2012 Petr Šabata <contyk@redhat.com> - 1.5011-1
- 1.5011 bump

* Tue Apr 03 2012 Petr Šabata <contyk@redhat.com> - 1.5010-1
- 1.5010 bump

* Mon Mar 19 2012 Marcela Mašláňová <mmaslano@redhat.com> 1.5008-1
- bump to 1.5008

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.5007-1
- 1.5007 bump

* Wed Nov 30 2011 Petr Šabata <contyk@redhat.com> - 1.5006-1
- 1.5006 bump

* Wed Nov 23 2011 Petr Šabata <contyk@redhat.com> - 1.5005-1
- 1.5005 bump
- defattr removed

* Wed Nov 09 2011 Petr Sabata <contyk@redhat.com> - 1.5004-1
- 1.5004 bump

* Wed Oct 19 2011 Petr Sabata <contyk@redhat.com> - 1.5003-1
- 1.5003 bump

* Tue Oct 18 2011 Petr Sabata <contyk@redhat.com> - 1.5002-1
- 1.5002 bump

* Fri Oct 14 2011 Petr Sabata <contyk@redhat.com> - 1.5001-1
- 1.5001 bump

* Thu Oct 13 2011 Petr Sabata <contyk@redhat.com> - 1.5000-1
- 1.5000 bump

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 1.4008-3
- RPM 4.9 dependency filtering added

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4008-2
- Perl mass rebuild

* Thu Jun 16 2011 Petr Pisar <ppisar@redhat.com> - 1.4008-1
- 1.4008 bump

* Wed May 18 2011 Petr Pisar <ppisar@redhat.com> - 1.4007-1
- 1.4007 bump
- LWP is optional since this package bundles HTTP::Tiny. Upstream recognized
  LWP being heavy. Follow upstream decision in RPM package dependencies.

* Tue May 17 2011 Petr Pisar <ppisar@redhat.com> - 1.4006-1
- 1.4006 bump
- Fix obsoleted version string

* Thu May 12 2011 Petr Sabata <psabata@redhat.com> - 1.4005-1
- 1.4005 bump

* Fri Mar 11 2011 Petr Sabata <psabata@redhat.com> - 1.4004-1
- 1.4004 bump

* Thu Mar 10 2011 Petr Pisar <ppisar@redhat.com> - 1.4003-1
- 1.4003 bump

* Tue Mar 08 2011 Petr Pisar <ppisar@redhat.com> - 1.4000-1
- 1.4000 bump

* Fri Mar 04 2011 Petr Pisar <ppisar@redhat.com> - 1.3001-1
- 1.3001 bump

* Thu Mar 03 2011 Petr Pisar <ppisar@redhat.com> - 1.3000-1
- 1.3000 bump
- Clean up spec file
- Require modules needed by cpanm
- Merge cpanminus into main package as cpanminus required main package and
  main package did not contain any code (i.e. was useless).

* Thu Feb 17 2011 Petr Sabata <psabata@redhat.com> - 1.2001-1
- 1.2001 bump

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Petr Pisar <ppisar@redhat.com> - 1.1008-1
- 1.1008 bump

* Mon Jan 24 2011 Petr Pisar <ppisar@redhat.com> - 1.1007-1
- 1.1007 bump

* Mon Jan  3 2011 Petr Sabata <psabata@redhat.com> - 1.1006-1
- 1.1006 bump

* Thu Dec  2 2010 Petr Sabata <psabata@redhat.com> - 1.1004-1
- 1.1004 bump

* Fri Nov 19 2010 Petr Pisar <ppisar@redhat.com> - 1.1002-1
- 1.1002 bump

* Mon Sep 27 2010 Petr Pisar <ppisar@redhat.com> - 1.0015-1
- 1.0015 bump

* Thu Sep 23 2010 Petr Pisar <ppisar@redhat.com> - 1.0014-1
- 1.0014 bump

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 1.0013-1
- 1.0013 bump
- Correct description spelling

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.9935-3
- Mass rebuild with perl-5.12.0

* Tue Mar 16 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.9935-2
- filter unwanted requires

* Tue Mar 16 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.9935-1
- update

* Tue Mar 16 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.9923-1
- update
- create sub-package

* Tue Mar  2 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.9911-1
- new version & fix description

* Tue Feb 23 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
