document.onreadystatechange  = () => {
    if(document.readyState == 'complete'){
        listarUsers();
    }
}

const listarUsers = () => {
    const container = document.getElementById("lista-usuarios");
    
    fetch('http://127.0.0.1:8000/users', {
        method: 'GET',
        headers: {'Content-Type': 'application/json'}
    }).then(response => response.json())
    .then(users => {
        const ul = document.createElement("ul");
        users.forEach(user => {
            const li = document.createElement("li");
            li.textContent = `Nome: ${user.name} - Idade: ${user.age}`;
            ul.appendChild(li);
        });
        container.appendChild(ul);
    })
    .catch(error => console.error("Erro ao listar:", error));
}