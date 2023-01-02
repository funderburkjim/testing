// scans/STCSCAN/web/main.js  Nov 24, 2008
var requestActive=false;
function loadFcn() {
 document.getElementById("rightpane").innerHTML = "";
 var word = document.getElementById("key").value;
  if (word) {
    getWord();
  }
}
function getWord() {
  var word = "";
  if (document.getElementById("key").value) {
    word = document.getElementById("key").value;
    word = word.trim();
  }
  if ((word.length < 1)) {
   alert('Please specify a citation.');
   return;
  }
 var filterdir = document.getElementById("filterdir").value;
 var transLit = document.getElementById("transLit").value;
 var filter = document.getElementById("filter").value;
  var url =  "/cgi-bin/work/stcscan/getWord.pl" +
   "?key=" +escape(word) +
   "&filterdir=" + escape(filterdir) +
   "&filter=" + escape(filter) +
   "&transLit=" + escape(transLit);
  request.open("GET", url, true);
  request.onreadystatechange = updatePage;
  request.send(null);
  requestActive=true;
}

function updatePage() {
  if (request.readyState == 4) {
   requestActive=false;
   if (request.status == 200) {
    var response = request.responseText;
    var ans1,ans2;
    var i,x,n;
    var arr;
    arr =eval( "(" + response + ")");
    n=arr.length;
    if (!(n)) {updatePageProb();return;}
    if ((n == 2) && (arr[0] == "ERR")) {updatePageERR(arr);return;}
    var ansEl = document.getElementById("botleftdiv");
    ansEl.innerHTML = "";
    updatePageSingle(response,arr);
    updateWordList(arr);
    return;
  } else {
    alert("Error! Request status is " + request.status);
  }
 }
}
function updatePageProb() {
    var ansEl = document.getElementById("botleftdiv");
    ansEl.innerHTML = "<p>Problem. Bad data returned.</p>";
    ansEl =  document.getElementById("rightpane");
    ansEl.style.zIndex="1";
}
function updatePageERR(arr) {
    var ansEl = document.getElementById("botleftdiv");
    ansEl.innerHTML = "<p>No data found for " + arr[1] + "</p>";
    ansEl =  document.getElementById("rightpane");
    ansEl.style.zIndex="1";
}
function updatePageSingle(response,arr) {
 obj = arr[0];
 updatePageImgPrep(obj);
}
function updatePageImgPrep (obj) {
// for stchoupak, the object names are:
// key, id, iddisp, 
// page, col, par, 
// nh, j1, i1, j2, i2,
//  left , top, bot
//  filename, fileprev, filenext
 var divid = "rightpane";
 var ansEl = document.getElementById(divid);
 ansEl.style.zIndex="-1"; //put temporarily below an empty area.
 var filename = obj.filename;
 var body;
 var imgurl = "/scans/STCScan/STCScanjpg/" + filename + ".jpg";
 var scroll_parms = construct_scroll_parms(obj);
// generate the image via serveimg.pl
  var onload = 'onload="scroll_div(' + "'" + divid + "'" + scroll_parms +
              ');"';
  var imgelt = '<img src="' + imgurl + '" '+ onload +' / >';
  body = imgelt;
  body = body + "<div id='hilitediv'></div>\n";
  var pagenav = compute_pagenav(obj);
  body = body + "<div id='pagenav'>\n" + pagenav + "</div>\n";
  ansEl.innerHTML = body;

}
//alert('updatePageImgPrep');
function updatePageImg (){
  if (request.readyState == 4) {
   requestActive=false;
   if (request.status == 200) {
    var response = request.responseText;
    if (!(response)) {updatePageImgProb();return;}
//     alert('response=' + response);
     var ansEl;
     ansEl = document.getElementById("rightpane");
     ansEl.style.zIndex="1";
     ansEl.innerHTML = response;
     ansEl = document.getElementById("pagenav");
     ansEl.style.zIndex="1";
    return;
  } else {
    alert("Error! Request status is " + request.status);
  }
 }
}
function updatePageImgProb() {
    var ansEl = document.getElementById("botleftdiv");
    ansEl.innerHTML = "<p>Problem with image.</p>";
    ansEl =  document.getElementById("rightpane");
    ansEl.style.zIndex="1";
}
function construct_scroll_parms(obj) {
// jpg image size: 750px × 1054px (width by height)
// for stchoupak, the object names are:
// key, id, iddisp, 
// page, col, par, 
// nh, j1, i1, j2, i2,
//  left , top, bot
//  filename, fileprev, filenext
// azva: {"key":"azva","id":"azva","iddisp":"aSva","page":"098",
// "par":"11","nh":"0","j1":"4","i1":"5","j2":"27","i2":"13",
// "filename":"stchou-098-azaucin","fileprev":"stchou-097-azarIrin","filenext":"stchou-099-azvattha",
// "left":"119","top":"95","bot":"816"}
 var imgw = 750;
 var imgh = 1054;
 var page = parseInt(obj.page,10);
 var imgc1_left = parseInt(obj.left,10);
 var imgtop = parseInt(obj.top,10);
// if ((page % 2) == 0) {
//  imgtop = imgtop + 35;
// }
 var imgbot = parseInt(obj.bot,10);
 var imgc1_right = imgc1_left + 275;
 var intercolspc = 18; // formerly 20
 var imgc2_left =  imgc1_right + intercolspc;
 var imgc2_right = imgc2_left + 275;
 var imgheight ;
 imgheight = imgbot - imgtop;
 var ans;
 if (! (obj.col)) {
  ans = ',' + 0 + ',' + 0 +
              ',' + 0 + ',' + 0 + ',' + 0 + ',' + 0;
 return ans;
 }
 var col = parseInt(obj.col,10); // column (1 or 2)

// l2 = last line of this text
// l1 = first line of this text
 var nl,l2,l1,lt;
 var np = parseInt(obj.par,10); //  paragraph number
 var nh = parseInt(obj.nh,10); // # of <H> lines.
 var j1 = parseInt(obj.j1,10); // 
 var i1 = parseInt(obj.i1,10);  // 
 var j2 = parseInt(obj.j2,10); // 
 var i2 = parseInt(obj.i2,10);  // 
 var textt,texth,textl,textw,texth;
 // vertical positions don't depend on col
 if (page == 1) {nh = 0;}
 else if (page == 273) {nh = 0;}
 else if (page == 581) {nh = 0;}
 var parpx = 18;
 if ((page == 1) && (col == 1)) {parpx=20;}
 var hpx = 55;
 if (page == 239){hpx =  95;}
 else if ((page == 107) && (col == 1)){hpx = 110;}
 else if (page == 133){hpx = 105;}
 else if (page == 134){hpx = 105;}
 else if (page == 162){hpx = 100;}
 else if (page == 163){hpx =  40;}
 else if (page == 164){hpx =  80;}
 else if (page == 168){hpx =  80;}
 else if (page == 169){hpx = 110;}
 else if (page == 170){hpx = 110;}
 else if (page == 241){hpx = 105;}
 else if (page == 254){hpx = 100;}
 else if ((page == 268) && (col == 1)){hpx = 100;}
 else if ((page == 268) && (col == 2)){hpx = 115;}
 else if (page == 269){hpx = 115;}
 else if (page == 335){hpx =  90;}
 else if (page == 347){hpx =  80;}
 else if (page == 395){hpx =  50;}
 else if (page == 502){hpx = 110;}
 else if (page == 504){hpx = 120;}
 else if (page == 542){hpx = 115;}
 else if (page == 595){hpx = 120;}
 else if (page == 610){hpx =  95;}
 else if (page == 620){hpx = 100;}
 else if (page == 748){hpx = 106;}
 else if (page == 749){hpx =  95;}
 else if (page == 882){hpx = 110;}
//textt = imgtop + (nh * 55 ) + ((np - 1)*parpx) + (j1*13) + (i1*14);
//textb = imgtop + (nh * 55 ) + ((np - 1)*parpx) + parpx + (j2*13) + (i2*14);
  textt = imgtop + (nh * hpx) + ((np - 1)*parpx) + (j1*14.0) + (i1*14.0);
  textb = imgtop + (nh * hpx) + ((np - 1)*parpx) + parpx + (j2*14.0) + (i2*14.0);
  texth = textb - textt;

 if (col == 1) {
  // text starts in column 1
  textl = imgc1_left;
  textw = imgc1_right - imgc1_left;
 }else {
  // text starts in column 2
  textl = imgc2_left;
  textw = imgc2_right - imgc2_left;
 }
 var scrollx = textl - 40;
 var scrolly = textt - 40;
 var divid = "rightpane";
 ans = ',' + scrollx + ',' + scrolly +
              ',' + textl + ',' + textt + ',' + textw + ',' + texth;
 return ans;
}
function scroll_div(divid,x,y,textl,textt,textw,texth) {
 var div = document.getElementById(divid);
 if (div) {
  var div1 = document.getElementById("autoscroll");
  if (0 == 1) { //temporarily remove window scrolling
  div.scrollTop = y;
  div.scrollLeft = x;
  }
  if (div1.value == "scroll") {
   // change scroll only if needed to make visible.
    div.scrollTop = y;
    div.scrollLeft = x;
  }
  var tempobj = document.getElementById("hilitediv");
  if (tempobj) {
   tempobj.style.position = "absolute";
   tempobj.style.left = textl + "px";
   tempobj.style.top =  textt + "px";
   tempobj.style.width = textw + "px";
   tempobj.style.height = texth + "px";
  }
  div.style.zIndex="1";
 } else {
  alert('problem in scroll_div ' + divid);
 }
}
function compute_pagenav(obj) {
 var fileprev = obj.fileprev;
 var filenext = obj.filenext;
 var ans1 = compute_pagenav_helper("&lt;",fileprev);
 var ans2 = compute_pagenav_helper("&gt;",filenext);
 return (ans1 + ans2);
}
function compute_pagenav_helper(text,filein) {
 var a;
 if (!(filein)) {
  a="<!-- " + text + "  file unavailable -->\n";
  return (a);
 }
 // filein is like stchou-284-gargIya. Use regexp to extract 'gargIya'
// var patt = new RegExp("[a-zA-Z]+$"); // $ is end of string
 var patt = new RegExp("[0-9]+")
 var word = patt.exec(filein);
 a = "<a onclick=\"getWord1('" + word + "');\"" +
     " class='nppage'><span class='nppage1'>" + text + "</span>&nbsp;</a>";
 return (a);
}
function getWord1(wordin) {
 if (wordin) {
  document.getElementById("key").value = wordin;
  getWord();
 }
}
function queryInputChar(e){
var keynum;
var keychar;
var numcheck;

if(window.event) // IE
{
keynum = e.keyCode;
}
else if(e.which) // Netscape/Firefox/Opera
{
keynum = e.which;
}
keychar = String.fromCharCode(keynum);
if ((keynum == 10) || (keynum == 13)) { // newline or return
 getWord();
 return (1 == 1);
}
return keychar;
}
function updateWordList(arr) {
 var obj = arr[0];
 var key = obj.key;
 var id = obj.id;
 var ansEl = document.getElementById("botleftdiv");
 var html="";
 var ans1;
 if (key != id) {
//  var iddisp = obj.iddisp;
//  ans1 = "<span class='iddisp'>" + iddisp + " </span> <br/>\n";
  ans1 = iddisp_format1(obj);
  html  = html + ans1;
 }
 var n;
 var m=arr.length;
 var n1,n2,l1,l2,ltot,ltot2;
 // find n2 as the first subscript with col = 2
 obj = arr[0]
 n = 1;
 n2 = 1; // in case something goes wrong
 while (n < m) {
  obj = arr[n];
  l1 = parseInt(obj.col,10);
  if (l1 == 2) {
   n2 = n;
   n = m; //to exit loop
  }
  n++;
 }
// alert('ltot = ' + ltot + ', ltot2 = ' + ltot2 + ', n2 = ' + n2);
 ans1 = "<span class='wordlist'>\n";
 html = html + ans1;
 html = html + "<table>\n";
 n = 1;
 n1 = n2;
 while (n < n2) {
  obj = arr[n];
  id = iddisp_format1(obj);
  ans1 =  n + ". " + id;
  ans1 = "<tr><td>" + ans1 + "</td>\n";
  ans1 = ans1 + "<td>";
  if (n1 < m) {
   obj = arr[n1];
   id = iddisp_format1(obj);
   ans1 =  ans1 + n1 + ". " + id;
  }
  ans1 = ans1 + "</td>\n";
  ans1 = ans1 + " </tr>\n";
  html  = html + ans1;  
  n++;
  n1++;
 }
 // there might be one or two more
 n = n1;
 while (n < m) {
  obj = arr[n];
  id = iddisp_format1(obj);
  ans1 =  n + ". " + id;
  ans1 = "<tr><td></td><td>" + ans1 + "</td></tr>\n";
  html  = html + ans1;  
  n++;
 }
 html = html + "</table>\n";
 html = html + "</span>\n";
 ansEl.innerHTML = html;
}
function iddisp_format(id) {
 return("<span class='iddisp'>" + id + "</span>");
}
function iddisp_format1(obj) {
 var id = obj.iddisp;
// var ans1 = iddisp_format(id);
 var ans1 = id;
 var a;
 var divid = "rightpane";
 var scroll_parms = construct_scroll_parms(obj);
 var onclick = 'onclick="scroll_div(' + "'" + divid + "'" + scroll_parms +
              ');"';
 a = "<a class='iddisp1' " + onclick + ">" + ans1 + "</a>";
 a = "<span class='iddisp'>" + a + "</span>\n";
 return(a);
}

