$('#insert-content-modal').on('shown.bs.modal', function () {
    $('input[name=title]').trigger('focus')
});

$('#add-post').click( function() {
    $('#insert-content-modal .modal-post-title').html("Create a New Post");
    $('#insert-content-modal .submit-button').html("Create Post");
    
    $('#insert-content-modal input[name=title]').val("");
    $('#insert-content-modal textarea[name=content]').val("");

})

$('.edit').click( function() {
    $('#insert-form').attr('action', "{{% url 'edit_post' %}}");

    $('#insert-content-modal .modal-post-title').html("Edit Post");
    $('#insert-content-modal .submit-button').html("Edit Post");

    title = $(this).find('.title').html();
    content = $(this).find('.content').html();


    $('#insert-content-modal input[name=title]').val(title);
    $('#insert-content-modal textarea[name=content]').val(content);

})


