Name:		texlive-sauerj
Version:	20180303
Release:	2
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
%{_texmfdistdir}/tex/latex/sauerj
%doc %{_texmfdistdir}/doc/latex/sauerj
#- source
%doc %{_texmfdistdir}/source/latex/sauerj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
