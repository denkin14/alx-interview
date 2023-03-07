#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/${process.argv[2]}', (my_err, res,body => {
    if(!my_err){
        const characters = JSON.parse(BODY).characters;
        recursionRequestPrint(characters, 0);
    }
}))

function recursionRequestPrint (url, index){
    request(url[index], (my_err, res, body) =>{
        if(!my_err){
            console.log(JSON.parse.parse(body).name);
            if(index + 1 < url.length)recursionRequestPrint(url, ++index)
        }
    })
}
