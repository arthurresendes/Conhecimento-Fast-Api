document.onreadystatechange  = () => {
    if(document.readyState == 'complete'){
        const btnPost = document.getElementById("btn-envio");
        btnPost.onclick = addUser;
    }
}

const addUser = () => {
    const nome = document.getElementById("txt-user").value;
    const idade = parseInt(document.getElementById("age-user").value);
    const data = {"name": nome, "age": idade};

    fetch('http://127.0.0.1:8000/users', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => {
        console.log("Sucesso:", data);
        alert("Usuário cadastrado!"); 
    })
    .catch(error => console.error("Erro no Fetch:", error));
}