Name:           cub-devel
Version:        1.8.0
Release:        1%{?dist}
Summary:        Patterns and behaviors for GPU computing         
License:        BSD 2-Clause
URL:            http://nvlabs.github.io/cub/
Source:         cub-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3
BuildRequires:  gcc-c++

%description
CUB is a flexible library of cooperative threadblock primitives and other utilities for CUDA kernel programming. the library is in its accelerated primitives for solving irregularly parallel problems.

%prep
%setup -n cub-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/include
cp -R cub $RPM_BUILD_ROOT/usr/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE.TXT README.md
/usr/include/cub

%changelog
