$(function () {
    var aid =$('#aid').html()
	all_chart_ajax()
	function all_chart_ajax(){
		$.ajax({
			url:'/read_num/read_num/'+ aid + '/',
			async:true,
			success:function (data) {
				all_chart(data.date_list,data.num_list)
			}
		})
	}

	function all_chart(date,num) {
		var chart = Highcharts.chart('read_num', {
		chart: {
			type: 'line'
		},
		title: {
			text: '此文章阅读量数据图'
		},
		subtitle: {
			text: '数据来源: www.zythird.com'
		},
		xAxis: {
			categories: date
		},
		yAxis: {
			title: {
				text: '阅读数'
			}
		},
		plotOptions: {
			line: {
				dataLabels: {
					// 开启数据标签
					enabled: true
				},
				// 关闭鼠标跟踪，对应的提示框、点击事件会失效
				enableMouseTracking: false
			}
		},
		series: [{
			name: '阅读量',
			data: num
		}]
		});
    }


})