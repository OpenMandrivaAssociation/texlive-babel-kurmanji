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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of
Kurmanji in babel. Kurmanji belongs to the family of Kurdish languages.
Some shortcuts are defined, as well as translations to Kurmanji of
standard "LaTeX names". Note that the package is dealing with 'Northern'
Kurdish, written using a Latin-based alphabet. The arabxetex package
offers support for Kurdish written in Arabic script.

