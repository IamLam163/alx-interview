#!/usr/bin/node
/*
 * print the list of characters
 * */
// fetch('https://swapi.dev/api/people/1/')
//   .then(response => response.json())
//   .then(data => console.log(data))
//   .catch(err => console.error(err))


const url = 'https://swapi.dev/api/films/';
const args = process.argv.slice(1);

if (args.length < 2) {
  console.log('args cannot be less than two!');
} else {
  const movie = args[1];
  fetch(`${url}${movie}`)
    .then(response => response.json())
    .then(data => {
      const characters = data.characters;
      const characterNames = characters.map(characterUrl => {
        return fetch(characterUrl)
          .then(response => response.json())
          .then(CharacterData => CharacterData.name);
      });
      Promise.all(characterNames).then(names => {
        names.forEach(name => console.log(name));
      });
    })
    .catch(err => console.error(err));
}

/*
url = 'https://swapi.dev/api/films/'
movie = process.argv[2]

fetch(`${url}${movie}`)
  .then(response => response.json())
  .then(data => {
    const characters = data.characters;
    const characterNames = characters.map(characterUrl => {
      return fetch(characterUrl)
        .then(response => response.json())
        .then(characterData => characterData.name);
    });
    Promise.all(characterNames).then(names .then=> {
      names.forEach(name => console.log(name));
    });
  })
  .catch(err => console.error(err))

*/
