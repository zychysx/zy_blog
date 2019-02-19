$(function () {
    $('#bbs_go_btn').click(function () {
        var bbs_go_input = $('#bbs_go_input').val();
        var all_page_num =  parseInt($('#all_page_num').html())
        var re = /^\d+$/;
        if (bbs_go_input == ''){
            alert('请输入页码')
        }else if (bbs_go_input <= 0 || bbs_go_input > all_page_num){
            alert('请输入0至'+ all_page_num + '之间的数字')
        }else if (! re.test(bbs_go_input)) {
            alert('请输入0至'+ all_page_num + '之间的数字')
        }else {
            window.location.href = '/blog_article/bbs/'+ bbs_go_input +'.html'
        }
    })
    $('#article_list_go_btn').click(function () {
        var article_list_go_input = $('#article_list_go_input').val();
        var all_page_num =  parseInt($('#all_page_num').html())
        var a_type = $('#a_type').html()
        var re = /^\d+$/;
        if (article_list_go_input == ''){
            alert('请输入页码')
        }else if (article_list_go_input <= 0 || article_list_go_input > all_page_num){
            alert('请输入0至'+ all_page_num + '之间的数字')
        }else if (! re.test(article_list_go_input)) {
            alert('请输入0至'+ all_page_num + '之间的数字')
        }else {
            window.location.href = '/blog_article/article_list/'+a_type+'/' + article_list_go_input +'.html'
        }
    })

    $('#article_go_btn').click(function () {
        var article_go_input = $('#article_go_input').val();
        var all_page_num =  parseInt($('#all_page_num').html())
        var aid = $('#aid').html()
        var re = /^\d+$/;
        if (article_go_input == ''){
            alert('请输入页码')
        }else if (article_go_input <= 0 || article_go_input > all_page_num){
            alert('请输入0至'+ all_page_num + '之间的数字')
        }else if (! re.test(article_go_input)) {
            alert('请输入0至'+ all_page_num + '之间的数字')
        }else {
            window.location.href = '/blog_article/article/'+aid+'/' + article_go_input +'.html'
        }
    })
})