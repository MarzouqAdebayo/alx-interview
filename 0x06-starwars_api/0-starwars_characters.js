#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}`, function (error, _, body) {
    if (error) {
      console.log(error);
    }
    const charactersUrls = JSON.parse(body).characters;
    const characters = charactersUrls.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, function (error, _, body) {
            if (error) {
              reject(error);
            }
            resolve(JSON.parse(body).name);
          });
        })
    );

    Promise.all(characters)
      .then((names) => console.log(names.join('\n')))
      .catch((err) => console.log(err));
  });
}
