const showCpf = document.getElementById("show-cpf");
const cpForm = document.getElementById("cp-form");
showCpf.addEventListener('click', function(event){
    cpForm.classList.toggle('d-none');
    showCpf.classList.toggle('d-none');
})

cpForm.addEventListener('reset', function(event){
    cpForm.classList.add('d-none');
    showCpf.classList.remove('d-none');
})