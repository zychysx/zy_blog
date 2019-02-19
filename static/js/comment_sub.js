$(function () {
    $('#arcticle_comment').submit(function () {
        CKEDITOR.instances['id_commen_text'].updateElement();
        $.ajax({
            url:'/comment/arcticle_comment/',
            type:'POST',
            data:$(this).serialize(),
            cache:false,
            success:function (data) {
                if (data.res == 'sucess'){
                    window.history.go(0)
                } else {
                    alert(data.msg)
                }
            }
        })
        return false
    })

    $('#article_form').submit(function () {
        CKEDITOR.instances['id_blog_text'].updateElement();
        $.ajax({
            url:'/blog_article/sub_article/',
            type:'POST',
            data:$(this).serialize(),
            cache:false,
            success:function (data) {
                if (data.res == 'sucess'){
                    window.history.go(0)
                } else {
                    alert(data.msg)
                }
            }
        })
        return false
    })

    // $('#bbs_form').submit(function () {
    //     CKEDITOR.instances['id_blog_text'].updateElement();
    //     $.ajax({
    //         url:'/blog_article/bbs.html',
    //         type:'POST',
    //         data:$(this).serialize(),
    //         cache:false,
    //         success:function (data) {
    //             if (data.res == 'sucess'){
    //                 window.history.go(0)
    //             } else {
    //                 alert(data.msg)
    //             }
    //         }
    //     })
    //     return false
    // })

})