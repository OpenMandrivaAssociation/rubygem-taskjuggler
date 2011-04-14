# Generated from taskjuggler-0.0.11.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	taskjuggler

Summary:	Project Management Software
Name:		rubygem-%{rbname}
Version:	0.0.11
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://www.taskjuggler.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch
Obsoletes:	taskjuggler
Provides:	taskjuggler

%description
TaskJuggler is a project management software that goes far beyond the commonly
known Gantt chart editors.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(benchmarks|examples|data|manual|spec|tasks|test)'/

%install
%gem_install

%files
%{_bindir}/tj3
%{_bindir}/tj3client
%{_bindir}/tj3d
%{_bindir}/tj3man
%{_bindir}/tj3ss_receiver
%{_bindir}/tj3ss_sender
%{_bindir}/tj3ts_receiver
%{_bindir}/tj3ts_sender
%{_bindir}/tj3ts_summary
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/data
%{ruby_gemdir}/gems/%{rbname}-%{version}/data/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/taskjuggler
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/taskjuggler/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec/support
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/support/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tasks
%{ruby_gemdir}/gems/%{rbname}-%{version}/tasks/*.rake
%{ruby_gemdir}/gems/%{rbname}-%{version}/tasks/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGELOG
%{ruby_gemdir}/gems/%{rbname}-%{version}/COPYING
%{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/benchmarks
%{ruby_gemdir}/gems/%{rbname}-%{version}/benchmarks/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*.tjp
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/manual
%{ruby_gemdir}/gems/%{rbname}-%{version}/manual/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test/
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*

