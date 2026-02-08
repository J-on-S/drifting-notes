const receiveBtn = document.getElementById("receiveBtn")
const messageBox = document.getElementById("messageBox")

receiveBtn.addEventListener("click", () => {
  fetch("../api/receive/random")
    .then(response => response.json())
    .then(data => {
      messageBox.value = data.message
    })
    .catch(err => {
      console.error(err)
      messageBox.value = "Something went wrong 😢"
    })
})
