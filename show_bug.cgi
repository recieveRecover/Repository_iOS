<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
                      "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
  <head>
    <title>Bug 153856 &ndash; Scroll gesture in text field in position:fixed element sometimes scrolls &lt;body&gt; instead of scrollable ancestor on iOS</title>

      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">


<link rel="Top" href="https://bugs.webkit.org/">

  


  
    <link rel="Show" title="Dependency Tree"
          href="showdependencytree.cgi?id=153856&amp;hide_resolved=1">
      <link rel="Show" title="Dependency Graph"
            href="showdependencygraph.cgi?id=153856">

      <link rel="Show" title="Bug Activity"
            href="show_activity.cgi?id=153856">
      <link rel="Show" title="Printer-Friendly Version"
            href="show_bug.cgi?format=multiple&amp;id=153856">



    
    
    <link href="skins/standard/global.css?1413475273"
          rel="alternate stylesheet" 
          title="Classic"><link href="js/yui/assets/skins/sam/autocomplete.css?1413475262" rel="stylesheet"
        type="text/css" ><link href="js/yui/assets/skins/sam/calendar.css?1413475262" rel="stylesheet"
        type="text/css" ><link href="skins/standard/global.css?1413475273" rel="stylesheet"
        type="text/css" ><link href="skins/standard/show_bug.css?1413475273" rel="stylesheet"
        type="text/css" ><!--[if lte IE 7]>
      



  <link href="skins/standard/IE-fixes.css?1413475263" rel="stylesheet"
        type="text/css" >
<![endif]-->

    
<link href="skins/contrib/Dusk/global.css?1413475273" rel="alternate stylesheet"
        type="text/css" title="Dusk">

    

    <link href="skins/custom/global.css?1273387843" rel="stylesheet"
        type="text/css" >

    
<script type="text/javascript" src="js/yui/yahoo-dom-event/yahoo-dom-event.js?1413475262"></script><script type="text/javascript" src="js/yui/cookie/cookie-min.js?1413475262"></script><script type="text/javascript" src="js/yui/datasource/datasource-min.js?1413475262"></script><script type="text/javascript" src="js/yui/connection/connection-min.js?1413475262"></script><script type="text/javascript" src="js/yui/json/json-min.js?1413475262"></script><script type="text/javascript" src="js/yui/autocomplete/autocomplete-min.js?1413475262"></script><script type="text/javascript" src="js/yui/calendar/calendar-min.js?1413475262"></script><script type="text/javascript" src="js/global.js?1413475262"></script>

    <script type="text/javascript">
    <!--
        YAHOO.namespace('bugzilla');
        YAHOO.util.Event.addListener = function (el, sType, fn, obj, overrideContext) {
               if ( ("onpagehide" in window || YAHOO.env.ua.gecko) && sType === "unload") { sType = "pagehide"; };
               var capture = ((sType == "focusin" || sType == "focusout") && !YAHOO.env.ua.ie) ? true : false;
               return this._addListener(el, this._getType(sType), fn, obj, overrideContext, capture);
         };
        if ( "onpagehide" in window || YAHOO.env.ua.gecko) {
            YAHOO.util.Event._simpleRemove(window, "unload", 
                                           YAHOO.util.Event._unload);
        }
        
        function unhide_language_selector() { 
            YAHOO.util.Dom.removeClass(
                'lang_links_container', 'bz_default_hidden'
            ); 
        } 
        YAHOO.util.Event.onDOMReady(unhide_language_selector);

        
        var BUGZILLA = {
            param: {
                cookiepath: '\/',
                maxusermatches: 1000
            },
            constant: {
                COMMENT_COLS: 80
            },
            string: {
                

                attach_desc_required:
                    'You must enter a Description for this attachment.',
                component_required:
                    'You must select a Component for this bug.',
                description_required:
                    'You must enter a Description for this bug.',
                short_desc_required:
                    'You must enter a Summary for this bug.',
                version_required:
                    'You must select a Version for this bug.'
            }
        };

    if( !document.location.href.match(/show_bug\.cgi/) && history && history.replaceState ) {
      history.replaceState( null, 
                         "Bug 153856 – Scroll gesture in text field in position:fixed element sometimes scrolls \x3cbody\x3e instead of scrollable ancestor on iOS",  
                         "show_bug.cgi?id=153856" );
      document.title = "Bug 153856 – Scroll gesture in text field in position:fixed element sometimes scrolls \x3cbody\x3e instead of scrollable ancestor on iOS";
    }
    // -->
    </script>
