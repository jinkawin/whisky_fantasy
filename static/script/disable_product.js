$(document).ready(function(){
    $('.off').click(function(){
       var product_id = $(this).attr('data-id');
       var product_status = $(this).attr('data-status');
       var button = $(this);
       $.get('/app/product_status/',{'id':product_id,'status':product_status},function(data){
          $('#flag'+product_id).text('Off Shelf')
           button.hide();
           $('#edit'+product_id).hide();
       })

    })
})