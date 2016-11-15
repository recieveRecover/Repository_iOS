<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<meta name="robots" content="nofollow" />
<meta content="text/html; charset=iso-8859-1" http-equiv="Content-Type" />
<link rel="search" type="application/opensearchdescription+xml" href="https://www.freebsd.org/search/opensearch/man.xml" title="FreeBSD Manpages" />
<link rel="search" type="application/opensearchdescription+xml" href="https://www.freebsd.org/search/opensearch/man-freebsd-release-ports.xml" title="FreeBSD + Ports Manpages" />
<style type="text/css">
<!--
b { color: #996600; }
i { color: #008000; }
-->
</style>
<title>syslog.conf(5)</title>
<meta http-equiv='content-type' content='text/html; charset=iso-8859-1' />
<meta name='robots' content='nofollow' />
    <link rel="stylesheet" media="screen"
    href="../layout/css/fixed.css" type="text/css"
    title="Normal Text" />
    <link rel="alternate stylesheet" media="screen"
    href="../layout/css/fixed_large.css" type="text/css"
    title="Large Text" />
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
    <link rel="apple-touch-icon" href="/favicon.ico" type="image/x-icon" />

<script type="text/javascript" src="../layout/js/google.js">
</script>

</head>
<body>

    <div id="containerwrap">
      <div id="container">
        <span class="txtoffscreen"><a href="#content"
        title="Skip site navigation" accesskey="1">Skip site
        navigation</a> (1)</span><span class="txtoffscreen"><a
        href="#content" title="Skip section navigation"
        accesskey="2">Skip section navigation</a> (2)</span>

        <div id="headercontainer">
          <div id="header">
            <h2 class="blockhide">Header And Logo</h2>

            <div id="headerlogoleft">
              <a href=".." title="FreeBSD"><img
              src="../layout/images/logo-red.png" width="457"
              height="75" alt="FreeBSD" /></a>
            </div>

            <div id="headerlogoright">
              <h2 class="blockhide">Peripheral Links</h2>

	      <div class="frontdonateroundbox">
		<div class="frontdonatetop">
		  <div>
		    <b style="display: none;">.</b>
		  </div>
		</div>
		<div class="frontdonatecontent">
		  <a href="https://www.FreeBSDFoundation.org/donate/">Donate to FreeBSD</a>
		</div>
		<div class="frontdonatebot">
		  <div>
		    <b style="display: none;">.</b>
		  </div>
		</div>
	      </div>

              <div id="search">
		<form method="get" id="search" action="https://duckduckgo.com/">
		  <h2 class="blockhide"><label for="words">Search</label></h2>
		  <input type="hidden" name="sites" value="www.FreeBSD.org,docs.FreeBSD.org,lists.FreeBSD.org,wiki.FreeBSD.org,forums.FreeBSD.org" />
		  <input type="hidden" name="ka" value="v" />
		  <input type="hidden" name="kt" value="v" />
		  <input type="hidden" name="kh" value="1" />
		  <input type="hidden" name="kj" value="r2" />
		  <input id="words" name="q" type="text" size="20"
		    maxlength="255"
		    onfocus="if( this.value==this.defaultValue ) this.value='';"
		    value="Search" />
		  <span>&nbsp;</span>
		  <input id="submit" name="submit" type="submit" value="Search" />
		</form>
              </div>
            </div>
          </div>

          <h2 class="blockhide">Site Navigation</h2>

	  <div id="menu">
	    <ul class="first">
	      <li><a href="../">Home</a></li>
	    </ul>
	    <ul>
	      <li><a href="../about.html">About</a>
		<ul>
		  <li><a href="../projects/newbies.html">Introduction</a></li>
		  <li><a href="../features.html">Features</a></li>
		  <li><a href="../advocacy/">Advocacy</a></li>
		  <li><a href="../marketing/">Marketing</a></li>
		</ul>
	      </li>
	    </ul>
	    <ul>
	      <li><a href="../where.html">Get FreeBSD</a>
		<ul>
		  <li><a href="../releases/">Release Information</a></li>
		  <li><a href="../releng/">Release Engineering</a></li>
		</ul>
	      </li>
	    </ul>
	    <ul>
	      <li><a href="../docs.html">Documentation</a>
		<ul>
		  <li><a href="../doc/en_US.ISO8859-1/books/faq/">FAQ</a></li>
		  <li><a href="../doc/en_US.ISO8859-1/books/handbook/">Handbook</a></li>
		  <li><a href="../doc/en_US.ISO8859-1/books/porters-handbook">Porter's Handbook</a></li>
		  <li><a href="../doc/en_US.ISO8859-1/books/developers-handbook">Developer's Handbook</a></li>
		  <li><a href="../cgi/man.cgi">Manual Pages</a></li>
		  <li><a href="../doc/en_US.ISO8859-1/books/fdp-primer">Documentation Project Primer</a></li>
		  <li><a href="../docs/books.html">All Books and Articles</a></li>
		</ul>
	      </li>
	    </ul>
	    <ul>
	      <li><a href="../community.html">Community</a>
		<ul>
		  <li><a href="../community/mailinglists.html">Mailing Lists</a></li>
		  <li><a href="https://forums.FreeBSD.org">Forums</a></li>
		  <li><a href="../usergroups.html">User Groups</a></li>
		  <li><a href="../events/events.html">Events</a></li>
		</ul>
	      </li>
	    </ul>
	    <ul>
	      <li><a href="../projects/index.html">Developers</a>
		<ul>
		  <li><a href="../projects/ideas/ideas.html">Project Ideas</a></li>
		  <li><a href="//svnweb.FreeBSD.org">SVN Repository</a></li>
		  <li><a href="//p4web.FreeBSD.org">Perforce Repository</a></li>
		</ul>
	      </li>
	    </ul>
	    <ul>
	      <li><a href="../support.html">Support</a>
		<ul>
		  <li><a href="../commercial/commercial.html">Vendors</a></li>
		  <li><a href="//security.FreeBSD.org/">Security Information</a></li>
		  <li><a href="https://bugs.freebsd.org/search/">Bug Reports</a></li>
		  <li><a href="../support.html">Submit Bug-report</a></li>
		</ul>
	      </li>
	    </ul>
	    <ul>
	      <li><a href="//www.freebsdfoundation.org/">Foundation</a>
		<ul>
		  <li><a href="//www.freebsdfoundation.org/donate/">Donate</a></li>
		</ul>
	      </li>
	    </ul>
	  </div> <!-- MENU -->
        </div>

	<div id="content">

<h1>FreeBSD Man Pages</h1>

<form method="get" action="/cgi/man.cgi">
Man Page or Keyword Search:
<input value="syslog.conf" name="query" />
<input type="submit" value="Submit" />
<input type="reset" value="Reset" />
<br />
<input name="apropos" value="0" type="radio" checked="checked" /> <a href="/cgi/man.cgi?query=man&amp;sektion=1&amp;apropos=0">Man</a>
<select name="sektion">
<option value="0">All Sections</option>
<option value="1">1 - General Commands</option>
<option value="2">2 - System Calls</option>
<option value="3">3 - Subroutines</option>
<option value="4">4 - Special Files</option>
<option selected="selected" value="5">5 - File Formats</option>
<option value="6">6 - Games</option>
<option value="7">7 - Macros and Conventions</option>
<option value="8">8 - Maintenance Commands</option>
<option value="9">9 - Kernel Interface</option>
<option value="n">n - New Commands</option>
</select>
<select name="manpath">
<option value="2.8 BSD">2.8 BSD</option>
<option value="2.9.1 BSD">2.9.1 BSD</option>
<option value="2.10 BSD">2.10 BSD</option>
<option value="2.11 BSD">2.11 BSD</option>
<option value="4.3BSD NET/2">4.3BSD NET/2</option>
<option value="4.3BSD Reno">4.3BSD Reno</option>
<option value="4.4BSD Lite2">4.4BSD Lite2</option>
<option value="386BSD 0.0">386BSD 0.0</option>
<option value="386BSD 0.1">386BSD 0.1</option>
<option value="CentOS 5.6">CentOS 5.6</option>
<option value="CentOS 5.7">CentOS 5.7</option>
<option value="CentOS 5.8">CentOS 5.8</option>
<option value="CentOS 5.9">CentOS 5.9</option>
<option value="CentOS 5.10">CentOS 5.10</option>
<option value="CentOS 5.11">CentOS 5.11</option>
<option value="CentOS 6.0">CentOS 6.0</option>
<option value="CentOS 6.1">CentOS 6.1</option>
<option value="CentOS 6.2">CentOS 6.2</option>
<option value="CentOS 6.3">CentOS 6.3</option>
<option value="CentOS 6.4">CentOS 6.4</option>
<option value="CentOS 6.5">CentOS 6.5</option>
<option value="CentOS 6.6">CentOS 6.6</option>
<option value="CentOS 7.0">CentOS 7.0</option>
<option value="CentOS 7.1">CentOS 7.1</option>
<option value="CentOS Linux/i386 3.9">CentOS Linux/i386 3.9</option>
<option value="CentOS Linux/i386 4.8">CentOS Linux/i386 4.8</option>
<option value="CentOS Linux/i386 5.4">CentOS Linux/i386 5.4</option>
<option value="CentOS Linux/i386 5.5">CentOS Linux/i386 5.5</option>
<option value="Darwin 1.3.1/x86">Darwin 1.3.1/x86</option>
<option value="Darwin 1.4.1/x86">Darwin 1.4.1/x86</option>
<option value="Darwin 6.0.2/x86">Darwin 6.0.2/x86</option>
<option value="Darwin 7.0.1">Darwin 7.0.1</option>
<option value="Darwin 8.0.1/ppc">Darwin 8.0.1/ppc</option>
<option value="Debian 2.2.7">Debian 2.2.7</option>
<option value="Debian 3.1.8">Debian 3.1.8</option>
<option value="Debian 4.0.9">Debian 4.0.9</option>
<option value="Debian 5.0.10">Debian 5.0.10</option>
<option value="Debian 6.0.10">Debian 6.0.10</option>
<option value="Debian 7.8.0">Debian 7.8.0</option>
<option value="Debian 8.1.0">Debian 8.1.0</option>
<option value="FreeBSD 1.0-RELEASE">FreeBSD 1.0-RELEASE</option>
<option value="FreeBSD 1.1-RELEASE">FreeBSD 1.1-RELEASE</option>
<option value="FreeBSD 1.1.5.1-RELEASE">FreeBSD 1.1.5.1-RELEASE</option>
<option value="FreeBSD 2.0-RELEASE">FreeBSD 2.0-RELEASE</option>
<option value="FreeBSD 2.0.5-RELEASE">FreeBSD 2.0.5-RELEASE</option>
<option value="FreeBSD 2.1.0-RELEASE">FreeBSD 2.1.0-RELEASE</option>
<option value="FreeBSD 2.1.5-RELEASE">FreeBSD 2.1.5-RELEASE</option>
<option value="FreeBSD 2.1.6.1-RELEASE">FreeBSD 2.1.6.1-RELEASE</option>
<option value="FreeBSD 2.1.7.1-RELEASE">FreeBSD 2.1.7.1-RELEASE</option>
<option value="FreeBSD 2.2.1-RELEASE">FreeBSD 2.2.1-RELEASE</option>
<option value="FreeBSD 2.2.2-RELEASE">FreeBSD 2.2.2-RELEASE</option>
<option value="FreeBSD 2.2.5-RELEASE">FreeBSD 2.2.5-RELEASE</option>
<option value="FreeBSD 2.2.6-RELEASE">FreeBSD 2.2.6-RELEASE</option>
<option value="FreeBSD 2.2.7-RELEASE">FreeBSD 2.2.7-RELEASE</option>
<option value="FreeBSD 2.2.8-RELEASE">FreeBSD 2.2.8-RELEASE</option>
<option value="FreeBSD 2.2.8-RELEASE and Ports">FreeBSD 2.2.8-RELEASE and Ports</option>
<option value="FreeBSD 3.0-RELEASE">FreeBSD 3.0-RELEASE</option>
<option value="FreeBSD 3.1-RELEASE">FreeBSD 3.1-RELEASE</option>
<option value="FreeBSD 3.2-RELEASE">FreeBSD 3.2-RELEASE</option>
<option value="FreeBSD 3.3-RELEASE">FreeBSD 3.3-RELEASE</option>
<option value="FreeBSD 3.4-RELEASE">FreeBSD 3.4-RELEASE</option>
<option value="FreeBSD 3.4-RELEASE and Ports">FreeBSD 3.4-RELEASE and Ports</option>
<option value="FreeBSD 3.5-RELEASE and Ports">FreeBSD 3.5-RELEASE and Ports</option>
<option value="FreeBSD 3.5.1-RELEASE">FreeBSD 3.5.1-RELEASE</option>
<option value="FreeBSD 3.5.1-RELEASE and Ports">FreeBSD 3.5.1-RELEASE and Ports</option>
<option value="FreeBSD 4.0-RELEASE">FreeBSD 4.0-RELEASE</option>
<option value="FreeBSD 4.1-RELEASE">FreeBSD 4.1-RELEASE</option>
<option value="FreeBSD 4.1.1-RELEASE">FreeBSD 4.1.1-RELEASE</option>
<option value="FreeBSD 4.1.1-RELEASE and Ports">FreeBSD 4.1.1-RELEASE and Ports</option>
<option value="FreeBSD 4.2-RELEASE">FreeBSD 4.2-RELEASE</option>
<option value="FreeBSD 4.2-RELEASE and Ports">FreeBSD 4.2-RELEASE and Ports</option>
<option value="FreeBSD 4.3-RELEASE">FreeBSD 4.3-RELEASE</option>
<option value="FreeBSD 4.3-RELEASE and Ports">FreeBSD 4.3-RELEASE and Ports</option>
<option value="FreeBSD 4.4-RELEASE">FreeBSD 4.4-RELEASE</option>
<option value="FreeBSD 4.5-RELEASE">FreeBSD 4.5-RELEASE</option>
<option value="FreeBSD 4.5-RELEASE and Ports">FreeBSD 4.5-RELEASE and Ports</option>
<option value="FreeBSD 4.6-RELEASE">FreeBSD 4.6-RELEASE</option>
<option value="FreeBSD 4.6-RELEASE and Ports">FreeBSD 4.6-RELEASE and Ports</option>
<option value="FreeBSD 4.6.2-RELEASE">FreeBSD 4.6.2-RELEASE</option>
<option value="FreeBSD 4.6.2-RELEASE and Ports">FreeBSD 4.6.2-RELEASE and Ports</option>
<option value="FreeBSD 4.7-RELEASE">FreeBSD 4.7-RELEASE</option>
<option value="FreeBSD 4.8-RELEASE">FreeBSD 4.8-RELEASE</option>
<option value="FreeBSD 4.8-RELEASE and Ports">FreeBSD 4.8-RELEASE and Ports</option>
<option value="FreeBSD 4.9-RELEASE">FreeBSD 4.9-RELEASE</option>
<option value="FreeBSD 4.9-RELEASE and Ports">FreeBSD 4.9-RELEASE and Ports</option>
<option value="FreeBSD 4.10-RELEASE">FreeBSD 4.10-RELEASE</option>
<option value="FreeBSD 4.10-RELEASE and Ports">FreeBSD 4.10-RELEASE and Ports</option>
<option value="FreeBSD 4.11-RELEASE">FreeBSD 4.11-RELEASE</option>
<option value="FreeBSD 4.11-RELEASE and Ports">FreeBSD 4.11-RELEASE and Ports</option>
<option value="FreeBSD 5.0-RELEASE">FreeBSD 5.0-RELEASE</option>
<option value="FreeBSD 5.1-RELEASE">FreeBSD 5.1-RELEASE</option>
<option value="FreeBSD 5.2-RELEASE">FreeBSD 5.2-RELEASE</option>
<option value="FreeBSD 5.2-RELEASE and Ports">FreeBSD 5.2-RELEASE and Ports</option>
<option value="FreeBSD 5.2.1-RELEASE">FreeBSD 5.2.1-RELEASE</option>
<option value="FreeBSD 5.2.1-RELEASE and Ports">FreeBSD 5.2.1-RELEASE and Ports</option>
<option value="FreeBSD 5.3-RELEASE">FreeBSD 5.3-RELEASE</option>
<option value="FreeBSD 5.3-RELEASE and Ports">FreeBSD 5.3-RELEASE and Ports</option>
<option value="FreeBSD 5.4-RELEASE">FreeBSD 5.4-RELEASE</option>
<option value="FreeBSD 5.4-RELEASE and Ports">FreeBSD 5.4-RELEASE and Ports</option>
<option value="FreeBSD 5.5-RELEASE">FreeBSD 5.5-RELEASE</option>
<option value="FreeBSD 5.5-RELEASE and Ports">FreeBSD 5.5-RELEASE and Ports</option>
<option value="FreeBSD 6.0-RELEASE">FreeBSD 6.0-RELEASE</option>
<option value="FreeBSD 6.0-RELEASE and Ports">FreeBSD 6.0-RELEASE and Ports</option>
<option value="FreeBSD 6.1-RELEASE">FreeBSD 6.1-RELEASE</option>
<option value="FreeBSD 6.2-RELEASE">FreeBSD 6.2-RELEASE</option>
<option value="FreeBSD 6.3-RELEASE">FreeBSD 6.3-RELEASE</option>
<option value="FreeBSD 6.3-RELEASE and Ports">FreeBSD 6.3-RELEASE and Ports</option>
<option value="FreeBSD 6.4-RELEASE">FreeBSD 6.4-RELEASE</option>
<option value="FreeBSD 6.4-RELEASE and Ports">FreeBSD 6.4-RELEASE and Ports</option>
<option value="FreeBSD 6.4-stable">FreeBSD 6.4-stable</option>
<option value="FreeBSD 7.0-RELEASE">FreeBSD 7.0-RELEASE</option>
<option value="FreeBSD 7.1-RELEASE">FreeBSD 7.1-RELEASE</option>
<option value="FreeBSD 7.1-RELEASE and Ports">FreeBSD 7.1-RELEASE and Ports</option>
<option value="FreeBSD 7.2-RELEASE">FreeBSD 7.2-RELEASE</option>
<option value="FreeBSD 7.2-RELEASE and Ports">FreeBSD 7.2-RELEASE and Ports</option>
<option value="FreeBSD 7.3-RELEASE">FreeBSD 7.3-RELEASE</option>
<option value="FreeBSD 7.3-RELEASE and Ports">FreeBSD 7.3-RELEASE and Ports</option>
<option value="FreeBSD 7.4-RELEASE">FreeBSD 7.4-RELEASE</option>
<option value="FreeBSD 7.4-RELEASE and Ports">FreeBSD 7.4-RELEASE and Ports</option>
<option value="FreeBSD 7.4-stable">FreeBSD 7.4-stable</option>
<option value="FreeBSD 8.0-RELEASE">FreeBSD 8.0-RELEASE</option>
<option value="FreeBSD 8.0-RELEASE and Ports">FreeBSD 8.0-RELEASE and Ports</option>
<option value="FreeBSD 8.1-RELEASE">FreeBSD 8.1-RELEASE</option>
<option value="FreeBSD 8.1-RELEASE and Ports">FreeBSD 8.1-RELEASE and Ports</option>
<option value="FreeBSD 8.2-RELEASE">FreeBSD 8.2-RELEASE</option>
<option value="FreeBSD 8.2-RELEASE and Ports">FreeBSD 8.2-RELEASE and Ports</option>
<option value="FreeBSD 8.3-RELEASE">FreeBSD 8.3-RELEASE</option>
<option value="FreeBSD 8.3-RELEASE and Ports">FreeBSD 8.3-RELEASE and Ports</option>
<option value="FreeBSD 8.4-RELEASE">FreeBSD 8.4-RELEASE</option>
<option value="FreeBSD 8.4-RELEASE and Ports">FreeBSD 8.4-RELEASE and Ports</option>
<option value="FreeBSD 8.4-stable">FreeBSD 8.4-stable</option>
<option value="FreeBSD 9.0-RELEASE">FreeBSD 9.0-RELEASE</option>
<option value="FreeBSD 9.0-RELEASE and Ports">FreeBSD 9.0-RELEASE and Ports</option>
<option value="FreeBSD 9.1-RELEASE">FreeBSD 9.1-RELEASE</option>
<option value="FreeBSD 9.1-RELEASE and Ports">FreeBSD 9.1-RELEASE and Ports</option>
<option value="FreeBSD 9.2-RELEASE">FreeBSD 9.2-RELEASE</option>
<option value="FreeBSD 9.2-RELEASE and Ports">FreeBSD 9.2-RELEASE and Ports</option>
<option value="FreeBSD 9.3-RELEASE">FreeBSD 9.3-RELEASE</option>
<option value="FreeBSD 9.3-RELEASE and Ports">FreeBSD 9.3-RELEASE and Ports</option>
<option value="FreeBSD 9.3-stable">FreeBSD 9.3-stable</option>
<option value="FreeBSD 10.0-RELEASE">FreeBSD 10.0-RELEASE</option>
<option value="FreeBSD 10.0-RELEASE and Ports">FreeBSD 10.0-RELEASE and Ports</option>
<option value="FreeBSD 10.1-RELEASE">FreeBSD 10.1-RELEASE</option>
<option value="FreeBSD 10.1-RELEASE and Ports">FreeBSD 10.1-RELEASE and Ports</option>
<option value="FreeBSD 10.2-RELEASE">FreeBSD 10.2-RELEASE</option>
<option value="FreeBSD 10.2-RELEASE and Ports">FreeBSD 10.2-RELEASE and Ports</option>
<option value="FreeBSD 10.2-stable">FreeBSD 10.2-stable</option>
<option value="FreeBSD 10.3-RELEASE">FreeBSD 10.3-RELEASE</option>
<option value="FreeBSD 10.3-RELEASE and Ports">FreeBSD 10.3-RELEASE and Ports</option>
<option value="FreeBSD 10.3-stable">FreeBSD 10.3-stable</option>
<option value="FreeBSD 11-current">FreeBSD 11-current</option>
<option value="FreeBSD 11.0-RELEASE">FreeBSD 11.0-RELEASE</option>
<option value="FreeBSD 11.0-RELEASE and Ports">FreeBSD 11.0-RELEASE and Ports</option>
<option value="FreeBSD 11.0-stable">FreeBSD 11.0-stable</option>
<option value="FreeBSD 12-current">FreeBSD 12-current</option>
<option value="FreeBSD Ports 2.2.8-RELEASE">FreeBSD Ports 2.2.8-RELEASE</option>
<option value="FreeBSD Ports 3.4-RELEASE">FreeBSD Ports 3.4-RELEASE</option>
<option value="FreeBSD Ports 3.5-RELEASE">FreeBSD Ports 3.5-RELEASE</option>
<option value="FreeBSD Ports 3.5.1-RELEASE">FreeBSD Ports 3.5.1-RELEASE</option>
<option value="FreeBSD Ports 4.1.1-RELEASE">FreeBSD Ports 4.1.1-RELEASE</option>
<option value="FreeBSD Ports 4.2-RELEASE">FreeBSD Ports 4.2-RELEASE</option>
<option value="FreeBSD Ports 4.3-RELEASE">FreeBSD Ports 4.3-RELEASE</option>
<option value="FreeBSD Ports 4.5-RELEASE">FreeBSD Ports 4.5-RELEASE</option>
<option value="FreeBSD Ports 4.6-RELEASE">FreeBSD Ports 4.6-RELEASE</option>
<option value="FreeBSD Ports 4.6.2-RELEASE">FreeBSD Ports 4.6.2-RELEASE</option>
<option value="FreeBSD Ports 4.7-RELEASE">FreeBSD Ports 4.7-RELEASE</option>
<option value="FreeBSD Ports 4.8-RELEASE">FreeBSD Ports 4.8-RELEASE</option>
<option value="FreeBSD Ports 4.9-RELEASE">FreeBSD Ports 4.9-RELEASE</option>
<option value="FreeBSD Ports 4.10-RELEASE">FreeBSD Ports 4.10-RELEASE</option>
<option value="FreeBSD Ports 4.11-RELEASE">FreeBSD Ports 4.11-RELEASE</option>
<option value="FreeBSD Ports 5.1-RELEASE">FreeBSD Ports 5.1-RELEASE</option>
<option value="FreeBSD Ports 5.2-RELEASE">FreeBSD Ports 5.2-RELEASE</option>
<option value="FreeBSD Ports 5.2.1-RELEASE">FreeBSD Ports 5.2.1-RELEASE</option>
<option value="FreeBSD Ports 5.3-RELEASE">FreeBSD Ports 5.3-RELEASE</option>
<option value="FreeBSD Ports 5.4-RELEASE">FreeBSD Ports 5.4-RELEASE</option>
<option value="FreeBSD Ports 5.5-RELEASE">FreeBSD Ports 5.5-RELEASE</option>
<option value="FreeBSD Ports 6.0-RELEASE">FreeBSD Ports 6.0-RELEASE</option>
<option value="FreeBSD Ports 6.2-RELEASE">FreeBSD Ports 6.2-RELEASE</option>
<option value="FreeBSD Ports 6.3-RELEASE">FreeBSD Ports 6.3-RELEASE</option>
<option value="FreeBSD Ports 6.4-RELEASE">FreeBSD Ports 6.4-RELEASE</option>
<option value="FreeBSD Ports 7.0-RELEASE">FreeBSD Ports 7.0-RELEASE</option>
<option value="FreeBSD Ports 7.1-RELEASE">FreeBSD Ports 7.1-RELEASE</option>
<option value="FreeBSD Ports 7.2-RELEASE">FreeBSD Ports 7.2-RELEASE</option>
<option value="FreeBSD Ports 7.3-RELEASE">FreeBSD Ports 7.3-RELEASE</option>
<option value="FreeBSD Ports 7.4-RELEASE">FreeBSD Ports 7.4-RELEASE</option>
<option value="FreeBSD Ports 8.0-RELEASE">FreeBSD Ports 8.0-RELEASE</option>
<option value="FreeBSD Ports 8.1-RELEASE">FreeBSD Ports 8.1-RELEASE</option>
<option value="FreeBSD Ports 8.2-RELEASE">FreeBSD Ports 8.2-RELEASE</option>
<option value="FreeBSD Ports 8.3-RELEASE">FreeBSD Ports 8.3-RELEASE</option>
<option value="FreeBSD Ports 8.4-RELEASE">FreeBSD Ports 8.4-RELEASE</option>
<option value="FreeBSD Ports 9.0-RELEASE">FreeBSD Ports 9.0-RELEASE</option>
<option value="FreeBSD Ports 9.1-RELEASE">FreeBSD Ports 9.1-RELEASE</option>
<option value="FreeBSD Ports 9.2-RELEASE">FreeBSD Ports 9.2-RELEASE</option>
<option value="FreeBSD Ports 9.3-RELEASE">FreeBSD Ports 9.3-RELEASE</option>
<option value="FreeBSD Ports 10.0-RELEASE">FreeBSD Ports 10.0-RELEASE</option>
<option value="FreeBSD Ports 10.1-RELEASE">FreeBSD Ports 10.1-RELEASE</option>
<option value="FreeBSD Ports 10.2-RELEASE">FreeBSD Ports 10.2-RELEASE</option>
<option value="FreeBSD Ports 10.3-RELEASE">FreeBSD Ports 10.3-RELEASE</option>
<option value="FreeBSD Ports 11.0-RELEASE">FreeBSD Ports 11.0-RELEASE</option>
<option value="HP-UX 10.01">HP-UX 10.01</option>
<option value="HP-UX 10.10">HP-UX 10.10</option>
<option value="HP-UX 10.20">HP-UX 10.20</option>
<option value="HP-UX 11.00">HP-UX 11.00</option>
<option value="HP-UX 11.11">HP-UX 11.11</option>
<option value="HP-UX 11.20">HP-UX 11.20</option>
<option value="HP-UX 11.22">HP-UX 11.22</option>
<option value="Linux Slackware 3.1">Linux Slackware 3.1</option>
<option value="Minix 2.0">Minix 2.0</option>
<option value="NetBSD 1.0">NetBSD 1.0</option>
<option value="NetBSD 1.1">NetBSD 1.1</option>
<option value="NetBSD 1.2">NetBSD 1.2</option>
<option value="NetBSD 1.2.1">NetBSD 1.2.1</option>
<option value="NetBSD 1.3">NetBSD 1.3</option>
<option value="NetBSD 1.3.1">NetBSD 1.3.1</option>
<option value="NetBSD 1.3.2">NetBSD 1.3.2</option>
<option value="NetBSD 1.3.3">NetBSD 1.3.3</option>
<option value="NetBSD 1.4">NetBSD 1.4</option>
<option value="NetBSD 1.4.1">NetBSD 1.4.1</option>
<option value="NetBSD 1.4.2">NetBSD 1.4.2</option>
<option value="NetBSD 1.4.3">NetBSD 1.4.3</option>
<option value="NetBSD 1.5">NetBSD 1.5</option>
<option value="NetBSD 1.5.1">NetBSD 1.5.1</option>
<option value="NetBSD 1.5.2">NetBSD 1.5.2</option>
<option value="NetBSD 1.5.3">NetBSD 1.5.3</option>
<option value="NetBSD 1.6">NetBSD 1.6</option>
<option value="NetBSD 1.6.1">NetBSD 1.6.1</option>
<option value="NetBSD 1.6.2">NetBSD 1.6.2</option>
<option value="NetBSD 2.0">NetBSD 2.0</option>
<option value="NetBSD 2.0.2">NetBSD 2.0.2</option>
<option value="NetBSD 2.1">NetBSD 2.1</option>
<option value="NetBSD 3.0">NetBSD 3.0</option>
<option value="NetBSD 3.1">NetBSD 3.1</option>
<option value="NetBSD 4.0">NetBSD 4.0</option>
<option value="NetBSD 4.0.1">NetBSD 4.0.1</option>
<option value="NetBSD 5.0">NetBSD 5.0</option>
<option value="NetBSD 5.1">NetBSD 5.1</option>
<option value="NetBSD 6.0">NetBSD 6.0</option>
<option value="NetBSD 6.1.5">NetBSD 6.1.5</option>
<option value="NetBSD 7.0">NetBSD 7.0</option>
<option value="OpenBSD 2.0">OpenBSD 2.0</option>
<option value="OpenBSD 2.1">OpenBSD 2.1</option>
<option value="OpenBSD 2.2">OpenBSD 2.2</option>
<option value="OpenBSD 2.3">OpenBSD 2.3</option>
<option value="OpenBSD 2.4">OpenBSD 2.4</option>
<option value="OpenBSD 2.5">OpenBSD 2.5</option>
<option value="OpenBSD 2.6">OpenBSD 2.6</option>
<option value="OpenBSD 2.7">OpenBSD 2.7</option>
<option value="OpenBSD 2.8">OpenBSD 2.8</option>
<option value="OpenBSD 2.9">OpenBSD 2.9</option>
<option value="OpenBSD 3.0">OpenBSD 3.0</option>
<option value="OpenBSD 3.1">OpenBSD 3.1</option>
<option value="OpenBSD 3.2">OpenBSD 3.2</option>
<option value="OpenBSD 3.3">OpenBSD 3.3</option>
<option value="OpenBSD 3.4">OpenBSD 3.4</option>
<option value="OpenBSD 3.5">OpenBSD 3.5</option>
<option value="OpenBSD 3.6">OpenBSD 3.6</option>
<option value="OpenBSD 3.7">OpenBSD 3.7</option>
<option value="OpenBSD 3.8">OpenBSD 3.8</option>
<option value="OpenBSD 3.9">OpenBSD 3.9</option>
<option value="OpenBSD 4.0">OpenBSD 4.0</option>
<option value="OpenBSD 4.1">OpenBSD 4.1</option>
<option value="OpenBSD 4.2">OpenBSD 4.2</option>
<option value="OpenBSD 4.3">OpenBSD 4.3</option>
<option value="OpenBSD 4.4">OpenBSD 4.4</option>
<option value="OpenBSD 4.5">OpenBSD 4.5</option>
<option value="OpenBSD 4.6">OpenBSD 4.6</option>
<option value="OpenBSD 4.7">OpenBSD 4.7</option>
<option value="OpenBSD 4.8">OpenBSD 4.8</option>
<option value="OpenBSD 4.9">OpenBSD 4.9</option>
<option value="OpenBSD 5.0">OpenBSD 5.0</option>
<option value="OpenBSD 5.1">OpenBSD 5.1</option>
<option value="OpenBSD 5.2">OpenBSD 5.2</option>
<option value="OpenBSD 5.3">OpenBSD 5.3</option>
<option value="OpenBSD 5.4">OpenBSD 5.4</option>
<option value="OpenBSD 5.5">OpenBSD 5.5</option>
<option value="OpenBSD 5.6">OpenBSD 5.6</option>
<option value="OpenBSD 5.7">OpenBSD 5.7</option>
<option value="OpenBSD 5.8">OpenBSD 5.8</option>
<option value="OpenDarwin 6.6.1/x86">OpenDarwin 6.6.1/x86</option>
<option value="OpenDarwin 6.6.2/x86">OpenDarwin 6.6.2/x86</option>
<option value="OpenDarwin 7.2.1">OpenDarwin 7.2.1</option>
<option value="OpenDarwin 20030208pre4/ppc">OpenDarwin 20030208pre4/ppc</option>
<option value="OSF1 V4.0/alpha">OSF1 V4.0/alpha</option>
<option value="OSF1 V5.1/alpha">OSF1 V5.1/alpha</option>
<option value="Plan 9">Plan 9</option>
<option value="Red Hat Linux/i386 4.2">Red Hat Linux/i386 4.2</option>
<option value="Red Hat Linux/i386 5.0">Red Hat Linux/i386 5.0</option>
<option value="Red Hat Linux/i386 5.2">Red Hat Linux/i386 5.2</option>
<option value="Red Hat Linux/i386 6.1">Red Hat Linux/i386 6.1</option>
<option value="Red Hat Linux/i386 6.2">Red Hat Linux/i386 6.2</option>
<option value="Red Hat Linux/i386 7.0">Red Hat Linux/i386 7.0</option>
<option value="Red Hat Linux/i386 7.1">Red Hat Linux/i386 7.1</option>
<option value="Red Hat Linux/i386 7.2">Red Hat Linux/i386 7.2</option>
<option value="Red Hat Linux/i386 7.3">Red Hat Linux/i386 7.3</option>
<option value="Red Hat Linux/i386 8.0">Red Hat Linux/i386 8.0</option>
<option value="Red Hat Linux/i386 9">Red Hat Linux/i386 9</option>
<option value="SunOS 4.1.3">SunOS 4.1.3</option>
<option value="SunOS 5.5.1">SunOS 5.5.1</option>
<option value="SunOS 5.6">SunOS 5.6</option>
<option value="SunOS 5.7">SunOS 5.7</option>
<option value="SunOS 5.8">SunOS 5.8</option>
<option value="SunOS 5.9">SunOS 5.9</option>
<option value="SunOS 5.10">SunOS 5.10</option>
<option value="SuSE Linux/i386 4.3">SuSE Linux/i386 4.3</option>
<option value="SuSE Linux/i386 5.0">SuSE Linux/i386 5.0</option>
<option value="SuSE Linux/i386 5.2">SuSE Linux/i386 5.2</option>
<option value="SuSE Linux/i386 5.3">SuSE Linux/i386 5.3</option>
<option value="SuSE Linux/i386 6.0">SuSE Linux/i386 6.0</option>
<option value="SuSE Linux/i386 6.1">SuSE Linux/i386 6.1</option>
<option value="SuSE Linux/i386 6.3">SuSE Linux/i386 6.3</option>
<option value="SuSE Linux/i386 6.4">SuSE Linux/i386 6.4</option>
<option value="SuSE Linux/i386 7.0">SuSE Linux/i386 7.0</option>
<option value="SuSE Linux/i386 7.1">SuSE Linux/i386 7.1</option>
<option value="SuSE Linux/i386 7.2">SuSE Linux/i386 7.2</option>
<option value="SuSE Linux/i386 7.3">SuSE Linux/i386 7.3</option>
<option value="SuSE Linux/i386 8.0">SuSE Linux/i386 8.0</option>
<option value="SuSE Linux/i386 8.1">SuSE Linux/i386 8.1</option>
<option value="SuSE Linux/i386 8.2">SuSE Linux/i386 8.2</option>
<option value="SuSE Linux/i386 9.2">SuSE Linux/i386 9.2</option>
<option value="SuSE Linux/i386 9.3">SuSE Linux/i386 9.3</option>
<option value="SuSE Linux/i386 10.0">SuSE Linux/i386 10.0</option>
<option selected="selected" value="SuSE Linux/i386 10.1">SuSE Linux/i386 10.1</option>
<option value="SuSE Linux/i386 10.2">SuSE Linux/i386 10.2</option>
<option value="SuSE Linux/i386 10.3">SuSE Linux/i386 10.3</option>
<option value="SuSE Linux/i386 11.0">SuSE Linux/i386 11.0</option>
<option value="SuSE Linux/i386 11.1">SuSE Linux/i386 11.1</option>
<option value="SuSE Linux/i386 11.2">SuSE Linux/i386 11.2</option>
<option value="SuSE Linux/i386 11.3">SuSE Linux/i386 11.3</option>
<option value="SuSE Linux/i386 ES 10 SP1">SuSE Linux/i386 ES 10 SP1</option>
<option value="ULTRIX 4.2">ULTRIX 4.2</option>
<option value="Unix Seventh Edition">Unix Seventh Edition</option>
<option value="X11R6.7.0">X11R6.7.0</option>
<option value="X11R6.8.2">X11R6.8.2</option>
<option value="X11R6.9.0">X11R6.9.0</option>
<option value="X11R7.2">X11R7.2</option>
<option value="X11R7.3.2">X11R7.3.2</option>
<option value="X11R7.4">X11R7.4</option>
<option value="XFree86 2.1">XFree86 2.1</option>
<option value="XFree86 3.3">XFree86 3.3</option>
<option value="XFree86 3.3.6">XFree86 3.3.6</option>
<option value="XFree86 4.0">XFree86 4.0</option>
<option value="XFree86 4.0.1">XFree86 4.0.1</option>
<option value="XFree86 4.0.2">XFree86 4.0.2</option>
<option value="XFree86 4.1.0">XFree86 4.1.0</option>
<option value="XFree86 4.2.0">XFree86 4.2.0</option>
<option value="XFree86 4.2.99.3">XFree86 4.2.99.3</option>
<option value="XFree86 4.3.0">XFree86 4.3.0</option>
<option value="XFree86 4.4.0">XFree86 4.4.0</option>
<option value="XFree86 4.5.0">XFree86 4.5.0</option>
<option value="XFree86 4.6.0">XFree86 4.6.0</option>
<option value="XFree86 4.7.0">XFree86 4.7.0</option>
</select>
<select name="arch">
<option  value="default">default</option>
<option  value="i386">i386</option>
</select>
Architecture

<br />
<input name="apropos" value="1" type="radio" /> <a href="/cgi/man.cgi?query=apropos&amp;sektion=1&amp;apropos=0">Apropos</a> Keyword Search (all sections)
<select name="format">
<option value="html">html</option>
<option value="pdf">pdf</option>
<option value="ascii">ascii</option>
</select>
Output format
</form>

<a href="/cgi/man.cgi?manpath=SuSE+Linux%2fi386+10.1">home</a> |
<a href="/cgi/man.cgi/help.html">help</a> 
<hr />
<pre>
SYSLOG.CONF(5)            Linux System Administration           SYSLOG.CONF(5)

<a name="NAME" href="#end"><b>NAME</b></a>
       syslog.conf - <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1">syslogd(8)</a> configuration file

<a name="DESCRIPTION" href="#end"><b>DESCRIPTION</b></a>
       The <i>syslog.conf</i> file is the main configuration file for the <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a>
       which logs system messages on *nix systems.  This file specifies rules
       for logging.  For special features see the <a href="/cgi/man.cgi?query=sysklogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>sysklogd</b>(8)</a> manpage.

       Every rule consists of two fields, a <i>selector</i> field and an <i>action</i>
       field.  These two fields are separated by one or more spaces or tabs.
       The selector field specifies a pattern of facilities and priorities
       belonging to the specified action.

       Lines starting with a hash mark (``#'') and empty lines are ignored.

       This release of <b>syslogd</b> is able to understand an extended syntax.  One
       rule can be divided into several lines if the leading line is
       terminated with an backslash (``\'').

<a name="SELECTORS" href="#end"><b>SELECTORS</b></a>
       The selector field itself again consists of two parts, a <i>facility</i> and a
       <i>priority</i>, separated by a period (``.'').  Both parts are case
       insensitive and can also be specified as decimal numbers, but don't do
       that, you have been warned.  Both facilities and priorities are
       described in <a href="/cgi/man.cgi?query=syslog&amp;sektion=3&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslog</b>(3)</a>.  The names mentioned below correspond to the
       similar <b>LOG_</b>-values in <i>/usr/include/syslog.h</i>.

       The <i>facility</i> is one of the following keywords: <b>auth</b>, <b>authpriv</b>, <b>cron</b>,
       <b>daemon</b>, <b>kern</b>, <b>lpr</b>,  <b>mail</b>, <b>mark</b>, <b>news</b>, <b>security</b> (same as <b>auth</b>),  <b>syslog</b>,
       <b>user</b>, <b>uucp</b> and <b>local0</b> through <b>local7</b>.  The keyword <b>security</b> should not
       be used anymore and <b>mark</b> is only for internal use and therefore should
       not be used in applications.  Anyway, you may want to specify and
       redirect these messages here.  The <i>facility</i> specifies the subsystem
       that produced the message, i.e. all mail programs log with the mail
       facility (<b>LOG_MAIL</b>) if they log using syslog.

       The <i>priority</i> is one of the following keywords, in ascending order:
       <b>debug</b>, <b>info</b>, <b>notice</b>, <b>warning</b>, <b>warn</b> (same as  <b>warning</b>), <b>err</b>, <b>error</b> (same
       as <b>err</b>), <b>crit</b>,  <b>alert</b>, <b>emerg</b>, <b>panic</b> (same as <b>emerg</b>).  The keywords
       <b>error</b>, <b>warn</b> and <b>panic</b> are deprecated and should not be used anymore.
       The <i>priority</i> defines the severity of the message

       The behavior of the original BSD syslogd is that all messages of the
       specified priority and higher are logged according to the given action.
       This <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a> behaves the same, but has some extensions.

       In addition to the above mentioned names the <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a> understands the
       following extensions: An asterisk (``*'') stands for all facilities or
       all priorities, depending on where it is used (before or after the
       period).  The keyword <b>none</b> stands for no priority of the given
       facility.

       You can specify multiple facilities with the same priority pattern in
       one statement using the comma (``,'') operator.  You may specify as
       much facilities as you want.  Remember that only the facility part from
       such a statement is taken, a priority part would be skipped.

       Multiple selectors may be specified for a single <i>action</i> using the
       semicolon (``;'') separator.  Remember that each selector in the
       <i>selector</i> field is capable to overwrite the preceding ones.  Using this
       behavior you can exclude some priorities from the pattern.

       This <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a> has a syntax extension to the original BSD source, that
       makes its use more intuitively.  You may precede every priority with an
       equation sign (``='') to specify only this single priority and not any
       of the above.  You may also (both is valid, too) precede the priority
       with an exclamation mark (``!'') to ignore all that priorities, either
       exact this one or this and any higher priority.  If you use both
       extensions than the exclamation mark must occur before the equation
       sign, just use it intuitively.

<a name="ACTIONS" href="#end"><b>ACTIONS</b></a>
       The action field of a rule describes the abstract term ``logfile''.  A
       ``logfile'' need not to be a real file, btw.  The <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a> provides
       the following actions.

   <b>Regular</b> <b>File</b>
       Typically messages are logged to real files.  The file has to be
       specified with full pathname, beginning with a slash ``/''.

       You may prefix each entry with the minus ``-'' sign to omit syncing the
       file after every logging.  Note that you might lose information if the
       system crashes right behind a write attempt.  Nevertheless this might
       give you back some performance, especially if you run programs that use
       logging in a very verbose manner.

   <b>Named</b> <b>Pipes</b>
       This version of <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a> has support for logging output  to named
       pipes (fifos).  A fifo or named pipe can be used as a destination for
       log messages by prepending a pipe symbol (``|'') to the name of the
       file.  This is handy for debugging.  Note that the fifo must be created
       with the <a href="/cgi/man.cgi?query=mkfifo&amp;sektion=1&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>mkfifo</b>(1)</a> command  before <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a> is started.

   <b>Unix</b> <b>Socket</b> <b>(UDP)</b>
       This version of <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a> has support for logging output to named
       sockets (UDP UNIX domain sockets).  A named socket can be used as a
       destination for log messages by prepending a double at-sign symbol
       (``@@'') to the pathname of the socket file. This feature is useful for
       applications that need to process all logged messages.  All they need
       to do is open the named socket for reading and then process the
       messages as they are received.

   <b>Terminal</b> <b>and</b> <b>Console</b>
       If the file you specified is a tty, special tty-handling is done, same
       with <i>/dev/console</i>.

   <b>Remote</b> <b>Machine</b>
       This <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a> provides full remote logging, i.e. is able to send
       messages to a remote host running <a href="/cgi/man.cgi?query=syslogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslogd</b>(8)</a> and to receive messages
       from remote hosts.  The remote host won't forward the message again, it
       will just log them locally.  To forward messages to another host,
       prepend the hostname with the at sign (``@'').

       Using this feature you're able to control all syslog messages on one
       host, if all other machines will log remotely to that.  This tears down
       administration needs.

   <b>List</b> <b>of</b> <b>Users</b>
       Usually critical messages are also directed to ``root'' on that
       machine.  You can specify a list of users that shall get the message by
       simply writing the login.  You may specify more than one user by
       separating them with commas (``,'').  If they're logged in they get the
       message.  Don't think a mail would be sent, that might be too late.

   <b>Everyone</b> <b>logged</b> <b>on</b>
       Emergency messages often go to all users currently online to notify
       them that something strange is happening with the system.  To specify
       this <a href="/cgi/man.cgi?query=wall&amp;sektion=1&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><i>wall</i>(1)</a>-feature use an asterisk (``*'').

<a name="EXAMPLES" href="#end"><b>EXAMPLES</b></a>
       Here are some example, partially taken from a real existing site and
       configuration.  Hopefully they rub out all questions to the
       configuration, if not, drop me (Joey) a line.

              # Store critical stuff in critical
              #
              *.=crit;kern.none            /var/adm/critical

       This will store all messages with the priority <b>crit</b> in the file
       <i>/var/adm/critical</i>, except for any kernel message.

              # Kernel messages are first, stored in the kernel
              # file, critical messages and higher ones also go
              # to another host and to the console
              #
              kern.*                       /var/adm/kernel
              kern.crit                    @finlandia
              kern.crit                    /dev/console
              kern.info;kern.!err          /var/adm/kernel-info

       The first rule direct any message that has the kernel facility to the
       file <i>/var/adm/kernel</i>.

       The second statement directs all kernel messages of the priority <b>crit</b>
       and higher to the remote host finlandia.  This is useful, because if
       the host crashes and the disks get irreparable errors you might not be
       able to read the stored messages.  If they're on a remote host, too,
       you still can try to find out the reason for the crash.

       The third rule directs these messages to the actual console, so the
       person who works on the machine will get them, too.

       The fourth line tells the syslogd to save all kernel messages that come
       with priorities from <b>info</b> up to <b>warning</b> in the file
       <i>/var/adm/kernel-info</i>.  Everything from <i>err</i> and higher is excluded.

              # The tcp wrapper loggs with mail.info, we display
              # all the connections on tty12
              #
              mail.=info                   /dev/tty12

       This directs all messages that uses <b>mail.info</b> (in source <b>LOG_MAIL</b> |
       <b>LOG_INFO</b>) to <i>/dev/tty12</i>, the 12th console.  For example the tcpwrapper
       <a href="/cgi/man.cgi?query=tcpd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>tcpd</b>(8)</a> uses this as it's default.

              # Store all mail concerning stuff in a file
              #
              mail.*;mail.!=info           /var/adm/mail

       This pattern matches all messages that come with the <b>mail</b> facility,
       except for the <b>info</b> priority.  These will be stored in the file
       <i>/var/adm/mail</i>.

              # Log all mail.info and news.info messages to info
              #
              mail,news.=info              /var/adm/info

       This will extract all messages that come either with <b>mail.info</b> or with
       <b>news.info</b> and store them in the file <i>/var/adm/info</i>.

              # Log info and notice messages to messages file
              #
              *.=info;*.=notice;\
                   mail.none  /var/log/messages

       This lets the <b>syslogd</b> log all messages that come with either the <b>info</b>
       or the <b>notice</b> facility into the file <i>/var/log/messages</i>, except for all
       messages that use the <b>mail</b> facility.

              # Log info messages to messages file
              #
              *.=info;\
                   mail,news.none       /var/log/messages

       This statement causes the <b>syslogd</b> to log all messages that come with
       the <b>info</b> priority to the file <i>/var/log/messages</i>.  But any message
       coming either with the <b>mail</b> or the <b>news</b> facility will not be stored.

              # Emergency messages will be displayed using wall
              #
              *.=emerg                     *

       This rule tells the <b>syslogd</b> to write all emergency messages to all
       currently logged in users.  This is the wall action.

              # Messages of the priority alert will be directed
              # to the operator
              #
              *.alert                      root,joey

       This rule directs all messages with a priority of <b>alert</b> or higher to
       the terminals of the operator, i.e. of the users ``root'' and ``joey''
       if they're logged in.

              *.*                          @finlandia

       This rule would redirect all messages to a remote host called
       finlandia.  This is useful especially in a cluster of machines where
       all syslog messages will be stored on only one machine.

<a name="CONFIGURATION_FILE_SYNTAX_DIFFERENCES" href="#end"><b>CONFIGURATION FILE SYNTAX DIFFERENCES</b></a>
       <b>Syslogd</b> uses a slightly different syntax for its configuration file
       than the original BSD sources.  Originally all messages of a specific
       priority and above were forwarded to the log file.  The modifiers
       ``='', ``!'' and ``-'' were added to make the <b>syslogd</b> more flexible and
       to use it in a more intuitive manner.

       The original BSD syslogd doesn't understand spaces as separators
       between the selector and the action field.

<a name="FILES" href="#end"><b>FILES</b></a>
       <i>/etc/syslog.conf</i>
              Configuration file for <b>syslogd</b>

<a name="BUGS" href="#end"><b>BUGS</b></a>
       The effects of multiple selectors are sometimes not intuitive.  For
       example ``mail.crit,*.err'' will select ``mail'' facility messages at
       the level of ``err'' or higher, not at the level of ``crit'' or higher.

<a name="SEE_ALSO" href="#end"><b>SEE ALSO</b></a>
       <a href="/cgi/man.cgi?query=sysklogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>sysklogd</b>(8)</a>, <a href="/cgi/man.cgi?query=klogd&amp;sektion=8&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>klogd</b>(8)</a>, <a href="/cgi/man.cgi?query=logger&amp;sektion=1&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>logger</b>(1)</a>, <a href="/cgi/man.cgi?query=syslog&amp;sektion=2&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslog</b>(2)</a>, <a href="/cgi/man.cgi?query=syslog&amp;sektion=3&amp;apropos=0&amp;manpath=SuSE+Linux%2fi386+10.1"><b>syslog</b>(3)</a>

<a name="AUTHORS" href="#end"><b>AUTHORS</b></a>
       The <b>syslogd</b> is taken from BSD sources, Greg Wettstein
       (greg@wind.enjellic.com) performed the port to Linux, Martin Schulze
       (joey@linux.de) made some bugfixes and added some new features.

Version 1.3                     1 January 1998                  SYSLOG.CONF(5)
</pre>
<a name="end" />
<hr />
<a href="#NAME">NAME</a> |
<a href="#DESCRIPTION">DESCRIPTION</a> |
<a href="#SELECTORS">SELECTORS</a> |
<a href="#ACTIONS">ACTIONS</a> |
<a href="#EXAMPLES">EXAMPLES</a> |
<a href="#CONFIGURATION_FILE_SYNTAX_DIFFERENCES">CONFIGURATION FILE SYNTAX DIFFERENCES</a> |
<a href="#FILES">FILES</a> |
<a href="#BUGS">BUGS</a> |
<a href="#SEE_ALSO">SEE ALSO</a> |
<a href="#AUTHORS">AUTHORS</a>
<p align="left">Want to link to this manual page? Use this URL:<br/>&lt;<a href="https://www.freebsd.org/cgi/man.cgi?query=syslog.conf&amp;sektion=5&amp;manpath=SuSE+Linux%2fi386+10.1">https://www.freebsd.org/cgi/man.cgi?query=syslog.conf&amp;sektion=5&amp;manpath=SuSE+Linux%2fi386+10.1</a>&gt;</p>
<a href="/cgi/man.cgi?manpath=">home</a> | <a href="/cgi/man.cgi/help.html">help</a> 
<hr noshade="noshade" />
	</div>
        <div id="footer">
          <a href="../copyright/">Legal Notices</a> | &copy; 1995-2016
          The FreeBSD Project. All rights reserved.<br />
	  <address><a href='../mailto.html'>Contact</a><br /></address>
        </div>
      </div>
    </div>
  </body>
</html>
