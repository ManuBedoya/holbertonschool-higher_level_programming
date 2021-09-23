$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data, textStatus){
    $('UL#list_movies').text(data.results[0].title)
})
