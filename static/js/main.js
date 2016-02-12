/**
 * Created by User on 15.01.2016.
 */


$(document).ready(function(){
    $('#NotalMap').unload(function(){
        calcMapWidth();
    });

    $(window).resize(function(){
        calcMapWidth();
    });

    $(document).on('click','.mapObject',function(){
        on_off($(this).attr('id'));
        var text = $(this).attr('data-text');
        $('#description').text(text).css("border","1px");
    });

    $('body:not(.mapObjectDescription)').click(function(){
        $('.mapObjectDescription').hide();
    });!

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

function on_off(t){
    p = document.getElementById(t+'Description');
    if(p.style.display=="none"){
        $('.mapObjectDescription').hide();
        p.style.display="block";}
    else{
        p.style.display="none";}
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
