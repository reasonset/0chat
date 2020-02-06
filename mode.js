$id = document.getElementById.bind(document)
var entry_forms = [ $id("NameEntry"), $id("MainChat") ]
var nameview = document.getElementById("NameView")

var registeredName

function changemode(index) {
  entry_forms.forEach(function(i) { i.style.display = "none" } )
  entry_forms[index].style.display = "initial"
}

function changename(name) {
  var form = entry_forms[1].getElementsByTagName("form")[0]
  form.name.value = name
  nameview.value = name
  if (registeredName) {
    form.chat.value = registeredName + " changes name to " + name + "."
  } else {
    form.chat.value = name + " logged in."
  }
  form.submit()
  form.chat.value = ""
  registeredName = name
  changemode(1)
}

changemode(0)