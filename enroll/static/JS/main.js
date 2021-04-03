var mybutton = document.getElementById("tpbtn");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20)
  {mybutton.style.display = "block";}
   else {mybutton.style.display = "none";}
}

function tp() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

//function con()
//    {
//        alert("button testing");
//    }
//
//function conf()
//{
//  if (confirm("AUTHENTICATION REQUIRED"))
//  {
//    var u = prompt("User Name");
//    var p = prompt("Password");
//    if (u != null)
//    {
//      document.getElementById("usr").innerHTML = u;
//      document.getElementById("pwd").innerHTML = p;
//    }
//    else
//    {
//      txt = "You pressed Cancel!";
//    }
//  }
//  else
//  {
//    txt = "You pressed Cancel!";
//  }
//}

