%global tl_name babel-kurmanji
%global tl_revision 30279

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Babel support for Kurmanji
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/kurmanji
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-kurmanji.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-kurmanji.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-kurmanji.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of
Kurmanji in babel. Kurmanji belongs to the family of Kurdish languages.
Some shortcuts are defined, as well as translations to Kurmanji of
standard "LaTeX names". Note that the package is dealing with 'Northern'
Kurdish, written using a Latin-based alphabet. The arabxetex package
offers support for Kurdish written in Arabic script.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-kurmanji
%dir %{_datadir}/texmf-dist/source/generic/babel-kurmanji
%dir %{_datadir}/texmf-dist/tex/generic/babel-kurmanji
%doc %{_datadir}/texmf-dist/doc/generic/babel-kurmanji/kurmanji.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-kurmanji/kurmanji.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-kurmanji/kurmanji.ins
%{_datadir}/texmf-dist/tex/generic/babel-kurmanji/kurmanji.ldf
