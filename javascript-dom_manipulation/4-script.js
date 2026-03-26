const addItem = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

addItem.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