<script type="text/javascript" src="js/util.js?1413475262"></script><script type="text/javascript" src="js/field.js?1413475284"></script>


    


    
    <link rel="search" type="application/opensearchdescription+xml"
                       title="Bugzilla" href="./search_plugin.cgi">
    <link rel="shortcut icon" href="images/favicon.ico" >
  </head>



  <body onload=""
        class="bugs-webkit-org bz_bug bz_status_NEW bz_product_WebKit bz_component_Forms bz_bug_153856 yui-skin-sam">




<div id="header">





<table border="0" cellspacing="0" cellpadding="0" id="titles">
<tr>
    <td id="title">

      <p>WebKit Bugzilla
      </p>

    </td>


</tr>
</table>

<table id="lang_links_container" cellpadding="0" cellspacing="0"
       class="bz_default_hidden"><tr><td>
</td></tr></table>


    <div id="bug_title">Bug&nbsp;153856: Scroll gesture in text field in position:fixed element sometimes scrolls &lt;body&gt; instead of scrollable ancestor on iOS</div>

<ul class="links">
  <li><a href="./">Home</a></li>
  <li><span class="separator">| </span><a href="enter_bug.cgi">New</a></li>
  <li><span class="separator">| </span><a href="describecomponents.cgi">Browse</a></li>
  <li><span class="separator">| </span><a href="query.cgi">Search</a></li>

  <li class="form">
    <span class="separator">| </span>
    <form action="buglist.cgi" method="get"
        onsubmit="if (this.quicksearch.value == '')
                  { alert('Please enter one or more search terms first.');
                    return false; } return true;">
    <input class="txt" type="text" id="quicksearch_top" name="quicksearch" 
           title="Quick Search" value="">
    <input class="btn" type="submit" value="Search" 
           id="find_top"></form>
  <a href="page.cgi?id=quicksearch.html" title="Quicksearch Help">[?]</a></li>

  <li><span class="separator">| </span><a href="report.cgi">Reports</a></li>

  <li>
      <span class="separator">| </span>
        <a href="request.cgi">Requests</a></li>

  <li>
        <span class="separator">| </span>
        <a href="docs/html/bug_page.html" target="_blank">Help</a>
      </li>
    
      <li id="new_account_container_top">
        <span class="separator">| </span>
        <a href="createaccount.cgi">New&nbsp;Account</a>
      </li>

    <li id="mini_login_container_top">
  <span class="separator">| </span>
  <a id="login_link_top" href="https://bugs.webkit.org/show_bug.cgi?id=153856&amp;GoAheadAndLogIn=1"
     onclick="return show_mini_login_form('_top')">Log In</a>

  
  <form action="https://bugs.webkit.org/show_bug.cgi?id=153856" method="POST" 
        class="mini_login bz_default_hidden"
        id="mini_login_top"
        onsubmit="return check_mini_login_fields( '_top' );"
  >
    <input id="Bugzilla_login_top" 
           class="bz_login"
           name="Bugzilla_login"
           title="Login"
           onfocus="mini_login_on_focus('_top')"
    >
    <input class="bz_password" 
           id="Bugzilla_password_top" 
           name="Bugzilla_password"
           type="password"
           title="Password"
    >
    <input class="bz_password bz_default_hidden bz_mini_login_help" type="text" 
           id="Bugzilla_password_dummy_top" value="password"
           title="Password"
           onfocus="mini_login_on_focus('_top')"
    >
    <input type="submit" name="GoAheadAndLogIn" value="Log in" 
            id="log_in_top">
    <script type="text/javascript">
      mini_login_constants = {
          "login" : "login",
          "warning" : "You must set the login and password before logging in."
      };
      
      if (YAHOO.env.ua.gecko || YAHOO.env.ua.ie || YAHOO.env.ua.opera) {
          YAHOO.util.Event.onDOMReady(function() {
              init_mini_login_form('_top');
          });
      }
      else {
          YAHOO.util.Event.on(window, 'load', function () {
              window.setTimeout(function() {
                  init_mini_login_form('_top');
              }, 200);
          });
    }
    </script>
    <a href="#" onclick="return hide_mini_login_form('_top')">[x]</a>
  </form>
