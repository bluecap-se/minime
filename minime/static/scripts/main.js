$(function() {

    var clipboard = new ClipboardJS('.btn-copy'),
        $labelCopied = $("#labelCopied");

    clipboard.on('success', function(e) {
        $labelCopied.fadeIn(100);
        setTimeout(function(){
            $labelCopied.fadeOut();
        }, 2000);
    });


    $("#formShorten").on("submit", function(e){
        e.preventDefault();

        var ajaxCall = $.post(this.action, $(this).serialize());

        ajaxCall.done(function(data){
            var href = document.location.href + "r/" + data["hash"],
                hrefAdmin = href + '+';

            $("#hash").attr("href", href).html(href);
            $("#copyUrl").attr("data-clipboard-text", href);
            $("#hashAdmin").attr("href", hrefAdmin).html(hrefAdmin);

            $(".panel.url-form").fadeOut({duration: 600, done: function() { $(".panel.result").fadeIn(600); }});
        });

        ajaxCall.fail(function() {
            alert("Something went wrong,\nplease try again soon.");
        });

        return false;
    });

    $("#usePassword").on("change", function(e) {
        $('#formPasswordField').fadeToggle(this.checked);
    });

});
