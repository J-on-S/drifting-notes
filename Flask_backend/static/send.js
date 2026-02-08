const sendBtn = document.getElementById("sendBtn")
const messageInput = document.getElementById("messageInput")

sendBtn.addEventListener("click", () => {
  const message = messageInput.value

  // optional safety check
  if (message.trim() === "") {
    alert("Please write a message first!")
    return
  }

  fetch("../api/send", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      message: message
    })
  })
  .then(() => {
    messageInput.value = ""   // clear box
    alert("Your note has been sent 💛")
  })
})
