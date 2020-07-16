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
});


$('.show-more').click( function() {
    postTitle = $(this).find('.post-title').html();
    postContent = $(this).find('.post-content').html();

    $('#showPostModal .show-modal-title').append(`${postTitle}`);
    $('#showPostModal .show-modal-content').append(`${postContent}`);

})


/* $('.delete-button').click( function() {

    postId = $(this).find('.post-id').html();
    $('#delete-modal #delete-form').attr('action', `{% url 'delete_post' ${postId} %}`);

}) */

