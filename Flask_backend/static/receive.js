const receiveBtn = document.getElementById("receiveBtn")
const messageBox = document.getElementById("messageBox")
const songURL = document.getElementById("url")

receiveBtn.addEventListener("click", () => {
  fetch("../api/receive/random")
    .then(response => response.json())
    .then(data => {
      messageBox.innerText = data.message
      songURL.innerHTML = data.url
    })
    .catch(err => {
      console.error(err)
      messageBox.innerText = "Something went wrong 😢"
    })
})
