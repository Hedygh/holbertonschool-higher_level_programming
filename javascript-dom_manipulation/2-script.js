const redHeader = document.querySelector('#red_header');
const header = document.querySelector('header');

redHeader.addEventListener('click', function () {
  header.classList.add('red');
});
