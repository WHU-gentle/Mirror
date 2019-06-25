// JavaScript Document
// echarts
// create for AgnesXu at 20161115


//折线图
var line = echarts.init(document.getElementById('line1'));
//var  data1=['2.21','2.22','2.23','2.24','2.25','22.26','2.27','2.28','2.29','2.30','3.1','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9','3.10','3.11','3.12','3.13','3.14','3.15','3.16','3.17','3.18','3.19','3.20'];
//var data2=[44,23, 42, 18, 45, 48, 49,100,64,63,26,25,86,84,39,85,94,35,75,52,76,86,46,37,57,35,75,65,34,77];

var data1 = {{var1|safe}};
var data2 = JSON.parse('{{var2|safe}}');

var data=[];
data.push(data1);
data.push(data2);
line.setOption({
    color:["#32d2c9"],
    title: {
        x: 'left',
        text: '总分',
        textStyle: {
            fontSize: '15',
            color: '#4c4c4c',
            fontWeight: 'bolder'
        }
    },
    tooltip: {
        trigger: 'axis'
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            magicType: {type: ['line', 'bar']}
        }
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
		rotate:45,
        data: data1,
        axisLabel: {
            interval:0
        }
    },
    yAxis: {
        type: 'value'
    },
	dataZoom: [
        {   // 这个dataZoom组件，默认控制x轴。
            type: 'inside', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
            start: 30,      // 左边在 10% 的位置。
            end: 100         // 右边在 60% 的位置。
        }
    ],
    series: [
        {
            name:'成绩',
            type:'line',
            data:data2,
            markLine: {data: [{type: 'average', name: '平均值'}]}
        }
    ]
}) ;



//柱状图
var pillar1 = echarts.init(document.getElementById('pillar1'));
var data=[];
var data_x=['4.20','4.21','4.22','4.23','4.24','4.25','4.26','4.27','4.28','4.29','4.30'];
var data_ya=['11','22','33','44','55','66','67','77','88','99','67'];
var data_yb=['14','54','64','46','75','58','87','67','86','87','57'];
var data_yc=['74','85','85','47','85','48','86','96','96','58','86'];
data.push(data_x);
data.push(data_ya);
data.push(data_yb);
data.push(data_yc);
pillar1.setOption({
    color:["#ce6e73","#ee804b","#ffc668"],
    title : {
        subtext: '分数（分）'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        x: 'right',
        data:['皱纹','斑点','痘印']
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            data : data_x
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'皱纹',
            type:'bar',
            data:data_ya
        },
        {
            name:'斑点',
            type:'bar',
            data:data_yb
        },
        {
            name:'痘印',
            type:'bar',
            data:data_yc
        }
    ]
}) ;



//柱状图2
var pillar2 = echarts.init(document.getElementById('pillar2'));
var data_x3=['4.20','4.21','4.22','4.23','4.24','4.25','4.26','4.27','4.28','4.29','4.30'];
var data_y3=['87','98','67','86','98','75','65','56','76','45','65'];
var data=[];
data.push(data_x3);
data.push(data_y3);

pillar2.setOption({
    color:["#00afff"],
    tooltip : {
        trigger: 'axis'
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            data : data_x3
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'index',
            type:'bar',
            data:data_y3
        }
    ]
});