</li>
<li id="forgot_container_top">
  <span class="separator">| </span>
  <a id="forgot_link_top" href="https://bugs.webkit.org/show_bug.cgi?id=153856&amp;GoAheadAndLogIn=1#forgot"
     onclick="return show_forgot_form('_top')">Forgot Password</a>
  <form action="token.cgi" method="post" id="forgot_form_top"
        class="mini_forgot bz_default_hidden">
    <label for="login_top">Login:</label>
    <input type="text" name="loginname" size="20" id="login_top">
    <input id="forgot_button_top" value="Reset Password" 
           type="submit">
    <input type="hidden" name="a" value="reqpw">
    <input type="hidden" id="token_top" name="token" value="1479256309-3a890403d3f479dca75260e619e32be9">
    <a href="#" onclick="return hide_forgot_form('_top')">[x]</a>
  </form>
</li>
</ul>
</div> 


<div id="bugzilla-body">

<div class="navigation">
  

  <i><font color="#777777">|&laquo;&nbsp;First</font></i>
  <i><font color="#777777">Last&nbsp;&raquo;|</font></i>
  <i><font color="#777777">&laquo;&nbsp;Prev</font></i>
  <i><font color="#777777">Next&nbsp;&raquo;</font></i>

  &nbsp;&nbsp;
  <i><font color="#777777">This bug is not in your last
    search results.</font></i>
</div>
<script type="text/javascript">
  <!--
  
  /* Outputs a link to call replyToComment(); used to reduce HTML output */
  function addReplyLink(id, real_id) {
      /* XXX this should really be updated to use the DOM Core's
       * createElement, but finding a container isn't trivial.
       */
        document.write('[<a href="#add_comment" onclick="replyToComment(' + 
                       id + ',' + real_id + '); return false;">reply<' + '/a>]');
  }

  /* Adds the reply text to the `comment' textarea */
  function replyToComment(id, real_id) {
      var prefix = "(In reply to comment #" + id + ")\n";
      var replytext = "";
        /* pre id="comment_name_N" */
        var text_elem = document.getElementById('comment_text_'+id);
        var text = getText(text_elem);
        replytext = prefix + wrapReplyText(text);


      /* <textarea id="comment"> */
      var textarea = document.getElementById('comment');
      textarea.value += replytext;

      textarea.focus();
  }

  if (typeof Node == 'undefined') {
      /* MSIE doesn't define Node, so provide a compatibility object */
      window.Node = {
          TEXT_NODE: 3,
          ENTITY_REFERENCE_NODE: 5
      };
  }

  /* Concatenates all text from element's childNodes. This is used
   * instead of innerHTML because we want the actual text (and
   * innerText is non-standard).
   */
  function getText(element) {
      var child, text = "";
      for (var i=0; i < element.childNodes.length; i++) {
          child = element.childNodes[i];
          var type = child.nodeType;
          if (type == Node.TEXT_NODE || type == Node.ENTITY_REFERENCE_NODE) {
              text += child.nodeValue;
          } else {
              /* recurse into nodes of other types */
              text += getText(child);
          }
      }
      return text;
  }


  /* Index all classifications so we can keep track of the classification
   * for the selected product, which could control field visibility.
   */
  var all_classifications = new Array(2);
      all_classifications['Security'] = 'Unclassified';
      all_classifications['WebKit'] = 'Unclassified';

  //-->
  </script>

<form name="changeform" id="changeform" method="post" action="process_bug.cgi">

  <input type="hidden" name="delta_ts" value="2016-09-18 17:45:01">
  <input type="hidden" name="longdesclength" value="3">
  <input type="hidden" name="id" value="153856">
  <input type="hidden" name="token" value="1479256309-598de11b6dc8459ef7c22ac0b29c1b52">
