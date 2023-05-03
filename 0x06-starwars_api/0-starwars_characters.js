#!/usr/bin/node
/*
 * print the list of characters
 * */

const request = require('request');

const url = 'https://swapi.dev/api';
const args = process.argv.slice(1);

if (args.length < 2) {
  console.log('Please provide movie id!');
} else {
  const movie = args[1];
  request(`${url}/films/${movie}`, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const data = JSON.parse(body);
      const characters = data.characters;
      const characterNames = characters.map(characterUrl => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              const characterData = JSON.parse(body);
              resolve(characterData.name);
            }
          });
        });
      });
      Promise.all(characterNames).then(names => {
        names.forEach(name => console.log(name));
      });
    }
  });
}

// const request = require('request');
//
// const url = 'https://swapi.dev/api/films/';
// const args = process.argv.slice(1);
//
// if (args.length < 2) {
//   console.log('args cannot be less than two!');
// } else {
//   const movie = args[1];
//   request.get(`${url}${movie}`, (error, response, body) => {
//     if (error) {
//       console.error(error);
//       return;
//     }
//     const data = JSON.parse(body);
//     const characters = data.characters;
//     const characterNames = characters.map(characterUrl => {
//       return request.get(characterUrl, (error, response, body) => {
//         if (error) {
//           console.error(error);
//           return;
//         }
//         const characterData = JSON.parse(body);
//         return characterData.name;
//       });
//     });
//     Promise.all(characterNames).then(names => {
//       names.forEach(name => console.log(name));
//     });
//   });
// }
