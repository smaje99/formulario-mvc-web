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

const setData = (user) => {
    $('#name').value = user.name;
    $('#alias').value = user.alias;
    $('#password').value = user.password;
    $('#birth').value = user.date_birth;
    $('#email').value = user.email;
    $('#phone').value = user.phone;
    $('#potential').value = user.potential;
    $('#masculino').checked = user.sex;
    $('#femenino').checked = user.sex;
    $('#fore').value = user.foreground;
    $('#back').value = user.background;
}

const registerForm = $('#register');
const loginForm = $('#login');
const container = $('.container');

const reset = () => {
    registerForm.reset();
    loginForm.reset();
    container.classList.add('hidden')
}

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
        .catch(() => alert('Usuario no creado'));
    reset();
})

registerForm.addEventListener('reset', reset);

loginForm.addEventListener('submit', e => {
    e.preventDefault();
    fetch(`/users/${$('#alias-login').value}`)
        .then(res => res.json())
        .then(data => {
            if (data.password === $('#password-login').value) {
                setData(data);

                container.classList.remove('hidden');
                container.style.color = data.foreground;
                container.style.backgroundColor = data.background;

                $('.greeting__name').innerText = data.name;
                $('.potential__number').innerText = data.potential;
                $('#submit').value = 'Actualizar datos';
            } else {
                alert('Contraseña no valida');
            }
        })
})