Name:		texlive-niceframe
Version:	36086
Release:	2
Summary:	Support for fancy frames
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/niceframe
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines means of drawing frames around boxes, using
dingbat fonts. Some (Metafont) font sources are included; the
fonts are available separately in Type 1 format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/niceframe/karta.mf
%{_texmfdistdir}/fonts/source/public/niceframe/karta15.mf
%{_texmfdistdir}/fonts/source/public/niceframe/umrand.mf
%{_texmfdistdir}/fonts/source/public/niceframe/umranda.mf
%{_texmfdistdir}/fonts/source/public/niceframe/umrandb.mf
%{_texmfdistdir}/fonts/tfm/public/niceframe/karta15.tfm
%{_texmfdistdir}/fonts/tfm/public/niceframe/umranda.tfm
%{_texmfdistdir}/fonts/tfm/public/niceframe/umrandb.tfm
%{_texmfdistdir}/tex/latex/niceframe/niceframe.sty
%doc %{_texmfdistdir}/doc/latex/niceframe/dingbat.mf
%doc %{_texmfdistdir}/doc/latex/niceframe/example.tex
%doc %{_texmfdistdir}/doc/latex/niceframe/niceframe.pdf
#- source
%doc %{_texmfdistdir}/source/latex/niceframe/niceframe.drv
%doc %{_texmfdistdir}/source/latex/niceframe/niceframe.dtx
%doc %{_texmfdistdir}/source/latex/niceframe/niceframe.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