<div class="bz_alias_short_desc_container edit_form">
     <a href="show_bug.cgi?id=153856"><b>Bug&nbsp;153856</b></a> -<span id="summary_alias_container" class="bz_default_hidden"> 
      <span id="short_desc_nonedit_display">Scroll gesture in text field in position:fixed element sometimes scrolls &lt;body&gt; instead of scrollable ancestor on iOS</span>
     </span>
  
       
    <div id="summary_alias_input">
      <table id="summary"> 
          <tr>
            <td colspan="2">
          </td>
        </tr> 
        
        <tr>
          <td>
            <label accesskey="s" for="short_desc"><u>S</u>ummary</label>:
          </td>
          <td><span title="Scroll gesture in text field in position:fixed element sometimes scrolls &lt;body&gt; instead of scrollable ancestor on iOS">Scroll gesture in text field in position:fixed element sometimes scrolls &lt;bod...
        </span>
          </td>
        </tr>
      </table>
    </div>
  </div>
  <script type="text/javascript">
    hideAliasAndSummary('Scroll gesture in text field in position:fixed element sometimes scrolls \x3cbody\x3e instead of scrollable ancestor on iOS', '');
  </script>

  <table id="bug_details" class="edit_form">

    <tr>
      
      <td id="bz_show_bug_column_1" class="bz_show_bug_column">     
        <table>
          <tr>
    <td class="field_label">
      <b><a href="page.cgi?id=fields.html#status">Status</a></b>:
    </td>
    <td id="bz_field_status">
      <span id="static_bug_status">NEW
      </span>
    </td>
  </tr>
          <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
          <tr><th class="field_label "
    id="field_label_product">


  <a 
      title="Bugs are categorised into Products and Components."
      class="field_help_link"
      href="describecomponents.cgi"
  >Product:</a>

</th>
  <td class="field_value "
      id="field_container_product" >WebKit</td>
    </tr>

    
    <tr class="bz_default_hidden"><th class="field_label "
    id="field_label_classification">


  <a 
      title="Bugs are categorised into Classifications, Products and Components. classifications is the top-level categorisation."
      class="field_help_link"
      href="page.cgi?id=fields.html#classification"
  >Classification:</a>

</th>
  <td class="field_value "
      id="field_container_classification" >Unclassified</td>
    </tr>
        
    
    
    <tr><th class="field_label "
    id="field_label_component">


  <a 
      title="Components are second-level categories; each belongs to a particular Product. Select a Product to narrow down this list."
      class="field_help_link"
      href="describecomponents.cgi?product=WebKit"
  >Component:</a>

</th>
  <td class="field_value "
      id="field_container_component" >Forms</td>
    </tr>
    <tr>
      <td class="field_label">

        <label for="version"><b><u>V</u>ersion</b></label>:

      </td>

<td>WebKit Nightly Build
  </td>

    </tr>
        
    
        
    <tr>
      <td class="field_label">
        <label for="rep_platform" accesskey="h"><b>Platform</b></label>:
      </td>
      <td class="field_value">iPhone / iPad
       iOS 10
       <script type="text/javascript">

         assignToDefaultOnChange(['product']);

       </script>
      </td>
    </tr>
          <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
          
          <tr>
      <td class="field_label">
        <label for="priority" accesskey="i">

          <b><a href="page.cgi?id=fields.html#importance"><u>I</u>mportanc<u>e</u></a></b></label>:

      </td>
      <td>P2

       Normal

      </td>
    </tr>            
          
          <tr>
      <td class="field_label">
        <b><a href="page.cgi?id=fields.html#assigned_to">Assigned To</a></b>:
      </td>
      <td><span class="vcard"><span class="fn">Nobody</span>
</span>
      </td>
    </tr>
          <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
          <tr><th class="field_label "
    id="field_label_bug_file_loc">

    <label for="bug_file_loc" accesskey="u">

  <a 
      title="Bugs can have a URL associated with them - for example, a pointer to a web site where the problem is seen."
      class="field_help_link"
      href="page.cgi?id=fields.html#bug_file_loc"
  >URL:</a>
</label>
</th>
    <td>
      <span id="bz_url_input_area">
      </span>
    </td>
  </tr>
  
  
    <tr>
      <td class="field_label">
        <label for="keywords" accesskey="k">
          <b><a href="describekeywords.cgi"><u>K</u>eywords</a></b></label>:
      </td>
      <td class="field_value" colspan="2">HasReduction, InRadar
      </td>
    </tr>
          <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
          
          <tr><th class="field_label "
    id="field_label_dependson">


  <a 
      title="The bugs listed here must be resolved before this bug can be resolved."
      class="field_help_link"
      href="page.cgi?id=fields.html#dependson"
  >Depends on:</a>

