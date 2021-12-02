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

const createUser = async () => {
    const user = await fetch('/users/', {
        method: 'POST',
        body: getData(),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })

    user.json()
    return user;
}

registerForm.addEventListener('submit', e => {
    e.preventDefault();
    console.table(createUser());
})