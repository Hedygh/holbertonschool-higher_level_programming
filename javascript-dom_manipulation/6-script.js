const character = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    character.textContent = data.name;
  })
  .catch(function (error) {
    console.log(error);
  });