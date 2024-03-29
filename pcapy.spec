Summary:	Python pcap extension
Summary(pl.UTF-8):	Rozszerzenie pcap dla Pythona
Name:		pcapy
Version:	0.10.5
Release:	0.1
License:	Apache Software License 1.1
Group:		Libraries
Source0:	http://oss.coresecurity.com/repo/%{name}-%{version}.tar.gz
# Source0-md5:	1dcff6af494f3d6763f457aa86aa0853
URL:		http://oss.coresecurity.com/projects/pcapy.html
BuildRequires:	libpcap-devel
BuildRequires:	python-devel >= 2.2.1
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pcapy is a Python extension module that enables software written in
Python to access the routines from the pcap packet capture library.

%description -l pl.UTF-8
Pcapy to moduł rozszerzenia Pythona pozwalający programom napisanym w
Pythonie na dostęp do funkcji z biblioteki przechwytywania pakietów
pcap.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README pcapy.html
%attr(755,root,root) %{py_sitedir}/pcapy.so
