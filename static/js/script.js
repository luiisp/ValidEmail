const notice = document.getElementById('notice');

console.log('Js on')
notice.addEventListener('DOMSubtreeModified', () => {
    notice.style.opacity = 1; 
    setTimeout(() => {
      notice.style.opacity = 0; 
    }, 8000); 
  });


const form = document.querySelector('form')
  
form.addEventListener('submit', function(event) {
    // Impede o comportamento padrão do formulário para evitar que a página seja recarregada
    event.preventDefault();
    notice.textContent = 'Email Enviado!'
    // Aqui, você pode adicionar o código para processar os dados do formulário
    // ...

    // Crie um objeto FormData com os dados do formulário
    const formData = new FormData(form);

    // Use fetch para enviar os dados para o Django (ou qualquer URL desejada)
    fetch('/', {
        method: 'POST',
        body: formData,
    })

    

});

fetch('/')
    .then(response => response.json())
    .then(data => {
        console.log(data); 
    });