</th>

  <td>
    <span id="dependson_input_area">
    </span>
    
  </td>
  </tr>
  
  <tr><th class="field_label "
    id="field_label_blocked">


  <a 
      title="This bug must be resolved before the bugs listed in this field can be resolved."
      class="field_help_link"
      href="page.cgi?id=fields.html#blocked"
  >Blocks:</a>

</th>

  <td>
    <span id="blocked_input_area">
    </span>
    <a class="bz_bug_link 
          bz_status_NEW "
   title="NEW - [meta] Issues affecting Bootstrap"
   href="show_bug.cgi?id=159753">159753</a> 
  </td>
  
  <tr>
    <th>&nbsp;</th>
  
    <td colspan="2" align="left" id="show_dependency_tree_or_graph">
      Show dependency <a href="showdependencytree.cgi?id=153856&amp;hide_resolved=1">tree</a>
  
        /&nbsp;<a href="showdependencygraph.cgi?id=153856">graph</a>
    </td>
  </tr>
          
        </table>
      </td>
      <td>
        <div class="bz_column_spacer">&nbsp;</div>
      </td>
      
      <td id="bz_show_bug_column_2" class="bz_show_bug_column">
        <table cellpadding="3" cellspacing="1">
        <tr>
    <td class="field_label">
      <b>Reported</b>:
    </td>
    <td>2016-02-04 01:22 PST by <span class="vcard"><span class="fn">Chris Rebert</span>
</span>
    </td>
  </tr>
  
  <tr>
    <td class="field_label">
      <b> Modified</b>:
    </td>
    <td>2016-09-18 17:45 PDT 
      (<a href="show_activity.cgi?id=153856">History</a>)
    </td>
  
  </tr>
         <tr>
      <td class="field_label">
        <label for="newcc" accesskey="a"><b>CC List</b>:</label>
      </td>
      <td>5 
          users
          <span id="cc_edit_area_showhide_container" class="bz_default_hidden">
            (<a href="#" id="cc_edit_area_showhide">show</a>)
          </span>
        <div id="cc_edit_area">
          <br>
            <select id="cc" multiple="multiple" size="5">
                <option value="dbates">dbates</option>
                <option value="samtsai">samtsai</option>
                <option value="simon.fraser">simon.fraser</option>
                <option value="webkit-bug-importer">webkit-bug-importer</option>
                <option value="wenson_hsieh">wenson_hsieh</option>
            </select>
        </div>
          <script type="text/javascript">
            hideEditableField( 'cc_edit_area_showhide_container', 
                               'cc_edit_area', 
                               'cc_edit_area_showhide', 
                               '', 
                               '');  
          </script>
      </td>
    </tr>
         <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
<tr><th class="field_label "
    id="field_label_see_also">


  <a 
      title="This allows you to refer to bugs in other installations. You can enter a URL to a bug in the 'Add Bug URLs' field to note that that bug is related to this one. You can enter multiple URLs at once by separating them with a comma. You should normally use this field to refer to bugs in other installations. For bugs in this installation, it is better to use the Depends on and Blocks fields."
      class="field_help_link"
      href="page.cgi?id=fields.html#see_also"
  >See Also:</a>

</th>
  <td class="field_value "
      id="field_container_see_also" ></td>
    </tr> 
         
         <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
         
                

        </table>
      </td>
    </tr>
    <tr>
      <td colspan="3">
          <hr id="bz_top_half_spacer">
      </td>
    </tr>
  </table>

  <table id="bz_big_form_parts" cellspacing="0" cellpadding="0"><tr>
  <td>

    
