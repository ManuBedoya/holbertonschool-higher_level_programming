$('DIV#add_item').click(function(){
    let item = $('<li></li>').text('Item')
    $('UL.my_list').append(item)
})

$('DIV#remove_item').click(function(){
    $('UL.my_list li:last-child').remove()
})

$('DIV#clear_list').click(function(){
    $('UL.my_list').html('')
})
