$(function () {
    sec_count = 60
    var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_n_name = false;
	var error_email = false;
	var error_check = false;
    var error_check_num = false;
    var error_name_repeat = false
    
    $('#check_num').click(function () {
    	check_email()
    	if(!error_email){
    		var user_email = $('#user_email').val()
        	send_check_num_ajax(user_email)
        	$(this).attr('disabled','disabled')
        	myVar_set_time = setInterval(set_time, 1000,user_email);
		}else {
		}
		
    })


    $('#user_name').blur(function () {
        check_user_name()
        check_user_name_exist(true)
    })

    $('#pass_word').blur(function () {
        check_pwd()
    })

    $('#cpwd').blur(function () {
        check_cpwd()
    })

    $('#user_email').blur(function () {
        check_email()
    })

	$('#n_name').blur(function () {
		check_n_name()
    })


    //发送验证码
    function send_check_num_ajax(user_email) {
    	$.ajax({
			url:'/blog_user/send_check_num/',
            async:true,
            data:{'user_email':user_email},
            success:function () {

            }
    	})

    }
    //删除过期验证码
    function del_num_ajax(user_email) {
        $.ajax({
            url:'/blog_user/del_num/',
            async:true,
            data:{'user_email':user_email},
            success:function () {
            }
        })
    }
    //倒计时
    function set_time(user_email) {
        sec_count = sec_count - 1
        $('#check_num').html(sec_count + '秒后可重新发送')
        if (sec_count == 0) {
            clearInterval(myVar_set_time)
            sec_count = 60
            del_num_ajax(user_email)
            $('#check_num').html('发送验证码')
            $('#check_num').removeAttr('disabled')
        }
    }
    //校验用户名格式
    function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').parent().next().html('请输入正确的用户名格式')
			error_name = true;
		}
		else
		{
			$('#user_name').parent().next().html('')
			error_name = false;
		}
	}
    //校验密码格式
	function check_pwd(){
		var len = $('#pass_word').val().length;
		if(len<8||len>20)
		{
			$('#pass_word').parent().next().html('密码最少8位，最长20位')
			error_password = true;
		}
		else
		{
			$('#pass_word').parent().next().html('')
			error_password = false;
		}
	}

    //校验密码是否相同
	function check_cpwd(){
		var pass = $('#pass_word').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').parent().next().html('两次输入的密码不一致')
			error_check_password = true;
		}
		else
		{
			$('#cpwd').parent().next().html('')
			error_check_password = false;
		}

	}
	// 检验昵称
	function check_n_name() {
		var nick_name = $('#n_name').val()
		if (nick_name.length < 4) {
			error_n_name = true;
			$('#n_name').parent().next().html('昵称长度不符合')
		} else {
			$('#n_name').parent().next().html('')
			error_n_name = false;
		}
    }
    // 校验邮箱格式
	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#user_email').val()))
		{
			$('#user_email').parent().next().html('')
			error_email = false;
		}
		else
		{
			$('#user_email').parent().next().html('你输入的邮箱格式不正确')
			error_email = true;
		}
	}
	// 校验验证码
	function check_email_num() {
		var check_num = $('#check_num_input').val()
		if (check_num.length == 6){
			$('#check_num_input').parent().next().html('')
			error_check_num = false;
		} else {
			error_check_num = true;
			$('#check_num_input').parent().next().html('你输入的验证码格式不正确')
		}
    }


	function check_user_name_exist(async) {
		// 校验用户名是否存在
		// 1.获取用户名
		user_name = $('#user_name').val()
		// 2.发起一个ajax请求
		$.ajax({
			url:'/blog_user/is_name_valid/?user_name='+user_name,
			async:async,
			success:function (data) {
				// 进行处理
				if (data.res == '0'){
					// 用户名已注册
					$('#user_name').parent().next().text('用户名已被注册').show()
					error_name_repeat = true
				}
				else
				{
					$('#user_name').parent().next().text('').html('')
					error_name_repeat = false
				}
            }
		})
    }

    $('#register_form').submit(function () {
        check_user_name();
		check_pwd();
		check_cpwd();
		check_email();
		check_n_name();
		check_email_num();
		check_user_name_exist(false);

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false && error_n_name == false && error_check_num == false && error_name_repeat == false)
		{
			return true;
		} else {
			return false;
		}
    })





})