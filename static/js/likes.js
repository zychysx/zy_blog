$(function () {
    $('#like_btn').click(function () {
        var aid = $('#aid').html()
        $.ajax({
            url:'/likes/like_btn/'+ aid + '/',
			async:true,
			success:function (data) {
				if (data.like_status == true){
				    $('#like_btn').removeClass('like_btn_black')
                    $('#like_btn').addClass('like_btn_red')
                    $('#like_btn').children().html('&nbsp已赞&nbsp&nbsp' +data.like_count)
                } else if (data.like_status == false) {
                    $('#like_btn').removeClass('like_btn_red')
                    $('#like_btn').addClass('like_btn_black')
                    $('#like_btn').children().html('&nbsp赞&nbsp&nbsp' + data.like_count)
                }else {
				    window.location.href = data.next_path
                }
			}
        })
    })
})