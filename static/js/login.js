$(function () {
	var error_name = false
    $('#login_name').blur(function () {
        check_user_name_exist(true)
    })



	$('#submit_btn').click(function () {
		var user_name = $('#login_name').val()
		var pass_word = $('#pass_word').val()
		var csrfmiddleware = $("input[name='csrfmiddlewaretoken']").val()

		check_user_name_exist(false)
		if (error_name == true) {
			return false
		}
		var params =  {
			'user_name':user_name,
			'pass_word':pass_word,
			'csrfmiddlewaretoken':csrfmiddleware,
		}
		$.post('/blog_user/login/',params,function (data) {
			if (data.res == '1'){
					window.location.href = data.next_path
				} else {
					$('#pass_word').parent().next().html(data.login_error_msg)
				}
        })
		// $.ajax({
		// 	type:'POST',
		// 	url:'/blog_user/login/',
		// 	data:params,
		// 	dataType: "json",
		// 	success:function (data) {
		// 		if (data.res == '1'){
		// 			location.href = data.next_path
		// 		} else {
		// 			$('#pass_word').parent().next().html(data.login_error_msg)
		// 		}
         //    }
		// })
    })

	function check_user_name_exist(async) {
		// 校验用户名是否存在
		// 1.获取用户名
		var user_name = $('#login_name').val()
		// 2.发起一个ajax请求
		$.ajax({
			url:'/blog_user/is_name_valid/?user_name='+user_name,
			async:async,
			success:function (data) {
				// 进行处理
				if (data.res == '0'){
                    $('#login_name').parent().next().html('').hide()
					error_name = false
				}
				else
				{
					$('#login_name').parent().next().html('用户名不存在').show()
					error_name = true
				}
            }
		})
    }

})