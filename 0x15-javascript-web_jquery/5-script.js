$('DIV#add_item').click(function (){
    let item = $('<li></li>').text('item')
    $('DIV#add_item').append(item)
})
