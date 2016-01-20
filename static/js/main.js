/**
 * Created by User on 15.01.2016.
 */

$(document).ready(function(){
    calcMapWidth();

    $(window).resize(function(){
        calcMapWidth();
    });



    $(document).on('click','.mapObject',function(){
        var text = $(this).attr('data-text');
        $('#description').text(text).show();
    });
});

function calcMapWidth(){
    var elem =  $('.img-maps');
    var width = elem.height();
    elem.width(width);
}



function getName (str){
    if (str.lastIndexOf('\\')){
        var i = str.lastIndexOf('\\')+1;
    }
    else{
        var i = str.lastIndexOf('/')+1;
    }
    var filename = str.slice(i);
    var uploaded = document.getElementById("fileformlabel");
    uploaded.innerHTML = filename;
}
