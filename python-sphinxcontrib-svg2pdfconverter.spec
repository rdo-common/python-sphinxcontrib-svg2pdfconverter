%{?python_enable_dependency_generator}
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%global srcname sphinxcontrib-svg2pdfconverter

Name:           python-%{srcname}
Version:        0.1.0
Release:        4%{?dist}
Summary:        Sphinx SVG to PDF Converter Extension

License:        BSD
URL:            https://pypi.org/project/sphinxcontrib-svg2pdfconverter/
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).


%package -n python%{pyver}-%{srcname}-common
Summary:        Sphinx SVG to PDF Converter Extension - common files

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-sphinx


%description -n python%{pyver}-%{srcname}-common
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains common files.


%package -n python%{pyver}-sphinxcontrib-inkscapeconverter
Summary:        Sphinx SVG to PDF Converter Extension - Inkscape converter

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-sphinx
Requires:       /usr/bin/inkscape
Requires:       python%{pyver}-%{srcname}-common = %{version}-%{release}

%{?python_provide:%python_provide python%{pyver}-sphinxcontrib-inkscapeconverter}

%description -n python%{pyver}-sphinxcontrib-inkscapeconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using Inkscape.


%package -n python%{pyver}-sphinxcontrib-rsvgconverter
Summary:        Sphinx SVG to PDF Converter Extension - libRSVG converter

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-sphinx
Requires:       /usr/bin/rsvg-convert
Requires:       python%{pyver}-%{srcname}-common = %{version}-%{release}

%{?python_provide:%python_provide python%{pyver}-sphinxcontrib-rsvgconverter}

%description -n python%{pyver}-sphinxcontrib-rsvgconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using libRSVG.


%prep
%autosetup -n %{srcname}-%{version}


%build
%pyver_build


%install
%pyver_install


%check
%{pyver_bin} setup.py test


# Note that there is no %%files section for the unversioned python module
%files -n python%{pyver}-%{srcname}-common
%license LICENSE.txt
%doc README.rst
%{pyver_sitelib}/sphinxcontrib_svg2pdfconverter*nspkg.pth
%{pyver_sitelib}/sphinxcontrib_svg2pdfconverter-*.egg-info


%files -n python%{pyver}-sphinxcontrib-inkscapeconverter
%if %{pyver} == 3
%{python3_sitelib}/sphinxcontrib/__pycache__/inkscapeconverter.*.pyc
%endif
%{pyver_sitelib}/sphinxcontrib/inkscapeconverter.py*


%files -n python%{pyver}-sphinxcontrib-rsvgconverter
%if %{pyver} == 3
%{python3_sitelib}/sphinxcontrib/__pycache__/rsvgconverter.*.pyc
%endif
%{pyver_sitelib}/sphinxcontrib/rsvgconverter.py*


%changelog
* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-4
- Rebuilt for Python 3.8

* Sun Aug 04 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.0-3
- Correct the dependencies between subpackages

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.0-1
- Initial RPM release