<script type="text/javascript">
<!--
function toggle_display(link) {
    var table = document.getElementById("attachment_table");
    var view_all = document.getElementById("view_all");
    var hide_obsolete_url_parameter = "&hide_obsolete=1";
    // Store current height for scrolling later
    var originalHeight = table.offsetHeight;
    var rows = YAHOO.util.Dom.getElementsByClassName(
        'bz_tr_obsolete', 'tr', table);

    for (var i = 0; i < rows.length; i++) {
        bz_toggleClass(rows[i], 'bz_default_hidden');
    }

    if (YAHOO.util.Dom.hasClass(rows[0], 'bz_default_hidden')) {
        link.innerHTML = "Show Obsolete";
        view_all.href = view_all.href + hide_obsolete_url_parameter 
    }
    else {
        link.innerHTML = "Hide Obsolete";
        view_all.href = view_all.href.replace(hide_obsolete_url_parameter,"");
    }

    var newHeight = table.offsetHeight;
    // This scrolling makes the window appear to not move at all.
    window.scrollBy(0, newHeight - originalHeight);

    return false;
}
//-->
</script>

<br>
<table id="attachment_table" cellspacing="0" cellpadding="4">
  <tr id="a0">
    <th colspan="3" align="left">
      Attachments
    </th>
  </tr>


      <tr id="a1" class="bz_contenttype_text_html"


      >
        <td valign="top">
            <a href="attachment.cgi?id=270642"
               title="View the content of the attachment">
          <b>Testcase demonstrating the problem</b></a>

          <span class="bz_attach_extra_info">
              (8.86 KB,
                text/html)

            <br>
            <a href="#attach_270642"
               title="Go to the comment associated with the attachment">2016-02-04 01:22 PST</a>,
<span class="vcard"><span class="fn">Chris Rebert</span>
</span>
          </span>
        </td>

          <td class="bz_attach_flags" valign="top">
              <i>no flags</i>
          </td>

        <td valign="top">


          <a href="attachment.cgi?id=270642&amp;action=edit">Details</a>




        </td>
      </tr>
      <tr id="a2" class="bz_contenttype_image_gif"


      >
        <td valign="top">
            <a href="attachment.cgi?id=270643"
               title="View the content of the attachment">
          <b>GIF video demonstrating the bug</b></a>

          <span class="bz_attach_extra_info">
              (1.81 MB,
                image/gif)

            <br>
            <a href="#attach_270643"
               title="Go to the comment associated with the attachment">2016-02-04 01:23 PST</a>,
<span class="vcard"><span class="fn">Chris Rebert</span>
</span>
          </span>
        </td>

          <td class="bz_attach_flags" valign="top">
              <i>no flags</i>
          </td>

        <td valign="top">


          <a href="attachment.cgi?id=270643&amp;action=edit">Details</a>




        </td>
      </tr>

  <tr class="bz_attach_footer">
    <td colspan="3">
        <span class="bz_attach_view_hide">
            <a id="view_all" href="attachment.cgi?bugid=153856&amp;action=viewall">View All</a>
        </span>
        <a href="attachment.cgi?bugid=153856&amp;action=enter">Add an attachment</a>
        (proposed patch, testcase, etc.)
    </td>
  </tr>
</table>
<br>
<div id="add_comment" class="bz_section_additional_comments">
      <table>
        <tr>
          <td>
            <fieldset>
              <legend>Note</legend>
              You need to
              <a href="show_bug.cgi?id=153856&amp;GoAheadAndLogIn=1">log in</a>
              before you can comment on or make changes to this bug.
            </fieldset>
          </td>
        </tr> 
      </table>
  </div>
  </td>
  <td>
  </td>
  </tr></table>

  
  <div id="comments"><script src="js/comments.js?1413475262" type="text/javascript">
</script>




<!-- This auto-sizes the comments and positions the collapse/expand links 
     to the right. -->
<table class="bz_comment_table" cellpadding="0" cellspacing="0"><tr>
<td>
<div id="c0" class="bz_comment bz_first_comment">

      <div class="bz_first_comment_head">



        <span class="bz_comment_number">
          <a 
             href="show_bug.cgi?id=153856#c0">Description</a>
        </span>

        <span class="bz_comment_user"><span class="vcard"><span class="fn">Chris Rebert</span>
</span>
        </span>

        <span class="bz_comment_user_images">
        </span>

        <span class="bz_comment_time">
          2016-02-04 01:22:53 PST
        </span>
      </div>



