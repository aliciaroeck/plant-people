// focus on the first input for create and edit form
$('#insert-content-modal').on('shown.bs.modal', function () {
    $('input[name=title]').trigger('focus');
});

// adding heading and button text to create modal
$('#add-post').click( function() {
    $('#insert-content-modal .modal-post-title').html("Create a New Post");
    $('#insert-content-modal .submit-button').html("Create Post");
    
    $('#insert-content-modal input[name=title]').val("");
    $('#insert-content-modal textarea[name=content]').val("");
});

//  inserts content to edit modal
$('.edit').click( function() {
    postId = $(this).find('.post-id').html();
    $('#insert-form').attr('action', `/${postId}/edit_post/`);

    $('#insert-content-modal .modal-post-title').html("Edit Post");
    $('#insert-content-modal .submit-button').html("Edit Post");

    title = $(this).find('.title').html();
    content = $(this).find('.content').html();
    $('#insert-content-modal input[name=title]').val(title);
    $('#insert-content-modal textarea[name=content]').val(content);
});

// show trancated info
$('.show-more').click( function() {
    postUser = $(this).find('.post-user').html();
    postUserImg = $(this).find('.post-user-img').html();
    postTitle = $(this).find('.post-title').html();
    postContent = $(this).find('.post-content').html();

    console.log($(this))
    $('#showPostModal .user').append(`${postUserImg}`);
    $('#showPostModal .user').append(`${postUser}`);
    $('#showPostModal .show-modal-title').append(`${postTitle}`);
    $('#showPostModal .show-modal-content').append(`${postContent}`);

    $('#showPostModal .close').click( function() {
        setTimeout(function(){
                $('#showPostModal .user').empty();
                $('#showPostModal .show-modal-title').empty();
                $('#showPostModal .show-modal-content').empty(); 
        },200)
    });
});

// delete route per modal
$('.delete-button').click( function() {
    postIdDelete = $(this).find('.post-id').html();
    $('#delete-form').attr('action', `/${postIdDelete}/delete_post/`);
});

