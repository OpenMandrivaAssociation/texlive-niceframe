%global tl_name niceframe
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1c
Release:	%{tl_revision}.1
Summary:	Support for fancy frames
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/niceframe
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines means of drawing frames around boxes, using dingbat
fonts. Some (Metafont) font sources are included; the fonts are
available separately in Type 1 format.

