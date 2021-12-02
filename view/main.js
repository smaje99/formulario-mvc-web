const $ = element => document.querySelector(element);

const getData = () => {
    return {
        name: $('#name').value,
        alias: $('#alias').value,
        password: $('#password').value,
        date_birth: $('#birth').value,
        email: $('#email').value,
        phone: $('#phone').value,
        potential: $('#potential').value,
        sex: $('#masculino').checked,
        foreground: $('#fore').value,
        background: $('#back').value
    }
}

const registerForm = $('#register');

registerForm.addEventListener('submit', e => {
    e.preventDefault();
    fetch('/users/', {
        method: 'POST',
        body: JSON.stringify(getData()),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
        .then(() => alert('Usuario Creado'))
        .try(() => alert('Usuario no creado'));
    e.target.reset();
})

const loginForm = $('#login');

loginForm.addEventListener('submit', e => {
    e.preventDefault();
    fetch(`/users/${$('#alias-login').value}`)
        .then(data => data.json())
        .then(console.log);
})