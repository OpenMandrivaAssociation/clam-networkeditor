%define soname 1.4
%define libname %mklibname clam-qtmonitors%{soname}
%define develname %mklibname clam-qtmonitors -d

Name: clam-networkeditor
Version: 1.4.0
Release: 1
Summary: A tool for editing CLAM processing networks
URL: http://clam-project.org/
Group: System/Libraries
License: GPL
Source: http://clam-project.org/download/src/NetworkEditor-%{version}.tar.gz
Patch1: %{name}-1.4.0-key-scope.patch
BuildRequires: libclam-devel scons qt4-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The CLAM Network Editor is a tool for editing CLAM processing networks.
Those processing networks can become the processing core of an application
by using the CLAM::NetworkPlayer class in your program or by using
the CLAM Prototyper to link the network to a Qt Designer interface.


%package examples
Group: System/Libraries
Summary: CLAM Network Editor examples

%description examples
The CLAM Network Editor is a tool for editing CLAM processing networks.
Those processing networks can become the processing core of an application
by using the CLAM::NetworkPlayer class in your program or by using
the CLAM Prototyper to link the network to a Qt Designer interface.

This package contains examples for the CLAM Network Editor.


%package -n %{libname}
Group: System/Libraries
Summary: Plugins for CLAM applications

%description -n %{libname}
CLAM is a full-fledged software framework for research and application
development in the Audio and Music Domain. It offers a conceptual model
as well as tools for the analysis, synthesis and processing of audio signals.

This package contains plugins for adding graphical processing units
to your CLAM applications.


%package -n %{develname}
Group: Development/C
Summary: Development components for clam-qtmonitors
Requires: %{libname} = %{version}-%{release}

%description -n %{develname}
CLAM is a full-fledged software framework for research and application
development in the Audio and Music Domain. It offers a conceptual model
as well as tools for the analysis, synthesis and processing of audio signals.

This package contains the development components for modules provided by
the clam-qtmonitors CLAM plugin.


%prep
%setup -q -n NetworkEditor-%{version}
%patch1 -p1 -b .key-scope

%build
mkdir -p %{buildroot}%{_prefix}
scons \
  prefix=%{buildroot}%{_prefix} \
  clam_prefix=%{_prefix} \
  release=yes

%install
mkdir -p %{buildroot}%{_prefix}
scons install

%clean
rm -rf %{buildroot}

%files
%doc README CHANGES
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*desktop
%{_datadir}/mime/packages/clam-network.xml
%{_datadir}/mimelnk/application/vnd.clam.network.desktop


%files examples
%{_datadir}/networkeditor

%files -n %{libname}
%defattr(0644,root,root,0755)
%{_libdir}/clam/libclam_qtmonitors_plugin.so

%files -n %{develname}
%defattr(0644,root,root,0755)
%{_includedir}/CLAM/qtmonitors
%{_libdir}/pkgconfig/clam_qtmonitors.pc
%{_libdir}/libclam_qtmonitors.so*
