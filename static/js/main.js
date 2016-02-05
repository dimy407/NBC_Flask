/**
 * Created by User on 15.01.2016.
 */


$(document).ready(function(){
    $('#NotalMap').unload(function(){
        calcMapWidth();
    });

    /*calcMapWidth();*/

    $(window).resize(function(){
        calcMapWidth();
    });

    $(document).on('click','.mapObject',function(){
        var text = $(this).attr('data-text');
        $('#description').text(text).css("border","1px");
    });

    $("#show_activity_areas").change(function () {
        if($(this).prop('checked')){
            $('.mapObject').css("background-color","#AAA");
        }else{
            $('.mapObject').css("background-color","inherit");
        }
        return false;
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

    $('#baton_draw').click();
}
