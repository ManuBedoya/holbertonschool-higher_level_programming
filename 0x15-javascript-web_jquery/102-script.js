$('INPUT#btn_translate').click(function(){
    let item = $('INPUT#language_code').val()
    $.get(`https://fourtonfish.com/hellosalut/?lang=${item}`, function(data, textStatus){
        $('DIV#hello').text(data.hello)
    })
})