<pre class="bz_comment_text" >Created <span class=""><a href="attachment.cgi?id=270642" name="attach_270642" title="Testcase demonstrating the problem">attachment 270642</a> <a href="attachment.cgi?id=270642&amp;action=edit" title="Testcase demonstrating the problem">[details]</a></span>
Testcase demonstrating the problem

Steps to reproduce:
1. Open the attached testcase in iOS Safari.
2. Tap the &quot;Launch demo modal&quot; button.
3. Tap into the 2nd text field.
4. Type some text.
5. Tap the Done button.
6. Perform a scroll-down gesture (i.e. flick your finger upward), but start the scroll gesture within the bounds of the 2nd text field.

Actual result:
The &lt;body&gt; scrolls downward.

Expected result:
The yellow &lt;div&gt; (which is a descendant of a position:fixed &lt;div&gt;) should scroll downward.
The &lt;body&gt; shouldn't scroll at all, because it's styled as overflow:hidden.

Original Bootstrap bug: <a href="https://github.com/twbs/bootstrap/issues/14839#issuecomment-60940738">https://github.com/twbs/bootstrap/issues/14839#issuecomment-60940738</a>

This is similar to <a class="bz_bug_link 
          bz_status_NEW "
   title="NEW - &lt;body&gt; with overflow:hidden CSS is scrollable on iOS"
   href="show_bug.cgi?id=153852">bug 153852</a>, but that bug usually occurs only when the position:fixed element has already been scrolled to its top or bottom,
whereas this bug doesn't have that requirement and seems to be related to text fields specifically.</pre>
    </div><div id="c1" class="bz_comment">

      <div class="bz_comment_head">



        <span class="bz_comment_number">
          <a 
             href="show_bug.cgi?id=153856#c1">Comment 1</a>
        </span>

        <span class="bz_comment_user"><span class="vcard"><span class="fn">Chris Rebert</span>
</span>
        </span>

        <span class="bz_comment_user_images">
        </span>

        <span class="bz_comment_time">
          2016-02-04 01:23:46 PST
        </span>
      </div>



<pre class="bz_comment_text" >Created <span class=""><a href="attachment.cgi?id=270643" name="attach_270643" title="GIF video demonstrating the bug">attachment 270643</a> <a href="attachment.cgi?id=270643&amp;action=edit" title="GIF video demonstrating the bug">[details]</a></span>
GIF video demonstrating the bug</pre>
    </div><div id="c2" class="bz_comment">

      <div class="bz_comment_head">



        <span class="bz_comment_number">
          <a 
             href="show_bug.cgi?id=153856#c2">Comment 2</a>
        </span>

        <span class="bz_comment_user"><span class="vcard"><span class="fn">Radar WebKit Bug Importer</span>
</span>
        </span>

        <span class="bz_comment_user_images">
        </span>

        <span class="bz_comment_time">
          2016-02-05 02:23:52 PST
        </span>
      </div>



<pre class="bz_comment_text" >&lt;rdar://problem/24522873&gt;</pre>
    </div>


  

</td>
<td>
</td>
</tr></table>
  </div>
        

</form>

<hr>
<ul class="related_actions">
    <li><a href="show_bug.cgi?format=multiple&amp;id=153856">Format For Printing</a></li>
    <li>&nbsp;-&nbsp;<a href="show_bug.cgi?ctype=xml&amp;id=153856">XML</a></li>
    <li>&nbsp;-&nbsp;<a href="enter_bug.cgi?cloned_bug_id=153856">Clone This Bug</a></li>
    
    <li>&nbsp;-&nbsp;<a href="#">Top of page </a></li>
    </ul>        


<div class="navigation">
  

  <i><font color="#777777">|&laquo;&nbsp;First</font></i>
  <i><font color="#777777">Last&nbsp;&raquo;|</font></i>
  <i><font color="#777777">&laquo;&nbsp;Prev</font></i>
  <i><font color="#777777">Next&nbsp;&raquo;</font></i>

  &nbsp;&nbsp;
  <i><font color="#777777">This bug is not in your last
    search results.</font></i>
</div>

<br>
</div>



<div id="footer">
  <div class="intro"></div>




