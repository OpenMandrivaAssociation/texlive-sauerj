# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sauerj
# catalog-date 2007-01-15 20:25:47 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-sauerj
Version:	20070115
Release:	8
Summary:	A bundle of utilities by Jonathan Sauer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sauerj
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sauerj.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sauerj.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sauerj.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle consists of: a tool for collecting text for later
re-use, a tool for typesetting the "meta-information" within a
text, a tool for use in constructing macros with multiple
optional parameters, a package for multiple column parallel
texts, a tool for processing key-value structured lists, and
macros for typesetting a number as a German-language string.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sauerj/collect.sty
%{_texmfdistdir}/tex/latex/sauerj/metainfo.sty
%{_texmfdistdir}/tex/latex/sauerj/optparams.sty
%{_texmfdistdir}/tex/latex/sauerj/parcolumns.sty
%{_texmfdistdir}/tex/latex/sauerj/processkv.sty
%{_texmfdistdir}/tex/latex/sauerj/zahl2string.sty
%doc %{_texmfdistdir}/doc/latex/sauerj/README
%doc %{_texmfdistdir}/doc/latex/sauerj/collect.pdf
%doc %{_texmfdistdir}/doc/latex/sauerj/metainfo.pdf
%doc %{_texmfdistdir}/doc/latex/sauerj/optparams.pdf
%doc %{_texmfdistdir}/doc/latex/sauerj/parcolumns.pdf
%doc %{_texmfdistdir}/doc/latex/sauerj/processkv.pdf
%doc %{_texmfdistdir}/doc/latex/sauerj/zahl2string.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sauerj/collect.dtx
%doc %{_texmfdistdir}/source/latex/sauerj/collect.ins
%doc %{_texmfdistdir}/source/latex/sauerj/metainfo.dtx
%doc %{_texmfdistdir}/source/latex/sauerj/metainfo.ins
%doc %{_texmfdistdir}/source/latex/sauerj/optparams.dtx
%doc %{_texmfdistdir}/source/latex/sauerj/optparams.ins
%doc %{_texmfdistdir}/source/latex/sauerj/parcolumns.dtx
%doc %{_texmfdistdir}/source/latex/sauerj/parcolumns.ins
%doc %{_texmfdistdir}/source/latex/sauerj/processkv.dtx
%doc %{_texmfdistdir}/source/latex/sauerj/processkv.ins
%doc %{_texmfdistdir}/source/latex/sauerj/zahl2string.dtx
%doc %{_texmfdistdir}/source/latex/sauerj/zahl2string.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070115-2
+ Revision: 755790
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070115-1
+ Revision: 719481
- texlive-sauerj
- texlive-sauerj
- texlive-sauerj
- texlive-sauerj

