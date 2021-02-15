function con()
    {
        alert("button testing");
    }

function conf()
{
  if (confirm("AUTHENTICATION REQUIRED"))
  {
    var u = prompt("User Name");
    var p = prompt("Password");
    if (u != null)
    {
      document.getElementById("usr").innerHTML = u;
      document.getElementById("pwd").innerHTML = p;
    }
    else
    {
      txt = "You pressed Cancel!";
    }
  }
  else
  {
    txt = "You pressed Cancel!";
  }
}