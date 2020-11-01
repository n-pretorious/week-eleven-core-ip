function submitPost() {
    $('#postForm').submit(function(event) {
        event.preventDefault()
        form = $("#postForm")

        $.ajax({
            'path': '/',
            'type': 'POST',
            'data': form.serialize(),
            'dataType': 'json',
            'success': function(data) {
                alert(data['success'])
            },
        })
        $('#postSelect').val('')
        $('#postText').val('')
    })
}

function submitBusiness() {
    $('#businessPost').submit(function(event) {
        event.preventDefault()
        form = $("#businessPost")

        $.ajax({
            'path': '/business',
            'type': 'POST',
            'data': form.serialize(),
            'dataType': 'json',
            'success': function(data) {
                alert(data['success'])
            },
        })
        $('#name').val('')
        $('#mail').val('')
    })
}