<ul id="useful-links">
  <li id="links-actions"><ul class="links">
  <li><a href="./">Home</a></li>
  <li><span class="separator">| </span><a href="enter_bug.cgi">New</a></li>
  <li><span class="separator">| </span><a href="describecomponents.cgi">Browse</a></li>
  <li><span class="separator">| </span><a href="query.cgi">Search</a></li>

  <li class="form">
    <span class="separator">| </span>
    <form action="buglist.cgi" method="get"
        onsubmit="if (this.quicksearch.value == '')
                  { alert('Please enter one or more search terms first.');
                    return false; } return true;">
    <input class="txt" type="text" id="quicksearch_bottom" name="quicksearch" 
           title="Quick Search" value="">
    <input class="btn" type="submit" value="Search" 
           id="find_bottom"></form>
  <a href="page.cgi?id=quicksearch.html" title="Quicksearch Help">[?]</a></li>

  <li><span class="separator">| </span><a href="report.cgi">Reports</a></li>

  <li>
      <span class="separator">| </span>
        <a href="request.cgi">Requests</a></li>

  <li>
        <span class="separator">| </span>
        <a href="docs/html/bug_page.html" target="_blank">Help</a>
      </li>
    
      <li id="new_account_container_bottom">
        <span class="separator">| </span>
        <a href="createaccount.cgi">New&nbsp;Account</a>
      </li>

    <li id="mini_login_container_bottom">
  <span class="separator">| </span>
  <a id="login_link_bottom" href="https://bugs.webkit.org/show_bug.cgi?id=153856&amp;GoAheadAndLogIn=1"
     onclick="return show_mini_login_form('_bottom')">Log In</a>

  
  <form action="https://bugs.webkit.org/show_bug.cgi?id=153856" method="POST" 
        class="mini_login bz_default_hidden"
        id="mini_login_bottom"
        onsubmit="return check_mini_login_fields( '_bottom' );"
  >
    <input id="Bugzilla_login_bottom" 
           class="bz_login"
           name="Bugzilla_login"
           title="Login"
           onfocus="mini_login_on_focus('_bottom')"
    >
    <input class="bz_password" 
           id="Bugzilla_password_bottom" 
           name="Bugzilla_password"
           type="password"
           title="Password"
    >
    <input class="bz_password bz_default_hidden bz_mini_login_help" type="text" 
           id="Bugzilla_password_dummy_bottom" value="password"
           title="Password"
           onfocus="mini_login_on_focus('_bottom')"
    >
    <input type="submit" name="GoAheadAndLogIn" value="Log in" 
            id="log_in_bottom">
    <script type="text/javascript">
      mini_login_constants = {
          "login" : "login",
          "warning" : "You must set the login and password before logging in."
      };
      
      if (YAHOO.env.ua.gecko || YAHOO.env.ua.ie || YAHOO.env.ua.opera) {
          YAHOO.util.Event.onDOMReady(function() {
              init_mini_login_form('_bottom');
          });
      }
      else {
          YAHOO.util.Event.on(window, 'load', function () {
              window.setTimeout(function() {
                  init_mini_login_form('_bottom');
              }, 200);
          });
    }
    </script>
    <a href="#" onclick="return hide_mini_login_form('_bottom')">[x]</a>
  </form>
</li>
<li id="forgot_container_bottom">
  <span class="separator">| </span>
  <a id="forgot_link_bottom" href="https://bugs.webkit.org/show_bug.cgi?id=153856&amp;GoAheadAndLogIn=1#forgot"
     onclick="return show_forgot_form('_bottom')">Forgot Password</a>
  <form action="token.cgi" method="post" id="forgot_form_bottom"
        class="mini_forgot bz_default_hidden">
    <label for="login_bottom">Login:</label>
    <input type="text" name="loginname" size="20" id="login_bottom">
    <input id="forgot_button_bottom" value="Reset Password" 
           type="submit">
    <input type="hidden" name="a" value="reqpw">
    <input type="hidden" id="token_bottom" name="token" value="1479256309-3a890403d3f479dca75260e619e32be9">
    <a href="#" onclick="return hide_forgot_form('_bottom')">[x]</a>
  </form>
</li>
</ul>
  </li>

  
    

  


  
</ul>

  <div class="outro"></div>
</div>


<!-- WEBKIT_CHANGES -->
<script defer src="/committers-autocomplete.js"></script>
</body>
</html>