$(document).ready(function() {
    $('.comment-container').click(function() {
        $(this).find('.comment-actions').toggle();
    });

    $('.edit-btn').click(function() {
        $(this).closest('form').submit();
    });

    $('.delete-btn').click(function() {
        if (confirm("Are you sure you want to delete this comment?")) {
            $(this).closest('form').submit();
        }
    });
});