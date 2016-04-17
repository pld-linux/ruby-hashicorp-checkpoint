#
# Conditional build:
%bcond_with	tests		# tests. requires RSpec3

%define	pkgname	hashicorp-checkpoint
Summary:	Internal HashiCorp service to check version information
Name:		ruby-%{pkgname}
Version:	0.1.4
Release:	2
License:	MPL v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	e1400274453f554e97204e75fdb31b6d
URL:		http://www.hashicorp.com
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.6
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec < 3.1
BuildRequires:	ruby-rspec >= 3.0.0
BuildRequires:	ruby-rspec-its < 1.1
BuildRequires:	ruby-rspec-its >= 1.0.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Internal HashiCorp service to check version information.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
rspec spec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.txt
%{ruby_vendorlibdir}/checkpoint.rb
%{ruby_vendorlibdir}/checkpoint
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
