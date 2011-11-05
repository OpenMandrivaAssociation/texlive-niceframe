# revision 24120
# category Package
# catalog-ctan /macros/latex/contrib/niceframe
# catalog-date 2011-06-16 20:35:20 +0200
# catalog-license lppl
# catalog-version 1.1c
Name:		texlive-niceframe
Version:	1.1c
Release:	1
Summary:	Support for fancy frames
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/niceframe
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package defines means of drawing frames around boxes, using
dingbat fonts. Some (Metafont) font sources are included; the
fonts are available separately in Type 1 format.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
