// Configurações para as tabelas

(function(window, document, $, undefined){

  $(function(){

    var dtInstance2 = $('#tabela').dataTable({
        'paging': true,  // Table pagination
        'ordering': false,  // Column ordering
        'info': true,  // Bottom left status text
        'responsive': true, // https://datatables.net/extensions/responsive/examples/
    });

  });

})(window, document, window.jQuery);
