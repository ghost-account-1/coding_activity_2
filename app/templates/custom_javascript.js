<script>
    $(".js-soft-delete").click(function () {
        var btn = $(this);
        var token = '{{csrf_token}}';
        //open modal
        $("#js-delete-confirmation").modal("show");
        //update action
        $('#js-modal-form').attr('action', btn.attr("data-url"));
        return false
    });

    $(".js-like-button").click(function () {
        var btn = $(this);
        var token = '{{csrf_token}}';
        var l_url = btn.attr("data-url");
        var movie_id = btn.attr("data-movie-id");
        var l_id = "#"+movie_id+" span";
        $.ajax({
            headers: { "X-CSRFToken": token },
            url: l_url,
            type: 'post',
            dataType: 'json',
            success: function (data) {
                //update like
                $(l_id).text(data['likes']);
            }
        });
        return false
    });
</script>
