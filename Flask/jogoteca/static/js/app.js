$('form input[type="file"]').change(event => {
    let arquivos = event.target.files;
    if (arquivos.length === 0) {
      console.log('sem imagem pra mostrar')
    } else {
        if(arquivos[0].type == 'image/jpeg') {
          $('img').remove();
          let imagem = $('<img class="capa_jogo col-md-12">');
          imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
          $('figure').prepend(imagem);
        } else {
          alert('Formato não suportado')
        }
    }
  });