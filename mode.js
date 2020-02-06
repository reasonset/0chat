$id = document.getElementById.bind(document)
var entry_forms = [ $id("NameEntry"), $id("MainChat") ]

function changemode(index) {
  entry_forms.forEach(function(i) { i.style.display = "none" } )
  entry_forms[index].style.display = "initial"
}

function changename(name) {
  entry_forms[1].getElementsByTagName("form")[0].name.value = name
  changemode(1)
}

changemode(0)