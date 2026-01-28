async function sendMessage(){
  const message=document.getElementById("message").value;
  const language=document.getElementById("language").value;
  const res=await fetch("http://127.0.0.1:5000/chat",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({message,language})
  });
  const data=await res.json();
  document.getElementById("response").innerText=data.reply;
}